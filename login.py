from getpass import getpass as PW

def login(username,password):
    if username == 'david' and password == '4life':
        return True
    
    else:
        return False
        

for i in range(3):
    un = input("enter user name")
    pw = PW("Enter password")

    if login(un,pw) == True:
        print("Welcome david !!!")
        break
    else:
        print("wrong passwor try again")

    