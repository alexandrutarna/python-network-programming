import devutils as Device

if __name__ == "__main__":
    
    Device.connect()

    Device.check()

    cmd = "show ip int brief"
    Device.execute(cmd)

    Device.show()

    Device.backup()

    Device.restart()

    Device.restore("conf_file.txt")