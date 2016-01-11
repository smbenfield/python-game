#!/usr/bin/python

from sys import *
from random import randint

# Game Variables
prompt = "> "
fail = "I don't know that one. \n Try again?"
bye = "Thanks for playing!"
inventory_list = []
lives = 3
swing_exists = True
name = 'John Cena'

# Game Setup Object/Classes
class Room(object):

	def enter(self):
		print "This room has not been configured, subclass it and run enter()."
		exit(1)
class Character(object):
	def lives(self):
		lives = 3
		print "You have %s lives left." % self.lives

	def inventory(self):
		inventory_list = []
		print "Your inventory contains: ", self.inventory_list

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
		print "4. At any time, as long as you're not dead, you can restart, simply type 'return' or 'start'."
		print "5. Have fun and don't do anything I wouldn't do."
		print "6. You can check the status of your character at any time, simply type 'lives', 'character', or 'inventory'."
		print "Ready to 'start' or would you like to 'quit'?"

		start = raw_input(prompt).upper()
		
		if start == "START":
			return 'start'
		elif start == "QUIT":
			return 'quit'
		else:
			print fail
			return 'opening'
# Level 1
class Start(Room):
	def enter(self):
		print "Hello, %s, how are you?" % name
		print "You have awoken from a trance."
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
			return 'opening'

# Level 2
class North(Room):
	def enter(self):
		print "You are standing in a graveyard." 
		print "The graves look as though they haven't been touched in decades."
		print "You see red glowing eyes in the treeline."
		print "You can examine the 'graves', go toward the 'eyes', or 'return' to the clearing, what do you do?"

		north = raw_input(prompt).upper()

		if north == "GRAVES":
			return 'graves'
		elif north == "EYES":
			return 'eyes'
		elif north == "RETURN":
			return 'opening'
		elif north == "QUIT":
			return 'quit'
		else:
			print fail
			return 'opening'

class South(Room):
	def enter(self):
		print "You are on the front porch of an older, antebellum house."
		print "It has a wooden, but comfortable-looking swing you can 'sit' in."
		print "The door is slightly open, and you can enter the 'house'." 
		print "What do you do?"

		south = raw_input(prompt).upper()

		if south == "SIT":
			return 'sit'
		if south == "HOUSE":
			return 'basement'
		elif south == "QUIT":
			return 'quit'
		else:
			print fail
			return 'opening'

# Level 3
class Eyes(Room):
	def enter(self):
		print "You reach the space where you thought the eyes were,"
		print "but nothing is there. Far in the distance, you see what looks like the same eyes."
		print "You can go forward, to the 'lights' or you can go back to the 'graveyard', what do you do?"

		eyes = raw_input(prompt).upper()

		if eyes == "LIGHTS":
			print "You tripped on a root and were impaled"
			print "The lights you saw were fireflies."
			print "They say 'You can't see us'."
			return 'death'
		elif eyes == "GRAVEYARD":
			return 'graves'
		#elif eyes == "STONE":
		#	pass
		elif eyes == "QUIT":
			return 'quit'
		else:
			print fail
			return 'opening'


# Level 4

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
    	'startup' : Startup(),
        'opening' : Opening(),
        'start' : Start(),
        'north' : North(),
        'south' : South(),
        # 'sit' : Swing(),
        # 'stake' : Stake(),
        'eyes' : Eyes(),
        # 'graves' : Graves(),
        # 
        'quit' : Quit(),
        'death' : Death(),
        'finished' : Finished(),
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def opening_room(self):
        return self.next_room(self.start_room)


a_map = Map('startup')
a_game = Engine(a_map)
a_game.play()
