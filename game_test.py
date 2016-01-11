#!/usr/bin/python

from sys import *
from random import randint

# Game Variables
prompt = "> "
fail = "I don't know that one. \n Try again?"
bye = "Thanks for playing!"
# inventory_list = []
# lives = 3
# swing_exists = True
name = 'John Cena'
divide = '-' * 20

# Game Setup Object/Classes
class Room(object):

	def enter(self):
		print "This room has not been configured, subclass it and run enter()."
		exit(1)
class Character(object):
	
	swing_exists = True
	
	inventory_list = []

	def inventory(self, choice):
		print "Adding %s to inventory." % choice
		self.inventory_list.append(choice)
		print "Your inventory contains: ", self.inventory_list


	def lives(self):
		lives = 3
		print "You have %s lives left." % self.lives

	def name(self):
		self.name = name
		print "Your name is: John Cena"

class Engine(object):

	def __init__(self, room_map):
		self.room_map = room_map

	def play(self):
		current_room = self.room_map.opening_room()
		last_room = self.room_map.next_room('completed')

		while current_room != last_room:
			next_room_name = current_room.enter()
			current_room = self.room_map.next_room(next_room_name)

		current_room.enter()

# Startup Rooms
class Startup(Room):
	def enter(self):
		print "What is your name?"
		crap = raw_input()
		print "Did you say '%s'?" % name
		yn = raw_input()
		print "Are you sure?"
		yn = raw_input()
		print "Your name is John Cena."
		return 'opening'

class Opening(Room):

	def enter(self):
		print "Welcome to Demon's Run"
		print "We are very glad to have you."
		print "A few housekeeping tips to make your stay enjoyable."
		print "1. Each prompt has a few words in single quotes, like 'this'."
		print "   Those words are commands you can give the game to make decisions."
		print "2. At any time, you can exit the game by simply typing 'quit'."
		print "3. Anything you run into can be killed or subdued, if you only have the resources."
		# print "4. At any time, as long as you're not dead, you can restart, simply type 'return' or 'start'."
		print "5. Have fun and don't do anything I wouldn't do."
		# print "6. You can check the status of your character at any time, simply type 'lives', 'character', or 'inventory'."
		print "Ready to 'start' or would you like to 'quit'?"

		start = raw_input(prompt).upper()
		
		if start == "START":
			print "Hello, %s, how are you?" % name
			print "You have awoken from a trance."
			return 'start'
		elif start == "QUIT":
			return 'quit'
		else:
			print fail
			return 'opening'
# Level 1
class Start(Room):
	def enter(self):
		print "You are standing in a clearing at night,"
		print "a path goes 'north' to 'south', which path do you take?"
		
		start_dir = raw_input(prompt).upper()

		if start_dir == "NORTH":
			return 'north'
		elif start_dir == "SOUTH":
			return 'south'
		elif start_dir == "QUIT":
			return 'quit'
		else:
			print fail
			return 'start'

# Level 2
class North(Room):
	def enter(self):
		print "The path splits in two:"
		print "One path heads further 'north' to what looks like a graveyard."
		print "The other path heads 'east' and you are unable to see where it ends."
		
		north = raw_input(prompt).upper()

		if north == "NORTH":
			return 'graveyard'
		if north == "EAST":
			return 'east'
		elif north == "QUIT":
			return 'quit'
		else:
			print fail
			return 'start'


class South(Room):
	def enter(self):
		print "You are in the front yard of an older, antebellum house."
		print "It has a wooden, but comfortable-looking swing on the front porch you can 'sit' in."
		print "The door is slightly open, and you can enter the 'house'." 
		print "What do you do?"

		south = raw_input(prompt).upper()

		if south == "SIT":
			return 'swing'
		if south == "HOUSE":
			return 'house'
		elif south == "QUIT":
			return 'quit'
		else:
			print fail
			return 'start'

