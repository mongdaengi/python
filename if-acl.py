aclNum = int(input("what is the IPv4 ACL number?"))
#if aclNum >= 1 and aclNum <=99:
if 1<= aclNum <= 99 :
    print("This is a standard IPv4 ACL.")
#elif aclNum >= 100 and aclNum <= 199:
elif 100 <= aclNum <= 199 :
    print("This is an extended IPv4 ACL.")
else:
    print("This is not a standard or extended IPv4 ACL.")
