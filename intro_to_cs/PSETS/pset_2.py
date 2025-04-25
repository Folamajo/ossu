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

import string
def get_available_letters():
   available_letters = string.ascii_lowercase
   return available_letters

def hangman(secret_word, with_help):
   print('Welcome to Hangman!')
   print(f"I am thinking of a word that is {len(secret_word)} letters long.")
   print('--------------------')

   guesses = 10 
   while guesses > 0:
      print(f'You currently have {guesses} left')
      print(f'Available letters: {get_available_letters}')
      guess = input("Please guess a letter: ")

if __name__ == '__main__':
   secret_word = "tact"
   with_help = False
   hangman(secret_word, with_help)
   print(get_available_letters())