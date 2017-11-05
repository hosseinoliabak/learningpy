import getpass
import telnetlib

def telnetToCisco(ip, user, password):

    tn = telnetlib.Telnet(ip)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"test\n")
    tn.write(b"conf t\n")


    for i in range(2, 101):
        tn.write(b"vlan "+ str(i).encode('ascii')+ b"\n")
        tn.write(b"name Python_VLAN_" + str(i).encode('ascii') + b"\n")


    tn.write(b"end\n")
    tn.write(b"exit\n") # this is essential for the next line not to wait for EOL
    print(tn.read_all().decode('ascii'))



username = input("Enter your telnet username: ")
passwd = getpass.getpass()

HOST = [("10.10.22." + str(n)) for n in range(11, 15)]
for n in HOST:
    telnetToCisco(n, username, passwd)
