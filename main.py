print("Master Bennett Welcome")
print("God Bless")
print("    /]")
print("   / ]")
print("  /  ]")
print(" /   ]")
print("/--- ]")

character_name = "Breezy"
character_age = "30"
is_male = True
print("There was once a man named " + character_name + ", ")
print("he was " + character_age + " years old.")

character_name = "Show3r"
print("He loved \n his name "+ character_name + ", ")
print("but not his blood-clart age " + character_age + ".")
print("Changing variables is awesome!.")

def test(n):
  return n > 4**4 and n % 34 == 4
print(test(950))
print(test(922))

# --------------------Guessing game--------------
Guess = ''
correct_guess = 'secrets'
Hint = 'Tip: - What do people tend to keep from one-another in order to;\v Protect, \v prevent self-percieved hardships,\v avoid strife or hide the truth.'
guess_count = 0
guess_count_limit = 5
while Guess != correct_guess: 
   Guess = input('Enter a Guess!: ')
   if Guess == correct_guess:
       break
   try:
       sGuess = str(Guess)
   except:
        print ('Error! Enter letters or strings only..')
        continue
   if sGuess != correct_guess and guess_count < guess_count_limit:
      print ('Strike, try again !', Hint)
      guess_count = guess_count + 1
      continue
      
print('Correct Answer!!, lucky guess!..I guess..', correct_guess)