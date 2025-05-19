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