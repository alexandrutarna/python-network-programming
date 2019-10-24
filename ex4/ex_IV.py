# import devutils as Device
import paramiko
import time
import os

ip_address = "192.168.122.10"

username = "sasa"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_connection = None
output = None


def connect():
    ssh_client.connect(hostname=ip_address, username=username, password=password)
    print("successful connection " + ip_address )

def check():
    response = os.system("ping -c 1 " + ip_address)

    #and then check the response...
    if response == 0:
        print (ip_address + ' is up!')
    else:
        print (ip_address + ' is down!')

def execute(cmd):
    cmd += '\n'
    remote_connection.send(cmd)

def show():
    time.sleep(2)
    output = remote_connection.recv(65535)
    print(output.decode())

def backup():

    # Disable paging on Brocade.
    execute('terminal length 0')
    time.sleep(2)
    run_cmd = "sh run"
    execute(run_cmd)
    time.sleep(1)
 
    output = remote_connection.recv(65535)
    
    print("-----=======================================-----------")
    print(output)

    print("writing configuration to 'backup.txt'")
    log = open("backup.txt", "wb+")
    log.write(output)
    log.close()


def restart():
    reboot_cmd = "reload"

    # if connected already
    if ssh_client.get_transport() is not None:
        execute("en")
        execute(reboot_cmd)
        time.sleep(0.1)
        execute('y')        # confirm reload

        output = remote_connection.recv(65535)
        print("-----=======================================-----------")
        print(output.decode())
    # if not connected
    else:
        connect()
        execute(reboot_cmd)
        time.sleep(0.1)
        execute('y')       # confirm reload 
        output = remote_connection.recv(65535)
        print("-----=======================================-----------")
        print(output.decode())

def restore(conf):
    with open(conf) as f:
        lines = f.read().splitlines()
    print (lines)

    for cmd in lines:
        execute(cmd)
        time.sleep(0.1)
        print(cmd)

    # output = remote_connection.recv(65535)
    # print(output)


if __name__ == "__main__":
    
    # Device.connect()

    # Device.check()

    # cmd = "show ip int brief"
    # Device.execute(cmd)

    # Device.show()

    # Device.backup()

    # Device.restart()

    # Device.restore("conf_file.txt")



    #connect
    connect()
    remote_connection = ssh_client.invoke_shell()
    #clear the buffer
    output = remote_connection.recv(1000)
    print(output)

    #check
    check()

    
    # execute
    cmd = "sh ip int brief"
    print("execute({})".format(cmd))
    execute(cmd)

    cmd = "sh ssh"
    print("execute({})".format(cmd))
    execute(cmd)

    # show
    print("show()\n")
    show()
    

    # backup    
    # backup()

    # restart 
    restart()

    #restore
    # restore("backup.txt")


    ssh_client.close