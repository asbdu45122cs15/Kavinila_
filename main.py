# taking input from the user
num = int(input("Enter any number:"))

# storing factorial value in a variable
factorial = 1

# check if the number is negative, positive, or zero
if num < 0:
   print("Factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
      factorial = factorial*i
   print("The factorial of",num,"is",factorial)
  year = 2000
if (year % 400 == 0) and (year % 100 == 0):
  print("{0} is a leap year".format(year))
elif ( year % 4 == 0) and (year % 100 != 0 ):
  print("{0}is a leap year".format(year))
else:
  print("{0} is not a leap year".format(year))