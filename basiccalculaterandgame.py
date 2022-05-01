# Comments are cool
"""But there are other ways to do it"""

# The 'input' function is for user input as stated but is essentially also a 'print' function also.
# print is default

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + float(num2)
print(result)

# Another way you can print comments using the 'print' function.
# And/or setting variables for the comments to insert within the string of text for example.

print("Integers (int) are for whole numbers, but float the funtion is for decimals.")

comment = """ 
Interesting design right?
It is amazing !
Incredibles
"""
print(comment)
# f string 'f"'is a straightforward way, instead of the "+ variable +"" way using 'print()'. 
adj = "amazing"
adverb = "learning"
verb = "focus"
character = "Tony Stark"
subject = "English"
pronoun = "my"
noun = "book"
madlib = f"Cloud computing is so {adj}!. I'm currently {adverb} Python as we code right now, whilst keeping my {verb}. The prologue of my real life {character} career.\nI can even write an {subject} lesson on here for the adolescants, right!?.\nAs I attempt to incorperate everything learnt in {pronoun} mental {noun}." 
print(madlib)
