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

list_of_words = ['apple', 'banana', 'tree']
random_word = random.choice(list_of_words)
print(random_word)





def get_available_letters(letter=None):
   available_letters = string.ascii_lowercase
   
   if letter is None:
       available_letters
   elif letter:
      available_letters = available_letters.replace(letter, "")


def has_player_won(secret_word, letters_guessed):
   set_secret_word = set(secret_word)
   set_letters_guessed = set(letters_guessed)
   return set_secret_word.issubset(set_letters_guessed)



def hangman(secret_word, with_help):
   print('Welcome to Hangman!')
   print(f"I am thinking of a word that is {len(secret_word)} letters long.")
   print('--------------------')

   num_of_guesses_left = 10 
   
   # while num_of_guesses_left > 0:
   revealed_word = ""
   # available_letters = string.ascii_lowercase

   while True:
      # print(f'You have {num_of_guesses_left} guesses left.')
      # print(f'Available letters: {get_available_letters()}')
      # guess = input("Please guess a letter: ") #Validate the guess 
      # get_available_letters(guess)
      
      print(f'You have {num_of_guesses_left} guesses left.')
      print(f'Available letters {get_available_letters()}')
      guess = input("Please guess a letter: ") #Validate the guess 
      
      # available_letters = available_letters.replace('guess', '')
      get_available_letters(guess)
      if guess == "1":
         break

   


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