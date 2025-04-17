# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y” 
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.
import math

def get_valid_number(prompt):
   while True:
      try:
         valid_number= int(input(prompt))
         if type(valid_number) == int and valid_number > 0:
            break
      except:
         print("Please enter a valid number input")

   return valid_number
# while True:
#    x = int(input('Enter a number "x":'))
#    if type(x) == int:
      # break 
      # y = int(input('Enter a number "y":'))

print(get_valid_number('Enter a number:'))

# try:
#    while True:
#    x = int(input('Enter a number "x":'))
#    y = int(input('Enter a number "y":'))
# except: 
#    print("Please input a number")
# print(x)
# print(x ** y)
# print(math.log2(x))

