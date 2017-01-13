################################################################################
#                      GUIPi: A GUI Framework for Pygame                       #
#                           Developed by Cody Kelly                            #
#                     Use with Python 2.7 and Pygame 1.9.1                     #
################################################################################

import pygame
from pygame.locals import *

class GUI(object):
	def __init__(self):
		self.elements = []
		
	def update(self, mouse, key, events):
		for element in self.elements:
			if element.isActive:
				element.update(mouse, key, events)
	
	def draw(self, surface):
		for element in self.elements:
			if element.isActive:
				element.draw(surface)
				
	def add_element(self, element):
		self.elements.append(element)
		element.GUIManager = self
	
	def add_elements(self, elementsList):
		self.elements += elementsList
		for element in elementsList:
			element.GUIManager = self
		
class Element(object):
	def __init__(self, x=0, y=0, name=None):
		self.x = x
		self.y = y
		self.name = name
		self.GUIManager = None
		self.isActive = True
		self.disabled = False

class Button(Element):
	'''
		Button is an object which has a position,
		
		a width and height,
		
		text that's displayed in the center of the button,
		
		a default graphic, which, if the button is given a graphic and not a size,
		the button will take its size from the default graphic,
		
		a graphic which is displayed when the button is clicked, and if no size is 
		given, it will take the size of the graphic while it is being shown
		(when the mouse is clicked and held down over the button),
		
		and lastly, a function to execute when the button is clicked.
	'''
	def __init__(self, x, y, width, height, name=None, text="", bordered=False, defaultGraphic=None, onPressGraphic=None, function=None):
		super(Button, self).__init__(x, y, name)
		self.width = width
		self.height = height
		self.text = text
		self.defaultGraphic = defaultGraphic
		self.onPressGraphic = onPressGraphic
		self.function = function
		
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.surface = pygame.Surface((self.width, self.height))
		
		self.bordered = bordered
		self.pressed = False
		self.highlighted = False
		
		self.defaultColor = pygame.Color(150, 150, 150, 255)
		self.defaultBorderColor = pygame.Color(170, 170, 170, 255)
		
		self.highlightedColor = pygame.Color(150, 150, 150, 255)
		self.highlightedBorderColor = pygame.Color(150, 150, 255, 255)
		
		self.pressedColor = pygame.Color(100, 100, 100, 255)
		self.pressedBorderColor = pygame.Color(80, 80, 80, 255)
		
		self.borderWidth = 30
	
	def update(self, key, mouse, events):
		for event in events:
			if event.type == MOUSEBUTTONDOWN and not self.pressed:
				if self.rect.collidepoint(mouse.get_pos()):
					self.pressed = True
					self.highlighted = True
				else:
					self.highlighted = False
			if event.type == MOUSEBUTTONUP and self.pressed:
				if self.rect.collidepoint(mouse.get_pos()):
					self.pressed = False
					if self.function:
						self.function(self)
			if event.type == KEYDOWN and self.highlighted:
				if event.key == K_RETURN:
					self.pressed = True
			if event.type == KEYUP and self.pressed and self.highlighted:
				if event.key == K_RETURN:
					self.pressed = False
					if self.function:
						self.function(self)
		
		if self.pressed and not self.rect.collidepoint(mouse.get_pos()) and not pygame.key.get_pressed()[K_RETURN]:
			self.pressed = False
	
	def draw(self, surface):
		if self.defaultGraphic == None:
			borderRect = pygame.Rect(-self.borderWidth / 2, -self.borderWidth / 2, self.width + self.borderWidth, self.height + self.borderWidth)
			
			if self.pressed :
				self.surface.fill(self.pressedColor)
				if self.bordered:
					pygame.draw.rect(self.surface, self.pressedBorderColor, borderRect, self.borderWidth * 2)
			else:
				if self.highlighted:
					self.surface.fill(self.highlightedColor)
					if self.bordered:
						pygame.draw.rect(self.surface, self.highlightedBorderColor, borderRect, self.borderWidth * 2)
				else:
					self.surface.fill(self.defaultColor)
					if self.bordered:
						pygame.draw.rect(self.surface, self.defaultBorderColor, borderRect, self.borderWidth * 2)
		
		surface.blit(self.surface, self.rect)
			
		