name=input("enter your name, last name, mother's maiden name and city:> ")
starWarName=f"Your star war name is: {name.split()[0][:3]}{name.split()[1][:3]} {name.split()[2][:2]}{name.split()[3][-3:]}"   
print(starWarName.upper())           
               