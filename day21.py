print("Math Game!")
point=0

multiple = int(input("Name your multiples"))
for i in range(1,11):
  print(f'{i} x {multiple}')
  number=i *multiple
  answer=int(input(">"))
  if answer == number:
        point +=1
        print("Great work!")

print(f'You scored {point} out of 10')
if point == 10:
  print("great job keep it up")