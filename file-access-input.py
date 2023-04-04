file=open("devices.txt","a")
while True:
    newitem=input("Enter new device name ")
#if user types exit
    if newitem == 'exit':
        print("All done!.")
        break
    file.write(newitem+"\n")

file.close()
    

