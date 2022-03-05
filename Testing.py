from netmiko import ConnectHandler

cisco = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.1',
    'username': 'admin',
    'password': 'Kode1234!',
    'secret': 'Kode1234!',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco)
net_connect.enable()



def Show_Interfaces():
    output = net_connect.send_command('show ip int brief')
    print(output)


def Selection_Menu():
    print("1. Show Interfaces")


def Input():
    input = int(input("Skriv et tal: "))
    if input == 1:
        Show_Interfaces()

def Start():
    while True:
        Selection_Menu()
        print()
        Input()
