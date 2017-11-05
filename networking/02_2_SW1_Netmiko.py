from netmiko import ConnectHandler

mydevice = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.10',
    'username': 'test',
    'password': 'test',
    'verbose': True
}

ssh_conn = ConnectHandler(**mydevice)
print("\n\n")

print(ssh_conn.send_command('sho ip int br'))

command_list = ['int l3', 'ip address 3.3.3.3 255.255.255.255']
output = ssh_conn.send_config_set(command_list)
print(output)


for i in range (2, 21):
    command_list = ['vlan '+ str(i), 'name VLAN'+ str(i)]
    output = ssh_conn.send_config_set(command_list)
    print(output)


ssh_conn.send_command('wr')