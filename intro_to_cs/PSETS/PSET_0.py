# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y” 
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.
import math

# Functions declared outside of main
def get_valid_number(prompt, must_be_positive = False ):
   while True:
      try:
         valid_number= int(input(prompt))
         if must_be_positive and valid_number <= 0:
            print("Please enter a real number >= 1")
         else:
            break
      except:
         print("Please enter a valid number input")

   return valid_number

def get_power_of(num1, num2):
   return num1 ** num2

def get_log_of(num):
   return math.log2(num)

#Entry Point
def main():   
   x = get_valid_number(f"Enter a number for x: ")
   y = get_valid_number('Enter a number y:', True)

   power = (get_power_of(x,y))
   log = (get_log_of(y))
   print(f'{x} raised to the power of {y}: {power}')
   print(f"Log (base 2) of {y}: {log}")
         
         
         
if __name__ == '__main__':
   main()


