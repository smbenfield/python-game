#!/usr/bin/python

rooms = {
	'room' : 'clearing', 
	'print1' : 'You have awoken from a trance.', 
	'print2' : 'You are standing in a clearing at night,', 
	'print3' : 'a path goes "north" to "south", which path do you take?'
}
#prints = {
#	'print1' : 
#}
for room, print1, print2, print3 in rooms.items():
	print print1
	print print2
	print print3