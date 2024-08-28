import os, time

toDoList = []

def printList():
    print()
    for index in range(len(toDoList)):
        print(f'\033[1m{index +1}. {toDoList[index]}')

def duplicateCheck(item):
    if item in toDoList:
        print("\033[1mDuplicated item\033[0m]")
    else:
        toDoList.append(item)


while True:
    print()
    print("\033[1m      To Do List Manager\033[0m")
    print("Do you want to Add, View, Edit or Remove")
    option=input(">")
    if option.lower() == 'add':
        item = input('enter list item:> ')
        duplicateCheck(item)
    elif option.lower() == "view":
        if len(toDoList)>0:
            printList()
        else:
            print("No item on to do list")
    elif option.lower()=="edit":
        oldItem = input("item to edit:> ")
        if oldItem in toDoList:
            toDoList.remove(oldItem)
            newItem = input("enter new item:> ")
            duplicateCheck(newItem)
        else:
            print(f'{oldItem} \033[1mis not in your list\033[0m')
    elif option.lower()=='remove':
        item = input("enter item to remove:> ")
        if item in toDoList:
            print(f"Do you want to remove {item} yes or no")
            response = input(">")
            if response.lower() =='yes':
                toDoList.remove(item)
        else:
            print('item not found')
    else:
        break

            