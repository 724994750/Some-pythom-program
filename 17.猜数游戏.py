#This is a simple game program:you can guess a number I think
#Program by FYC
import random
guess_made=0
print('This is a simple game program:Guess a number I think')
print('Program by FYC')
name=input('Hello! What is your name? Please input your name\n')

number=random.randint (1,20)
print('Well! {}! I am thinking of a number between 1 and 20 '.format(name))

while guess_made <6:
    guess=int(input('Take a guess:\n'))
    guess_made=guess_made+1

    if guess < number:
        print("Your guess is too low , try again")
    if guess > number:
        print("Your guess is too high , try again")
    if guess == number:
        break

if guess == number:
    print('Good job! You have got it! You guess my number in {0} guesses!'.format(guess_made))
    
else:
    print("Nope! You have not got it ! The number I was think of is {0}".format(number))
    
