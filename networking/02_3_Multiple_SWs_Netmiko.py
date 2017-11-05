from netmiko import ConnectHandler

sw1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.10',
    'username': 'test',
    'password': 'test',
    'verbose': True
}

sw2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.20',
    'username': 'test',
    'password': 'test',
    'verbose': True
}

sw3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.30',
    'username': 'test',
    'password': 'test',
    'verbose': True
}

devices = [sw1, sw2, sw3]

for device in devices:
    ssh_conn = ConnectHandler(**device)
    for i in range (2, 6):
        command_list = ['vlan '+ str(i), 'name VLAN'+ str(i)]
        output = ssh_conn.send_config_set(command_list)
        print(output)


ssh_conn.send_command('wr')