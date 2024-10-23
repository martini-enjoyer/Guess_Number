import random as rd

magic_number = rd.randint(1,10)
print("Welcome to the guessing game!") 
print("I'm thinking of a number between 1 and 10")
while True: 
  guess = int(input("What is your guess?"))
  if guess == magic_number:
    print("You guessed it!")
    break
  elif guess > magic_number:
    print("Too High!")
  else: 
    print("Too Low!")
