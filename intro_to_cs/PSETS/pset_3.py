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
   if not word_list:
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
      raise TypeError("Wrong input type.")
   
   if (len(dict1) == 0 and len(dict2) == 0):
      return 0
   
   U = set().union(dict1.keys(), dict2.keys())
   delta_score = 0
   sigma_score = 0

   for word in U:
      delta_difference = abs(dict1.get(word, 0) - dict2.get(word, 0))
      delta_score += delta_difference
      sigma_difference = dict1.get(word, 0) + dict2.get(word, 0)
      sigma_score += sigma_difference
      
   result = round(1 - (delta_score / sigma_score), 2)
   return result


def get_most_frequent_words(dict1, dict2):
   if (not isinstance(dict1, dict) or not isinstance(dict2, dict)):
      raise TypeError("Wrong input type.")
   
   if (len(dict1) == 0 and len(dict2) == 0):
      return []
   
   merged_dict = {}

   max_freq = 0
   result = []

   for key, value in dict1.items():
      if key in merged_dict:
         merged_dict[key] += value
      else:
         merged_dict[key] = value

   for key, value in dict2.items():
      if key in merged_dict:
         merged_dict[key] += value
      else:
         merged_dict[key] = value


   for key, value in merged_dict.items():
      if value > max_freq:
         max_freq = value
   
   for key, value in merged_dict.items():
      if value == max_freq:
         result.append(key)

   sorted_list = sorted(result)
   return sorted_list





def get_tf(word_list):
   #Validate
   if not isinstance(word_list, list):
      raise TypeError("Wrong input type.")
   
   if len(word_list) == 0:
      return {}
   
   result = {}
   
   frequency_dict = get_frequencies(word_list)

   
   for key, value in frequency_dict.items():
      result[key] = (value / len(word_list))

   return result




print(get_tf(['hello', 'world', 'hello']))












# delta_freq_scores = {}
   # sigma_freq_scores = {}
# delta_freq_scores[word] = delta_difference
      # sigma_freq_scores[word] = sigma_difference

   # result = round(1 - ((sum(delta_freq_scores.values()))/ (sum(sigma_freq_scores.values()))), 2)