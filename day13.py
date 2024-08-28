grade=int(input("Enter your grade:\n"))
if grade > 100:
  print("above 100 invalid grade\n")
elif grade>=90 and grade<=100:
  print("Your grade is A+\n")
elif grade >=80 and grade<90:
  print("your grade is A\n")
elif grade >=70 and grade<80:
  print("your grade is B\n")
elif grade >=60 and grade<70:
  print("your grade is C\n")
elif grade >=50 and grade<60:
  print("your grade is D\n")
else:
  print("under 50, poor grade\n")