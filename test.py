################################################################################
#                  This file is for testing elements of GUIPy                  #
################################################################################

import pygame, guipy
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hello World!')

gui = guipy.GUI()
button1 = guipy.Button(10, 10, 200, 200, name="Button 1", bordered=True)
button2 = guipy.Button(300, 10, 200, 200, name="Button 2", bordered=True)

gui.add_elements([button1, button2])

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
