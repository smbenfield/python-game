#!/usr/bin/python
# python ex31.py

from sys import argv
from sys import exit

script, name = argv

prompt = "> "
fail = "I don't know that one, try again."
bye = "Thanks for playing!"


def dead(death):
	print death, "Fantastic!"
	print "Would you like to try again?"
	print "Yes or No?"
	restart = raw_input(prompt)
	if restart == "Yes" or "yes":
		start()
	else:
		print "Bye!"


def start():
	print "Hello, %s, how are you?" % name
	print "You have awoken from a trance."
	print "You are standing in a clearing at night,"
	print "a path goes north to south, which path do you take?"
	print "1. North"
	print "2. South"

	start = raw_input(prompt)

	path(start)


def path(direction):
	if direction == "1":
		print "The path leads to a graveyard." 
		print "The graves look as though they haven't been touched in decades."
		print "You see red glowing eyes in the treeline, what do you do?"
		print "1. Go toward the red glowing eyes."
		print "2. Run away, back down the path."
	
		eyes_choice = raw_input(prompt)

		eyes(eyes_choice)

	elif direction == "2":
		print "You come upon an older, antebellum house."
		print "It has a metal, but very rusted swing."
		print "The door is slightly open. What do you do?"
		print "1. Sit on the swing."
		print "2. Enter the house."
		print "3. Go back to the clearing."

		house_choice = raw_input(prompt)
		
		house(house_choice)

	else :
		exit(dead(fail))


def house(choice):
	if choice == "1":
		print "You sit on the swing."
		print "It barely supports you, but is a good place to rest."
		print "You see carvings in the arms of the swing."
		print "What do you do?"
		print "1. Swing in the swing."
		print "2. Read the carvings."
		print "3. Stand up and step off of the porch."

		swing_choice = raw_input(prompt)

		swing(swing_choice)

	elif choice == "2":
		print "You push the door open, and are inside a large foyer."
		print "There is a rug immediately inside the door on the floor."
		print "Stepping on the rug, you feel a slight give in the floor, just before you fall through it."
		print "You find yourself in a tunnel that looks fairly modern."
		print "What do you do?"
		print "1. Go toward darkness."
		print "2. Return to relative safety."

		tunnel_choice = raw_input(prompt)

		tunnel(tunnel_choice)
	elif choice == "3":
		start()

	else:
		exit(dead(fail))


def tunnel(choice):
	if choice == "1":
		dead("You are eaten by a grue.")
	elif choice == "2":
		path("2")
	else:
		exit(dead(fail))

def swing(choice):
	if choice == "1":
		dead("That was really dumb. You're now impaled on the wreckage of the swing.")
	elif choice == "2":
		dead("Your brain is turned to mush and pours out of your eyes. Cthulhu has been summoned.")
	elif choice == "3":
		path("2")
	else:
		exit(dead(fail))


def eyes(choice):	
	if choice == "1":
		print "You reach the space where you thought the eyes were,"
		print "but nothing is there. Far in the distance,"
		print "you see what looks like the same eyes, what do you do?"
		print "1. Go toward the lights"
		print "2. Go back to the graveyard."
		
		eyes2 = raw_input(prompt)
		
		if eyes2 == "1":
			dead("You trip on a root and die, the lights you saw were lightning bugs. You're colorblind.")
		elif eyes2 == "2":
			path("1")
		else:
			exit(dead(fail))
	elif choice == "2":
		start()
	else:
		exit(dead(fail))

start()