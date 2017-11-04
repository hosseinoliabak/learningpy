import getpass
import telnetlib

def telnettocisco(ip, user, password):

    tn = telnetlib.Telnet(ip)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"terminal length 0\n")

    tn.write(b"show run\n")
    tn.write(b"exit\n")
    return tn.read_all().decode('ascii')


username = input("Enter your telnet username: ")
passwd = getpass.getpass()

with open("01_5_Switches_IPs.txt", "r") as flSwitches:
    for line in flSwitches:
        line = line.strip()
        print("Reading the configuration of "+ line+ "...")
        with open("01_Switch"+ line+ ".conf", "w") as saveOutput:
            print("Saving the configuration of "+ line+ "...")
            saveOutput.write(telnettocisco(line, username, passwd))
            print()
print("All Done! Browse the current directory to locate the backups!")
