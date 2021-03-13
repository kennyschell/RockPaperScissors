#Importing a package to extend Python (just like we extend Sublime)
#ALWAYS KEEP IMPORTS AT THE TOP
from random import randint

# [] => this is an array
# name = [value1, value2, value3]
#array is a container that can hold multiple items, like an egg carton.
# arrays are indexed, contents are assignes as number
#the index always starts at 0
choices = ["rock", "paper", "scissors"]

#Version 1, to explain array indexing
#player_choice = choices [1]
#print("index 1 in the choice array is " + player_choice + ", which is paper")

player_choice = input("choose rock, paper, or scissors: ")

print("user chose " + player_choice)

# This will be the AI choice -> a random pick from the choices array
computer_choice = choices[randint(0, 2)]

print("computer chose " + computer_choice)

# The following is a conditional

if computer_choice == player_choice:
	print("tie")

elif computer_choice == "rock":
	if player_choice == "scissors":
		print("you lose!")
	else:
		print("you win!")

elif computer_choice == "paper":
	if player_choice == "scissors":
		print("you win!")
	else:
		print("you lose!")

elif computer_choice == "scissors":
	if player_choice == "paper":
		print("you lose!")
	else:
		print("you win!")