# Level 3
class Graveyard(Room):
	def enter(self):
		print "You are standing in a graveyard." 
		print "The graves look as though they haven't been touched in decades."
		print "You see red glowing eyes in the treeline."
		print "You can examine the 'graves', go toward the 'eyes', or 'return' to the clearing, what do you do?"

		g_yard = raw_input(prompt).upper()

		if g_yard == "GRAVES":
			return 'graves'
		elif g_yard == "EYES":
			return 'eyes'
		elif g_yard == "RETURN":
			return 'start'
		elif g_yard == "QUIT":
			return 'quit'
		else:
			print fail
			return 'start'

class East(Room):
	def enter(self):
		print "You come upon a cabin that is obviously abandoned."
		print "The door is closed, but doesn't appear to have a handle."
		print "Would you like to 'look' around the cabin or 'enter' the cabin?"

		east = raw_input(prompt).upper()

		if east == "LOOK":
			print "You thoroughly search for useful items, and find nothing."
			return 'east'
		elif east == "ENTER":
			return 'cabin'
		elif east == "RETURN":
			return 'north'
		elif east == "QUIT":
			return 'quit'
		else:
			print fail
			return 'north'

class House(Room):
	def enter(self):
		print "Upon entering the house, you find yourself in a foyer."
		print "There are 'stairs' that go to the second floor,"
		print "as well as a 'hallway' that is dimly lit, but seems to have a door at the end of it."
		print "What would you like to do?"

		house = raw_input(prompt).upper()

		if house == "STAIRS":
			return 'stairs'
		elif house == "HALLWAY":
			return 'tunnel'
		elif house == "RETURN":
			return 'south'
		elif house == "QUIT":
			return 'quit'
		else:
			print fail
			return 'opening' 

class Swing(Room):
	def enter(self):
		print "Swing:", John_Cena.swing_exists
		if John_Cena.swing_exists == True:
			print "You sit on the swing."
			print "It barely supports you, but is a good place to rest."
			print "You can 'swing' on the swing, but it seems unsafe."
		print "You see 'carvings' in the wooden arms of the swing."
		print "What do you do?"

		sit = raw_input(prompt).upper()

		if sit == "SWING":
			return 'stake'
		elif sit == "CARVINGS":
			return 'carvings'
		elif sit == "RETURN":
			return 'south'
		elif sit == "QUIT":
			return 'quit'
		else:
			print fail
			return 'opening' 		

# Level 4
class Eyes(Room):
	def enter(self):
		print "You reach the space where you thought the eyes were,"
		print "but nothing is there. Far in the distance, you see what looks like the same eyes."
		if 'STONE' in John_Cena.inventory_list:
			print "You can throw your 'stone' at the lights."
		print "You can go forward, to the 'lights'."
		print "You can go back to the 'graveyard', what do you do?"


		eyes = raw_input(prompt).upper()

		if eyes == "LIGHTS":
			return 'lights'
		elif eyes == "GRAVEYARD":
			return 'graveyard'
		elif eyes == "STONE" and 'STONE' in John_Cena.inventory_list :
			throw = randint(1,10)
			John_Cena.inventory_list.remove('STONE')
			if throw > 1:
				print "You manage to throw your stone into the woods, but nothing happens."
				print "The stone disappears, and you are unable to find it."
				print "'STONE' removed from your inventory."
				return 'graveyard'
			if throw == 1:
				print "You hit one of the lights."
				print "It seems that the lights were fireflies."
				print "Disappointed, you return to the graveyard."
				print "The stone disappears, and you are unable to find it."
				print "'STONE' removed from your inventory."
				return 'graveyard'
		elif eyes == "QUIT":
			return 'quit'
		else:
			print fail
			return 'opening'

class Graves(Room):
	def enter(self):
		print "You examine the graves and find a fist-sized stone."
		print "You pick up the stone and store it in your satchel."
		John_Cena.inventory("STONE")
		return 'graveyard'

class Cabin(Room):
	def enter(self):
		print "Once inside the cabin, you find a single room with one large bed and one small bed."
		print "There is a single 'box' at the end of each bed, one locked, and the other unlocked."
		print "On a shelf, you find a 'doll' that looks worn, but otherwise, normal. What do you do?"

		cabin = raw_input(prompt).upper()
		
		if cabin == "DOLL":
			return 'doll'
		if cabin == "BOX":
			return 'box'
		elif cabin == "QUIT":
			return 'quit'
		else:
			print fail
			return 'opening'

