#Day1: understand how it works
#Day2: 
# Make a list ofwords so computer can choose random word
# Ask user for input 
#write has player won function
#get_word_progress
#get_available_letters should returns the string in alphabetical order 

#hangman function
   #takes in two parameters, (secret word, with_help)
   # variables: guesses(10)
   # count of how many words the user has to guess
   # Show avaliable letters
   # prompt to guess a letter: 
   # Good guess or bad guess
   # wrong vowels take off 2 points 


# Todo :-
# Validate the guess
import string
import random

# list_of_words = ['apple', 'banana', 'tree']
# random_word = random.choice(list_of_words)
# print(random_word)

def get_available_letters(letters_guessed = None):
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
   
   #create a string that has Unique letters that are in both the secret word and the avaiable letters 
   #apple
   
   #It should accept two parameters secret_word and letter_guessed
   #It should return revealed word
   #Validate parameters



def hangman(secret_word, with_help):

   guesses = 10
   letters_guessed = []

   #INTRO
   print("Welcome to Hangman!")
   print(f"I am thinking of a word that is {len(secret_word)} letters long.")

   #GAME LOOP
   while guesses > 0 and not has_player_won(secret_word, letters_guessed):
      print
   # WHILE guesses remain AND player hasn’t won:
   #  - Show visual separator (---)
   #  - Show guesses left
   #  - Show available letters
   #  - Ask for input
   #  - Validate input:
   #      - Already guessed? → Warn
   #      - Not a letter? → Warn
   #      - Valid + in word? → Add, confirm
   #      - Valid + NOT in word? → Penalize
   #      - Vowel miss? → -2 guesses
   #      - Consonant miss? → -1 guess
   #      - Input is "!" AND help allowed? → Call helper function, -3 guesses
   #  - Show word progress
   # 

   


if __name__ == '__main__':
   secret_word = "tact"
   with_help = False
   hangman(secret_word, with_help)
   # print(get_available_letters())
   
   
   
   
   # if guess in secret_word:
      #    for letter in secret_word:
      #       if guess == letter:
      #          revealed_word += guess
      #       else:
      #          revealed_word += "*"
      
      # print(f"Good guess : {revealed_word}")
      # print('--------------------')
      # 
      # 
      # 
      # print('Welcome to Hangman!')
   # print(f"I am thinking of a word that is {len(secret_word)} letters long.")
   # print('--------------------')

   # num_of_guesses_left = 10 
   
   # # while num_of_guesses_left > 0:
   # revealed_word = ""
   # # available_letters = string.ascii_lowercase

   # while True:
   #    # print(f'You have {num_of_guesses_left} guesses left.')
   #    # print(f'Available letters: {get_available_letters()}')
   #    # guess = input("Please guess a letter: ") #Validate the guess 
   #    # get_available_letters(guess)
      
   #    print(f'You have {num_of_guesses_left} guesses left.')
   #    print(f'Available letters {get_available_letters()}')
   #    guess = input("Please guess a letter: ") #Validate the guess 
      
   #    # available_letters = available_letters.replace('guess', '')
   #    get_available_letters(guess)
   #    if guess == "1":
   #       break