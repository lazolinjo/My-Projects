import random

#asks for name
print('Hello. What is your name?')
name = input()

#Adds random factor and random int
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)

#if's 
for guessesTaken in range(1, 7):    #Gives 7 guesses total
    print('Take a guess.')
    guess = int(input())
s
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # this is for the correct guess

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('nope. The number I was guessing of was ' + str(secretNumber))