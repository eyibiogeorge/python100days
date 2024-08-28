listOfShame=[]

def prettyPrint():
    print()
    for row in listOfShame:
        for item in row:
            print(f'{item :^10}',end=" | ")
        print()
    

while True:
    addRemove=input("add or remove:> ")
    if addRemove.strip().lower()[0]=="a":
        name = input("enter name:> ")
        age = input("enter age:> ")
        pre = input("enter your prefer computer:> ")
        row = [name,age,pre]
        listOfShame.append(row)
    elif addRemove.strip().lower()[0]=="r":
        name = input("enter name of recored to remove:> ")
        for row in listOfShame:
            if name in row:
                listOfShame.remove(row)

    exit = input("Exit y/n:> ")
    if exit.strip().lower()[0] =="y":
        break
prettyPrint()

    