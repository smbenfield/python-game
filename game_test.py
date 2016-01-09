#!/usr/bin/python

rooms = {
	'clearing' : 'You have awoken from a trance.' : 'You are standing in a clearing at night,' : 'a path goes "north" to "south", which path do you take?'
}
#prints = {
#	'print1' : 
#}
for room, print1, print2, print3 in rooms.items():
	print print1
	print print2
	print print3