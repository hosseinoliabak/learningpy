import getpass
import telnetlib

HOST = "10.10.32.2"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"test\n")
tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"vlan 3\n")
tn.write(b"vlan 4\n")
tn.write(b"vlan 5\n")
tn.write(b"vlan 6\n")
tn.write(b"end\n")
tn.write(b"exit\n") # this is essential for the next line not to wait for EOL

print(tn.read_all().decode('ascii'))