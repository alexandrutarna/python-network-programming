from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.10',
    'username': 'sasa',
    'password': 'cisco'
}

net_connect = ConnectHandler(**R1)
print("connected to "+ R1['ip'])

cmd = "show ip int brief"
print ("send command: '" + cmd + "' to " +  R1['ip'])

output = net_connect.send_command(cmd)
print("output: \n"+ output)

print("writing output to 'output.log'")
log = open("output.log", "w+")
log.write(output)
log.close()