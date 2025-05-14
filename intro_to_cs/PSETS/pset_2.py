
import string
import random
import re

def get_available_letters(letters_guessed):
   available_letters = list(string.ascii_lowercase)
   if letters_guessed : 
      if not isinstance(letters_guessed, list) or any(not x.isalpha() or not x.islower() for x in letters_guessed):
         raise TypeError("Incorrect input")
      else:
         for letter in letters_guessed:
            if letter in available_letters:
               available_letters.remove(letter)
   
   return ''.join(available_letters)


def get_word_progress(secret_word, letters_guessed):
   word_progress = []
   if type(secret_word) != str or isinstance(letters_guessed, list) == False or not secret_word.isalpha() or any(not x.isalpha() or not x.islower()  for x in letters_guessed):
         raise TypeError("Incorrect input ")
   
   else:
      for letter in secret_word:
         if letter in letters_guessed:
            word_progress.append(letter)
         else:
            word_progress.append('*')
   
   return ''.join(word_progress)


def has_player_won(secret_word, letters_guessed):
   if (
      type(secret_word) != str or 
      isinstance(letters_guessed, list) == False or 
      not secret_word.isalpha() or
      any(not x.isalpha() or not x.islower()  for x in letters_guessed)
   ):
         raise TypeError("Incorrect input ")
   
   else:
      for letter in secret_word:
         if letter in letters_guessed:
            continue
         else: 
            return False
      return True 
   
def choose_help_letter(secret_word, available_letters):
   if (not type(secret_word) == str or 
      not secret_word.isalpha() or 
      not type(available_letters) == str or 
      not available_letters.isalpha()):
         raise TypeError("One of the parameters is incorrect")

   else:
      set_secret_word = set(secret_word)
      choose_from = []
      for letter in set_secret_word:
         if letter in available_letters:
            choose_from.append(letter)
      
      revealed_letter = random.choice(choose_from)
   return revealed_letter


def hangman(secret_word, with_help):

   guesses = 10
   letters_guessed = []
   vowels = ["a", "e", "i", "o", "u"]
   score = 0
   



   #INTRO
   print("Welcome to Hangman!")
   print(f"I am thinking of a word that is {len(secret_word)} letters long.")

   #GAME LOOP
   # while guesses > 0 and not has_player_won(secret_word, letters_guessed):
   while True:
      print("--------------------")
      if guesses > 1: 
         print(f"You have {guesses} guesses left.")
      else:
         print(f"You have {guesses} guess left.")
      
      print(f"Available letters: {get_available_letters(letters_guessed )}")
      user_input = input("Please guess a letter: ").strip()
      match = re.search('[a-z!]', user_input)
      
      #Validate users input
      if not match or len(user_input) > 1:
         print(f"Oops! that is not a valid letter. Please input a single letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
  
      else:
         if not with_help:
            if user_input in secret_word:
               if user_input not in letters_guessed:
                  letters_guessed.append(user_input)
                  print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
               else: 
                  print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
            else:
               if user_input == "!":
                  print("Sorry! I can't help you. You are playing without help mode.")
                  continue
               
               if user_input not in letters_guessed:
                  letters_guessed.append(user_input)
                  print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
                  if user_input in vowels:
                     guesses -= 2
                  else:
                     guesses -= 1
               else: 
                  print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
         
         else:
            if user_input in secret_word:
               if user_input not in letters_guessed:
                  letters_guessed.append(user_input)
                  print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
               else: 
                  print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
            else:
               if user_input == "!" and guesses >= 3:
                  revealed_letter = choose_help_letter(secret_word, get_available_letters(letters_guessed))
                  print(f"Letter revealed: {revealed_letter}")
                  letters_guessed.append(revealed_letter)
                  print(get_word_progress(secret_word, letters_guessed))
                  guesses -= 3
               elif user_input == "!" and guesses < 3:
                  print("You can only get help when you have more than 3 guesses left")
                  
               
               if not user_input == "!" and user_input not in letters_guessed:
                  letters_guessed.append(user_input)
                  print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
                  if user_input in vowels:
                     guesses -= 2
                  else:
                     guesses -= 1
               elif not user_input == "!" and user_input in letters_guessed: 
                  print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
            
            
      if has_player_won(secret_word, letters_guessed):
         print("--------------------")
         print("Congratulations, you won!")
         score += guesses + 4
         score *= len(set(secret_word))
         score += len(secret_word)
         print(f"Your total score for this game is: {score}")
         return

      elif guesses <= 0:
         print("--------------------")
         print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
         return

if __name__ == '__main__':
   secret_word = "arsenal"
   with_help = True
   hangman(secret_word, with_help)
   
   
   
   