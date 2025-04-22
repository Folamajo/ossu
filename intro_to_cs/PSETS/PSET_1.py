

#PROGRAMMING PRINCIPLES USED:
   #Separation of concerns: A  function should do one thing and do it well. - 
   #Pure Functions: A pure function relies only on its inputs and produces a predictable output with no side effects- with no side effects (e.g input() or print())
   #Single Responsibility Principle (SOLID) - The fucntion has one job it doesn't handle inputs 
   #Testability: your function can now be tested with any inputs 
#REFACTORED CODE
def calculate_months_to_save(yearly_salary, portion_saved, home_cost):
   monthly_return_rate = 0.05/12
   months = 0
   deposit = float(home_cost * 0.25)
   savings_per_month = round(float((yearly_salary * portion_saved) / 12),2)
   amount_saved = 0

   while amount_saved < deposit:
      monthly_interest = (amount_saved * monthly_return_rate)
      amount_saved += savings_per_month
      amount_saved += monthly_interest
      months += 1   

   return months


# def saving_for_house():

#    yearly_salary = float(input('Enter your yearly salary: ' ))
#    portion_to_be_saved = float(input('Enter the amount you want to save as a decimal: '))
#    cost_of_dream_home = float(input('Enter the cost of your dream home: '))

#    amount_saved = 0
   
#    monthly_return_rate = 0.05/12
#    months = 0
#    deposit = float(cost_of_dream_home * 0.25)
#    savings_per_month = round(float((yearly_salary * portion_to_be_saved) / 12),2)
   
#    while amount_saved < deposit:
#       monthly_interest = (amount_saved * monthly_return_rate)
#       amount_saved += savings_per_month
#       amount_saved += monthly_interest
#       months += 1
      

#    return months


# def saving_with_raise():
   
#    yearly_salary = float(input('Enter your yearly salary: ' ))
#    portion_to_be_saved = float(input('Enter the amount you want to save as a decimal: '))
#    cost_of_dream_home = float(input('Enter the cost of your dream home: '))
#    semi_annual_raise = float(input('Enter semi annual raise: '))
   
#    amount_saved = 0
   
#    monthly_return_rate = 0.05/12
#    months = 0
#    deposit = float(cost_of_dream_home * 0.25)
#    savings_per_month = round(float((yearly_salary * portion_to_be_saved) / 12),2)
   
#    while amount_saved < deposit:
#       if months > 0 and months % 6 == 0:
#          savings_per_month += savings_per_month * semi_annual_raise


#       monthly_interest = (amount_saved * monthly_return_rate)
#       amount_saved += savings_per_month
#       amount_saved += monthly_interest
#       months += 1
      

#    return months


# print(saving_with_raise())