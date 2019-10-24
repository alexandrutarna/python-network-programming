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


    
# 1. connect() se conecteaza si → se autentifica la echipament
def connect():
    ssh_client.connect(hostname=ip_address, username=username, password=password)
    print("successful connected to " + ip_address )
    global remote_connection 
    remote_connection = ssh_client.invoke_shell()

    #clear the buffer
    output = remote_connection.recv(1000)
    # print(output)

# 2. check() → verifica conectivitatea cu echipamentul folosind ping
def check():
    response = os.system("ping -c 1 " + ip_address)

    #check the response...
    if response == 0:
        print("--------------------------")
        print (ip_address + ' is up!')
        print("--------------------------")
    else:
        print("--------------------------")
        print (ip_address + ' is down!')
        print("--------------------------")

# 3. execute() → executa o comanda pe echipament
def execute(cmd):
    cmd += '\n'
    remote_connection.send(cmd)

# 4. show() → afiseaza outputul comenzilor date prin execute()
def show():
    time.sleep(1)
    output = remote_connection.recv(65535)
    print(output.decode())

# 5. backup() → realizeaza un backup al fisierului de configurare (ex: runningconfig
# in cazul Cisco sau o arhiva a directorului /etc in cazul Linux)
def backup():

    # Disable paging on Brocade.
    execute('terminal length 0')
    time.sleep(0.5)
    run_cmd = "sh run"
    execute(run_cmd)
    time.sleep(0.5)

    output = remote_connection.recv(65535)
    
    # print("-----=======================================-----------")
    # print(output)

    print("writing configuration to 'backup.txt'")
    log = open("backup.txt", "wb+")
    log.write(output)
    log.close()

# 6. restart() se conecteaza + autentifica → (daca nu este conectat si
# autentificat deja) si restarteaza echipamentul.
def restart():
    reboot_cmd = "reload"

    # if connected already
    if ssh_client.get_transport() is not None:
        execute("en")
        execute(reboot_cmd)
        time.sleep(0.1)
        execute('y')        # confirm reload

        output = remote_connection.recv(65535)
        print("\n", 48*'-')
        print(output.decode())
    # if not connected
    else:
        connect()
        execute(reboot_cmd)
        time.sleep(0.1)
        execute('y')       # confirm reload 
        output = remote_connection.recv(65535)
        print("\n", 48*'-')
        print(output.decode())

# 7. restore('file.txt') → executa pe un echipament Cisco comenzile precizate in
# fisierul primit ca argument (poate fi un backup anterior).
def restore(conf):
    # read configurations from file
    with open(conf) as f:
        lines = f.read().splitlines()
    # print (lines)

    # enter configuration mode
    config_cmd = "configure terminal"
    execute(config_cmd)

    # execute configs from conf file
    for cmd in lines:
        execute(cmd)
        time.sleep(0.001)
        # print(cmd)

    time.sleep(1)

    execute("show logging")
    show()
    print("\nConfiguration Sent\n CHECK the last line of the LOG listed above")
    
ssh_client.close