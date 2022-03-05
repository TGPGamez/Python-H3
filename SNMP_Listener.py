from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asyncore.dgram import udp, udp6

config.addTransport(engine.SnmpEngine,
                    udp.domainName,
                    udp.UdpTransport().openServerMode(('192.168.1.1', 161))
                    )

#Implement listener to watch for port actions