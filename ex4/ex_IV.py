import Device as Dev


if __name__ == "__main__":
    

    #connect
    print("\n",48*'=')
    print("1. connect:")
    Dev.connect()

    #check
    print("\n",48*'=')
    print("2. check:")
    Dev.check()

    
    # # execute
    print("\n",48*'=')
    print("3. execute:")
    cmd = "sh ip int brief"
    print("execute({})".format(cmd))
    Dev.execute(cmd)

    cmd = "sh ssh"
    print("execute({})".format(cmd))
    Dev.execute(cmd)

    # show
    print("\n",48*'=')
    print("4. show:")
    Dev.show()
    

    # backup 
    print("\n",48*'=')
    print("5. backup:")   
    Dev.backup()

    # restart 
    print("\n",48*'=')
    print("6. restart:")
    Dev.restart()

    #restore
    print("\n",48*'=')
    print("7. restore:")
    Dev.restore("backup.txt")

