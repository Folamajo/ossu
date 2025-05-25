# How we will build this project:
# 1. Clarify the problem
# 2. Break it into sub-problems
# 3. Discuss constrains and edgecases
# 4 Design a solution (no code yet)
# 5. Write the test first — TDD mindset
# 6. Code the solution
# 7. Refactor for clarity, modularity, and SOLID

def text_to_list(word_list):
   if not isinstance(word_list, str):
      raise TypeError("Incorrect input")
   else:
      if len(word_list) < 1:
         return []
      else:
         return word_list.split()
      

def get_frequencies(word_list):
   if any(not isinstance(value, str) for value in word_list):
      raise TypeError("One of the values is not a string")

   result = {}
   if len(word_list) < 1:
      return {}
   
   for value in word_list:
      if value in result:
         result[value] += 1
      else:
         result[value] = 1
   return result


def get_letter_frequencies(word):
   if (not isinstance(word, str)):
      raise TypeError("Please input a string")
   
   if word == "":
      return {}

   split_word = list(word)
   return get_frequencies(split_word)


   #Check if input is empty 
   #else create dict if the for loop check value in input if it is already in dict += 1 else = 1

def calculate_similarity_score(dict1, dict2 ):
   if (not isinstance(dict1, dict) or not isinstance(dict2, dict)):
      raise TypeError("Wrong input type. ")
   
   if (len(dict1) == 0 and len(dict2) == 0):
      return 0
   
   U = set().union(dict1.keys(), dict2.keys())

   delta_freq_scores = {}
   sigma_freq_scores = {}

   for word in U:
      delta_difference = abs(dict1.get(word, 0) - dict2.get(word, 0))
      sigma_difference = dict1.get(word, 0) + dict2.get(word, 0)
      delta_freq_scores[word] = delta_difference

   return U 

print(calculate_similarity_score({'hello': 2, 'world' : 4}, {'hello': 2, 'fola' : 4}))