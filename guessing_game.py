print("My program thinks of a number and the player guesses the number")

rand = input("Type in the maximum number the random integer can be")

guess = 0

number = randint(rand)

while (guess != number):
    guess = input("guess your number")
    if guess > number:
        print("Number is greater")
    else if guess < number:
        print("Number is lower")
    
  print("Guess is correct")  