class Stake(Room):
	def enter(self):
		print "That was really dumb. You're now sitting on the wreckage of the old swing."
		print "A very sharp piece, almost a stake of wood sits beside you."
		print "You pick up the wooden stake."

		print "Swing exists:", John_Cena.swing_exists		
		John_Cena.swing_exists = False
		print "Swing exists:", John_Cena.swing_exists

		John_Cena.inventory("STAKE")
		print "You are sitting on the pile of wood."
		return 'sit'

class Tunnel(Room):
	def enter(self):
		print "The hallway ends at a door."
		print "Upon reaching the door, you open it and step down into the basement."
		print "The basement looks fairly modern, and it looks"
		print "to 'continue' for hundreds of feet away from the house."
		print "Would you like to 'continue' into the tunnel or go 'back'?"

		tunnel = raw_input(prompt).upper()
		
		if tunnel == "CONTINUE":
			return 'boss'
		elif tunnel == "BACK":
			return 'house'
		elif tunnel == "QUIT":
			return 'quit'
		else:
			print fail
			return 'opening'

class Stairs(Room):
	def enter(self):
		print "You head up the stairs and find a small child's room."
		print "Upon entering the room, you see a family photo on the wall. "
		print "Looking at the photo, you feel a presence surround you." 
		print "The aura feels full of love and protection."
		John_Cena.inventory("AURA")
		return 'cabin'

# Level 5
class Box(Room):
	def enter(self):
		print "You open the box and find a small book."
		print "Upon opening the book, you hear voices inside "
		print "your head that tell you the secret to combat." 
		print "'Don't get hit', it says."
		print "You take the book with you, because reasons."
		John_Cena.inventory("BOOK")
		return 'cabin'

class Doll(Room):
	def enter(self):
		print "You pick up the doll, and find a name on its dress."
		print "The name reads: Annabel Lee."
		print "You find small specks of blood on the dolls face."
		print "Sensing how important this doll may be, you keep the doll."
		John_Cena.inventory("DOLL")
		return 'cabin'

class Lights(Room):
	def enter(self):
		print "You go toward the lights, and on your way, you trip."
		if len(John_Cena.inventory_list) >= 1:
			"Your bag opens and you lose an item."
			item_lost = John_Cena.inventory_list[randint(0,len(John_Cena.inventory_list)-1)]
			print "You lost:", item_lost
			John_Cena.inventory_list.remove(item_lost)
		return 'eyes'

# Final Boss Fight
class Boss(Room):
	pass	
# Exit Rooms
class Death(Room):
	quips = [
		"You died.  You kinda suck at this.", 
		"Your mom would be proud...if she were smarter.", 
		"Such a luser.", 
		"I have a small puppy that's better at this."
	]
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

class Quit(Room):
	def enter(self):
		print "Sad to see you go, but thanks for playing!"
		print "*Five Nuckle Shuffles Away*"
		exit()

class Finished(Room):
	def enter(self):
		print "You won!"
		print "Congratulations"
		return 'finished'

class Map(object):

    rooms = {
    	# Setup
    	'startup' : Startup(),
        'opening' : Opening(),
        # Level 1
        'start' : Start(),
        # Level 2
        'north' : North(),
        'south' : South(),
        # Level 3
        'swing' : Swing(),
        'east' : East(),
        'sit' : Swing(),
        'graveyard' : Graveyard(),
        # Level 4
        'stairs' : Stairs(),
        'cabin' : Cabin(),
        'tunnel' : Tunnel(),
        'eyes' : Eyes(),
        'stake' : Stake(),
        'graves' : Graves(),
        # Level 5
        'box' : Box(),
        'doll' : Doll(),
        'lights' : Lights(),
        # Final Boss Fight
        'boss' : Boss(),
        # Exit Rooms
        'death' : Death(),
        'quit' : Quit(),
        'finished' : Finished(),
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def opening_room(self):
        return self.next_room(self.start_room)

John_Cena = Character()
a_map = Map('startup')
a_game = Engine(a_map)
a_game.play()
