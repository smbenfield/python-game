#!/usr/bin/python
from sys import argv
from sys import exit
from random import randint

# Universal Variables
bye = "Thanks for playing!"
breakline = "-" * 20
fail = "I don't know that one. \n Try again?"
name = None
prompt = ">> "

class engine(object):
	def __init__(self, room_map):
		self.room_map = room_map

	def play(self):
		current_room = self.room_map.opening_room()
		last_room = self.room_map.next_room('completed')

		while current_room != last_room:
			next_room_name = current_room.enter()
			current_room = self.room_map.next_room(next_room_name)

		current_room.enter()

