#!/usr/bin/python
# python ex31.py

from sys import *

script, name = argv

# Frequently used strings
prompt = "> "
fail = "I don't know that one, try again."
bye = "Thanks for playing!"

# Exit options
def dead(death):
	print death, "Fantastic!"
	print "Would you like to try again?"
	print "'Yes' or 'No'?"
	restart = raw_input(prompt)
	if restart.upper() == "YES":
		start()
	elif restart.upper() == "NO":
		exit(bye)
	else:
		leave()

def leave():
	print "bye"
	exit(bye)


# Game Begin and Housekeeping
def begin():
	print "Welcome to Demon's Run"
	print "We are very glad to have you."
	print "A few housekeeping tips to make your stay enjoyable."
	print "1. Each prompt has a few words in single quotes, like 'this'."
	print "   Those words are commands you can give the game to make decisions."
	print "2. At any time, you can exit the game by simply typing 'quit'."
	print "3. Anything you run into can be killed or subdued, if you only have the resources."
	print "4. At any time, as long as you're not dead, you can go backward, simply type 'back' or 'run'"
	print "5. Have fun and don't do anything I wouldn't do."
	print "Ready to start (Y/N)?"
	begin = raw_input(prompt)
	if begin.upper() == "Y" or begin.upper() == "YES":
		start()
	elif begin.upper()  == "QUIT" or begin.upper() == "N" or begin.upper() == "NO":
		leave()

# Game Start
def start():
	print "Hello, %s, how are you?" % name
	print "You have awoken from a trance."
	print "You are standing in a clearing at night,"
	print "a path goes 'north' to 'south', which path do you take?"

	start = raw_input(prompt)

	path(start)

	exit()


def path(direction):
	if direction.upper() == "NORTH" or direction.upper() == "N":
		print "The path leads to a graveyard." 
		print "The graves look as though they haven't been touched in decades."
		print "You see red glowing 'eyes' in the treeline."
		print "You can go forward toward the 'eyes' or 'back' to the clearing, what do you do?"
	
		eyes_choice = raw_input(prompt)

		eyes(eyes_choice)

	elif direction.upper() == "SOUTH" or direction.upper() == "S":
		print "You come upon an older, antebellum house."
		print "It has a metal, but very rusted, but comfortable looking 'swing'."
		print "The 'door' is slightly open, and you can enter the house. What do you do?"

		house_choice = raw_input(prompt)
		
		house(house_choice)
	elif direction.upper() == "QUIT":
		leave()
	else :
		start()


def house(choice):
	if choice.upper() == "SWING" or choice.upper() == "SIT":
		print "You sit on the swing."
		print "It barely supports you, but is a good place to rest."
		print "You can 'swing' on the swing, but it seems unsafe."
		print "You see 'carvings' in the arms of the swing."
		print "What do you do?"

		swing_choice = raw_input(prompt)

		swing(swing_choice)

	elif choice.upper() == "DOOR" or choice.upper() == "HOUSE" or choice.upper() == "ENTER":
		print "You push the door open, and are inside a large foyer."
		print "There is a rug immediately inside the door on the floor."
		print "Stepping on the rug, you feel a slight give in the floor, just before you fall through it."
		print "You find yourself in a 'tunnel' that looks fairly modern and continues into darkness."
		print "The tunnel has a 'ladder' back to the surface."
		print "What do you do?"

		tunnel_choice = raw_input(prompt)

		tunnel(tunnel_choice)
	elif choice.upper() == "BACK" or choice.upper() == "RUN":
		start()
	elif choice.upper() == "QUIT":
		leave()
	else:
		path("S")


def tunnel(choice):
	if choice.upper() == "DARK" or choice.upper() == "TUNNEL" or choice.upper() == "TOWARD":
		# make a fight with something?
		dead("You are eaten by a grue.")
	elif choice.upper == "LADDER" or choice.upper() == "RUN" or choice.upper() == "BACK":
		path("S")
	elif choice.upper() == "QUIT":
		leave()
	else:
		exit(dead(fail))

def swing(choice):
	if choice.upper() == "SWING":
		# make a resource for a stake.
		dead("That was really dumb. You're now impaled on the wreckage of the swing.")
	elif choice.upper() == "READ" or  choice.upper() == "CARVINGS":
		# make a resource for a spell.
		dead("Your brain is turned to mush and pours out of your eyes. Cthulhu has been summoned.")
	elif choice.upper() == "BACK" or choice.upper() == "RUN":
		path("S")
	elif choice.upper() == "QUIT":
		leave()
	else:
		exit(dead(fail))


def eyes(choice):	
	if choice.upper() == "EYES" or choice.upper() == "TREELINE":
		print "You reach the space where you thought the eyes were,"
		print "but nothing is there. Far in the distance, you see what looks like the same eyes."
		print "You can go toward the 'eyes' or you can go back to the 'graveyard', what do you do?"
		
		eyes2 = raw_input(prompt)
		
		if eyes2.upper() == "EYES" or eyes2.upper() == "FORWARD":
			dead("You trip on a root and die, the lights you saw were lightning bugs. You're colorblind.")
		elif eyes2.upper() == "GRAVEYARD" or eyes2.upper() == "BACK" or eyes2.upper() == "PATH":
			path("EYES")
		elif choice.upper() == "QUIT":
			leave()
		else:
			exit(dead(fail))
	elif choice.upper() == "BACK" or choice.upper() == "PATH" or choice.upper() == "CLEARING":
		start()
	elif choice.upper() == "QUIT":
		leave()
	else:
		exit(dead(fail))

begin()