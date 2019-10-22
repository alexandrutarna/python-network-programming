import paramiko
from paramiko.client import AutoAddPolicy

ip_address = "192.168.122.72"
username = "sasa"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(AutoAddPolicy)
remote_connection = ssh_client.invoke_shell()


# 1. connect() se conecteaza si → se autentifica la echipament
def connect():
    ssh_client.connect(hostname=ip_address, username=username,password=password)
    print("1. connect()")

# 2. check() → verifica conectivitatea cu echipamentul folosind ping
def check():
    ping_cmd = "ping " + ip_address

    print("2. check()")

# 3. execute() → executa o comanda pe echipament
def execute(cmd):
    remote_connection.send(cmd)

# 4. show() → afiseaza outputul comenzilor date prin execute()
def show():
    answer = "output from shell"

# 5. backup() → realizeaza un backup al fisierului de configurare (ex: runningconfig
# in cazul Cisco sau o arhiva a directorului /etc in cazul Linux)
def backup():
    pass

# 6. restart() se conecteaza + autentifica → (daca nu este conectat si
# autentificat deja) si restarteaza echipamentul.
def restart():
    pass

# 7. restore('file.txt') → executa pe un echipament Cisco comenzile precizate in
# fisierul primit ca argument (poate fi un backup anterior).
def restore(conf_file):
    print("7. "+ conf_file)