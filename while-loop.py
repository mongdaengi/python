#asks the user for a number
while True:
        num=input("enter a number to count to")
        if num == 'q' or num == 'quit':
            break
#convert a string value to integer value
#num=int(num)
#sn=1 #start number
#while sn<=num:
#    if sn%2==1:
#        print(sn)
#    sn=sn+1
        num=int(num)
        sn=1 #start number
        while True:
            if sn%2==0:
                print(sn)
            sn=sn+1
            if sn>num : 
                break
# num=int(num)
# sn=1 #start number
# while True:
#     if sn%2==0:
#         print(sn)
#     sn=sn+1
#     if sn>num : 
#         break



