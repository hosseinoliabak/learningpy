import getpass
import telnetlib

def telnettocisco(ip, user, password):

    tn = telnetlib.Telnet(ip)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"test\n")
    tn.write(b"conf t\n")


    for i in range(21, 101):
        tn.write(b"no vlan "+ str(i).encode('ascii')+ b"\n")

    tn.write(b"end\n")
    tn.write(b"exit\n") # this is essential for the next line not to wait for EOL
    print(tn.read_all().decode('ascii'))


username = input("Enter your telnet username: ")
passwd = getpass.getpass()

with open('01_5_Switches_IPs.txt', 'r') as flSwitches:
    for line in flSwitches:
        telnettocisco(line, username, passwd)
