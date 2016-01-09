#!/usr/bin/programming/python-game
# python game2.py
from sys import *

prompt = "> "
fail = "I don't know that one, try again."
bye = "Thanks for playing!"
inventory_list = []
lives = 3
swing_exists = True

# Game Center
def game():
	choice = raw_input(prompt).upper()
	# Level 1 - Start
	if choice == "BEGIN" or choice == "RETURN" or choice == "START":
		start()
	# Level 2 - Forest
	elif choice == "NORTH" or choice == "GRAVEYARD":
		north()
	# Level 2 - House
	elif choice == "SOUTH" or choice == "YARD" or choice == "LADDER":
		south()
	# Level 3 - Forest
	elif choice == "EYES":
		eyes()
	elif choice == "GRAVES":
		graves()
	# Level 3 - House
	elif choice == "SIT" and swing_exists == True:
		sit()
	elif choice == "HOUSE":
		house()
	# Level 4 - Forest
	elif choice == "LIGHTS":
		lights()
	# Level 4 - House
	elif choice == "SWING":
		swing()
	elif choice == "CARVINGS":
		carving()
	elif choice == "TUNNEL":
		tunnel()
	# Character Options
	elif choice == "INVENTORY" or choice == "LIVES" or choice == "CHARACTER":
		character()
	# Exit Options
	elif choice == "RESTART":
		begin()
	elif choice == "QUIT":
		leave()
	else:
		print "I don't know what that means, please try again"
		game()

# Begin Game Functions
def begin():
	global lives
	global inventory_list
	global swing_exists

	lives = 3
	inventory_list = []
	swing_exists = True

	print "Welcome to Demon's Run"
	print "We are very glad to have you."
	print "A few housekeeping tips to make your stay enjoyable."
	print "1. Each prompt has a few words in single quotes, like 'this'."
	print "   Those words are commands you can give the game to make decisions."
	print "2. At any time, you can exit the game by simply typing 'quit'."
	print "3. Anything you run into can be killed or subdued, if you only have the resources."
	print "4. At any time, as long as you're not dead, you can restart, simply type 'return' or 'start'."
	print "5. Have fun and don't do anything I wouldn't do."
	print "6. You can check the status of your character at any time, simply type 'lives', 'character', or 'inventory'."
	print "Ready to 'start' or would you like to 'quit'?"
	game()

# Level 1
def start():
	print "Hello, %s, how are you?" % name
	print "You have awoken from a trance."
	print "You are standing in a clearing at night,"
	print "a path goes 'north' to 'south', which path do you take?"
	game()

#Level 2	
def north():
	print "You are standing in a graveyard." 
	print "The graves look as though they haven't been touched in decades."
	print "You see red glowing eyes in the treeline."
	print "You can examine the 'graves', go toward the 'eyes', or 'return' to the clearing, what do you do?"
	game()

def south():
	print "You are on the front porch of an older, antebellum house."
	print "It has a wooden, but comfortable-looking swing you can 'sit' in."
	print "The door is slightly open, and you can enter the 'house'." 
	print "What do you do?"
	game()

# Level 3
def eyes():
	print "You reach the space where you thought the eyes were,"
	print "but nothing is there. Far in the distance, you see what looks like the same eyes."
	print "You can go forward, to the 'lights' or you can go back to the 'graveyard', what do you do?"
	game()

def graves():
	print "You examine the graves and find a fist-sized stone."
	inventory("STONE")
	north()

def sit():
	print "Swing:", swing_exists
	if swing_exists == True:
		print "You sit on the swing."
		print "It barely supports you, but is a good place to rest."
		print "You can 'swing' on the swing, but it seems unsafe."
	print "You see 'carvings' in the wooden arms of the swing."
	print "What do you do?"
	game ()

def house():
	print "You push the door open, and are inside a large foyer."
	print "There is a rug immediately inside the door on the floor."
	print "Stepping on the rug, you feel a slight give in the floor, just before you fall through it."
	print "You find yourself in a 'tunnel' that looks fairly modern and continues into darkness."
	print "The tunnel has a 'ladder' back to the surface."
	print "What do you do?"
	game ()


# Level 4
def carving():
	print "You feel a strange sensation in your mind, as though it is being molded by tentacles."
	print "You have gained an ability called 'sleep'. It's pretty self-explanatory."
	inventory("SLEEP")
	print "You stand and move away from the swing."
	south()

def lights():
	dead("You trip on a root and die, the lights you saw were lightning bugs. You're colorblind.")


def swing():
	print "That was really dumb. You're now sitting on the wreckage of the old swing."
	print "A very sharp piece, almost a stake of wood sits beside you."
	print "You pick up the wooden stake."
	swing_exists = False
	print "Swing exists:", swing_exists
	inventory("STAKE")
	print "You are sitting on the pile of wood."
	sit()

def tunnel():
	dead("You are eaten by a grue.")



# Character Management
def inventory(choice):
	print "Adding %s to inventory." % choice
	inventory_list.append(choice)
	print "Your inventory contains: ", inventory_list

# Exit Functions
def dead(death):
	print death, "Fantastic!"
	life()

def leave():
	print "bye"
	exit(bye)

# Character Management
def character():
	print "Your name is %s." % name
	print "Your inventory contains: ", inventory_list
	print "You have %s lives." % lives
	game()

def life():
	global lives

	if lives > 0:
		lives = lives - 1
		print "You have %s lives left." % lives
		print "Would you like to 'start' again?"
		game()

	if lives == 0:
		print "Game over!", bye

print "What is your name?"
name = raw_input()
begin()