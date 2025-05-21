# How we will build this project:
# 1. Clarify the problem
# 2. Break it into sub-problems
# 3. Discuss constrains and edgecases
# 4 Design a solution (no code yet)
# 5. Write the test first — TDD mindset
# 6. Code the solution
# 7. Refactor for clarity, modularity, and SOLID

def text_to_list(input):
   if not isinstance(input, str):
      raise TypeError("Incorrect input")
   else:
      if len(input) < 1:
         return []
      else:
         return input.split()
      

def get_frequencies(input):
   

   if any(not isinstance(value, str) for value in input):
      raise TypeError("One of the values is not a string")

   else:
      result = {}
      if len(input) < 1:
         return result
      else:
         for value in input:
            if value in result:
               result[value] += 1
            else:
               result[value] = 1
   #Check if input is empty 
   #else create dict if the for loop check value in input if it is already in dict += 1 else = 1