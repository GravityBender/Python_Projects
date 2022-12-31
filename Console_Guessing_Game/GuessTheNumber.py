import random

print("Set the limit for the guessing game")
lowerLimit = int(input("Enter the lower limit "))
upperLimit = int(input("Enter the upper limit "))
limit = int(input("Enter the maximum number of tries allowed"))

number = random.randint(lowerLimit, upperLimit)
print(number)

number_of_guesses = int(0)

while number_of_guesses <= limit:
    guess = int(input("Enter the number: "))
    number_of_guesses += 1
    if guess < number:
        print("Entered number is small!")
    elif guess == number:
        print("You won! It took you {0} number of guesses".format(number_of_guesses))
        break
    else:
        print("Entered number is large!")

if number_of_guesses > limit:
    print("You lost!\nYou exceeded the maximum number of guesses allowed!")
