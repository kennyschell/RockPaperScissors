#Importing a package to extend Python (just like we extend Sublime)
#ALWAYS KEEP IMPORTS AT THE TOP
from random import randint

#re-import our game variables
#gameVars is a subcomponent of the gameComponents pckg
from gameComponents import gameVars

#Define a win or lose funtion
def winorlose(status):
	#version 1 of funtion
	# print("Inside winorlose function; status is: ", status)
	print("You", status, " ! Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit. Better luck next time!")
		exit()
	elif choice == "Y" or choice == "y":
		#reset the player lives and computer lives
		#and reset player choice to False, so our loop restarts
		global player_lives
		global computer_lives
		global total_lives

		player_lives = total_lives
		computer_lives = total_lives
	else:
		print("Please print Y or N")
		#This may generate a bug we need to fix later
		choice = input("Y / N")

#player_choice ==False (comparing, can use 'is' instead)
while player_choice is False:
	print("========*/RPS GAME*/========")
	print("Computer Lives:", computer_lives, "/", total_lives)
	print("Player Lives:", player_lives, "/", total_lives)
	print("============================")

	#Version 1, to explain array indexing
	#player_choice = choices [1]
	#print("index 1 in the choice array is " + player_choice + ", which is paper")
	#\n adds a line break
	print("Choose your weapon! Or type 'quit' to exit\n")
	
	player_choice = input("choose rock, paper, or scissors: \n")
	#player_choice now equals TRUE -> it has a value

	if player_choice == "quit":
		print("You chose to quit")
		exit()

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
			#verbose way
			#player_lives = player_lives - 1
			#simplified way
			player_lives -= 1
		else:
			print("you win!")
			computer_lives -= 1

	elif computer_choice == "paper":
		if player_choice == "scissors":
			print("you win!")
			computer_lives -= 1
		else:
			print("you lose!")
			player_lives -= 1

	elif computer_choice == "scissors":
		if player_choice == "paper":
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			computer_lives -= 1

	if player_lives == 0:
		winorlose("lose")

	if computer_lives == 0:
		winorlose("won")
		

	print("Player lives:", player_lives)
	print("Computer lives:", computer_lives)

	#map the loop keep running, by setting player_choice back to False
	#unset, so that our loop condition will evaluate to True
	player_choice = False









