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
def get_available_letters(letter=None):
   available_letters = string.ascii_lowercase
   
   if letter is None:
      return available_letters
   elif letter:
      available_letters = available_letters.replace(letter, "")
      return available_letters

def hangman(secret_word, with_help):
   print('Welcome to Hangman!')
   print(f"I am thinking of a word that is {len(secret_word)} letters long.")
   print('--------------------')

   num_of_guesses_left = 10 
   
   # while num_of_guesses_left > 0:
   revealed_word = ""
   while True:
      print(f'You have {num_of_guesses_left} guesses left')
      print(f'Available letters: {get_available_letters()}')
      guess = input("Please guess a letter: ") #Validate the guess 
      get_available_letters(guess)
      
      
      if guess in secret_word:
         for letter in secret_word:
            if guess == letter:
               revealed_word += guess
            else:
               revealed_word += "*"
      
      print(f"Good guess : {revealed_word}")
      print('--------------------')
      # if guess == "1":
      #    break

      # if guess in secret_word:
      #    print(f"Good guess: " )
      #    for letter in secret_word:


   


if __name__ == '__main__':
   secret_word = "tact"
   with_help = False
   hangman(secret_word, with_help)
   print(get_available_letters())