import math
import re
import datetime

from pysnmp import hlapi


def get(target, oids, credentials, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.getCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        *construct_object_types(oids)
    )
    return fetch(handler, 1)[0]


def construct_object_types(list_of_oids):
    object_types = []
    for oid in list_of_oids:
        object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
    return object_types


def fetch(handler, count):
    result = []
    for i in range(count):
        try:
            error_indication, error_status, error_index, var_binds = next(handler)
            if not error_indication and not error_status:
                items = {}
                for var_bind in var_binds:
                    items[str(var_bind[0])] = cast(var_bind[1])
                result.append(items)
            else:
                raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
        except StopIteration:
            break
    return result


def cast(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            try:
                return str(value)
            except (ValueError, TypeError):
                pass
    return value


def get_bulk(target, oids, credentials, count, start_from=0, port=161,
             engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.bulkCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        start_from, count,
        *construct_object_types(oids)
    )
    return fetch(handler, count)


def get_bulk_auto(target, oids, credentials, count_oid, start_from=0, port=161,
                  engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    count = get(target, [count_oid], credentials, port, engine, context)[count_oid]
    return get_bulk(target, oids, credentials, count, start_from, port, engine, context)


def get_result(oid):
    result = get('192.168.1.1', [oid], hlapi.CommunityData('tgplab'))
    return result.get(oid[1:])

def get_all(oid, amount_oid):
    result = get_bulk_auto('192.168.1.1', [oid], hlapi.CommunityData('tgplab'), amount_oid)
    return result

def Get_Config_Version():
    regex = r'Version (.*?),'
    matches = re.finditer(regex, get_result('.1.3.6.1.4.1.9.9.25.1.1.1.2.7'), re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        return match.group(1)

def Get_Hostname():
    return get_result('.1.3.6.1.2.1.1.5.0')

def Get_Up_Time():
    time_ticks = get_result('.1.3.6.1.2.1.1.3.0')
    seconds = time_ticks/100
    td_str = str(datetime.timedelta(seconds=seconds))
    x = td_str.split(':')
    return x[0], 'Hours', x[1], 'Minutes', x[2].split('.', 2)[0], 'Seconds'
