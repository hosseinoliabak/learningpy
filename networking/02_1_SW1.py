import paramiko
import getpass
import time

def getUserPass():

    UseGSSAPI = paramiko.GSS_AUTH_AVAILABLE  # enable "gssapi-with-mic" authentication, if supported by python installation
    DoGSSAPIKeyExchange = paramiko.GSS_AUTH_AVAILABLE  # enable "gssapi-kex" key exchange, if supported by python installation
    # UseGSSAPI = False
    # DoGSSAPIKeyExchange = False

    default_username = getpass.getuser()
    username = input('Username [%s]: ' % default_username)
    if len(username) == 0:
        username = default_username
    if not UseGSSAPI and not DoGSSAPIKeyExchange:
        password = getpass.getpass('Password for %s@%s: ' % (username, ip))

    return username, password


def sshToCisco(hostname, username, password):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=hostname, username=username, password=password)


    remote_connection = client.invoke_shell()

    remote_connection.send(b"conf t\n")
    remote_connection.send(b"int l0\n")
    remote_connection.send(b"ip address 1.1.1.1 255.255.255.255\n")
    remote_connection.send(b"int l1\n")
    remote_connection.send(b"ip address 2.2.2.2 255.255.255.255\n")
    remote_connection.send(b"router ospf 1\n")
    remote_connection.send(b"network 0.0.0.0 255.255.255.255 area 0\n")
    remote_connection.send(b"exit\n")

    for i in range (2,21):
        remote_connection.send(b"vlan "+ str(i).encode('ascii')+ b"\n")
        remote_connection.send(b"name VLAN"+ str(i).encode('ascii')+ b"\n")
        time.sleep(0.5)

    remote_connection.send(b"end\n")
    remote_connection.send(b"exit\n")

    time.sleep(1)

    print(remote_connection.recv(65535).decode('ascii'))

    client.close()


ip = "192.168.122.10" # The IP address of SW1
username, password = getUserPass()
sshToCisco(ip, username, password)

