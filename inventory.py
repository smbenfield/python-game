#!/usr/bin/python

from sys import exit

prompt = ">> "
inventory = {
	}
bye = "Thanks for using inventory manager!"
def inventory_mgr(choice):
	if choice == "1":
		search()
	if choice == "2":
		inv_input()
	else:
		exit(bye)
def inv_input():
	print "What would you like to add to your inventory?"
	item_input = raw_input(prompt).upper()

	print "What does it do?"
	item_description = raw_input(prompt).upper()

	print "Adding %r to your inventory." % item_input
	inventory[item_input] = [item_description]

def search():
	print "What would you like to search for? ('Nothing' to end)"
	search_obj = raw_input(prompt).upper()
	if search_obj == "NOTHING":
		exit(bye)
	for item in inventory:
		if item == search_obj:
			print item
			print '1: Search again'
			print '2: Add another object'
			print '3: Exit'
			options = raw_input(prompt).upper()
			inventory_mgr(options)
		else:
			print 'not found, spelling error?'
			search()

inv_input()
search()