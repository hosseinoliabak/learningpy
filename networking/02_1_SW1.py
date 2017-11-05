import paramiko
import time

def sshToCisco()
ip = "192.168.122.10" # The IP address of SW1
username = "test"
password = "test"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=ip, username=username, password=password)

print("Successful connection "+ ip)



username = input("Enter your telnet username: ")
passwd = getpass.getpass()