import os, time
emailList=[]
emailBody = []

def prettyPrint():
  os.system("clear")
  print("Email List\n")
  for index in range(len(emailList)):
      print(f'{index}: {emailList[index]}')   

def printMessage():
    os.system("clear")
    for index in range(len(emailList)):
        print(f'Dear @{emailList[index]},\n{emailBody[index]}')
        print()


while True:
    print()
    print("SPAMMED INCO")
    print(f'1. add email\n2. remove email\n3. show email\n4. get email\n>')
    option = input("pick an option > ")
    if option =="1":
        item = input("enter an email> ")
        message=input("enter a message> ")
        emailList.append(item)
        emailBody.append(message)
    elif option =="2":
        item = input("enter an email: ")
        if item in emailList:
            emailList.remove(item)
        else:
            print(f"{item} is not in list")
    elif option =="3":
        if len(emailList)>0:
          prettyPrint()
          time.sleep(1)
          os.syste("clear")
        else:
            print("List is empty")
    elif option =="4":
        os.system("clear")
        printMessage()
    else:
        break
        

