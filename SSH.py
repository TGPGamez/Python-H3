from netmiko import ConnectHandler
import re

cisco = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.1',
    'username': 'admin',
    'password': 'Kode1234!',
    'secret': 'Kode1234!',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco)
net_connect.enable()

def Show_Cmd(cmd):
    return net_connect.send_command(cmd)

def Get_Hostname():
    return net_connect.find_prompt()[:-1]

def Get_Configuration_Version():
    #Use regex pattern to find version in command
    matches = re.finditer(r"version\s(.{2,5})", net_connect.send_command("show run | include version"), re.MULTILINE)
    print(matches)
    return "te"

def Change_Interface_Status(name, status):
    #Enable config mode
    net_connect.config_mode()
    #Check mode
    net_connect.check_config_mode()
    #Define cmd string
    command_string = "interface " + name
    #Sends command
    net_connect.send_command_timing(command_string)
    #Change status up/down
    if status == 2:
        net_connect.send_command_timing("no shutdown")
    else:
        net_connect.send_command_timing("shutdown")
    print("Changed status for " + name)
    #Exit config mode
    net_connect.exit_config_mode()
    #Save config
    net_connect.save_config()

