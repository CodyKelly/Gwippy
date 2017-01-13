################################################################################
#                  This file is for testing elements of Gwippy                 #
################################################################################

import pygame, gwippy
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hello World!')

gui = gwippy.GUI()

buttons = []

def button_function(but):
	print "You've pressed a button located at " + str(but.rect.center) + "."
	print "Its place in the elements list is " + str(gui.elements.index(but)) + "."

# for y in range(0, 100):
	# for x in range(0, 100):
		# newButton = gwippy.Button(x * 22, y * 22, 20, 20)
		# buttons.append(newButton)

newButton = gwippy.Button(10, 10, 200, 200, bordered = True, function = button_function)
buttons.append(newButton)

newButton = gwippy.Button(250, 10, 200, 200, bordered = True, function = button_function)
buttons.append(newButton)

gui.add_elements(buttons)

while True: # main game loop
	events = pygame.event.get()
	for event in events:
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	DISPLAYSURF.fill(pygame.Color("white"))
	
	gui.update(pygame.key, pygame.mouse, events)
	
	gui.draw(DISPLAYSURF)
			
	pygame.display.update()
