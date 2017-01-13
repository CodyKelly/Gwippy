################################################################################
#                      Gwippy: A GUI Framework for Pygame                      #
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

class Border(object):
	def __init__(self):
		pass

class ButtonStates:
	# A glorified enum
	Default, Pressed, Highlighted = range(1, 4)
		
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
		self.borderWidth = 30
		
		self.state = ButtonStates.Default
		
		self.defaultColor = pygame.Color(150, 150, 150, 255)
		self.defaultBorderColor = pygame.Color(170, 170, 170, 255)
		
		self.highlightedColor = pygame.Color(150, 150, 150, 255)
		self.highlightedBorderColor = pygame.Color(150, 150, 255, 255)
		
		self.pressedColor = pygame.Color(100, 100, 100, 255)
		self.pressedBorderColor = pygame.Color(80, 80, 80, 255)
		
		self.currentColor = self.defaultColor
		self.currentBorderColor = self.defaultBorderColor
	
	def update(self, key, mouse, events):
	
		mousePos = mouse.get_pos()
	
		if self.state == ButtonStates.Default:
			self.change_to_color_scheme(ButtonStates.Default)
			for event in events:
				if event.type == MOUSEBUTTONDOWN:
					if self.rect.collidepoint(mousePos):
						self.state = ButtonStates.Pressed
						
		elif self.state == ButtonStates.Pressed:
			self.change_to_color_scheme(ButtonStates.Pressed)
			for event in events:
				if event.type == MOUSEBUTTONUP:
					if self.rect.collidepoint(mousePos):
						self.execute_function()
					self.state = ButtonStates.Highlighted
				if event.type == KEYUP and event.key == K_RETURN:
					self.execute_function()
					self.state = ButtonStates.Highlighted
				if event.type == MOUSEBUTTONDOWN and not self.rect.collidepoint(mousePos):
					self.state = ButtonStates.Default
			if not self.rect.collidepoint(mousePos) and not pygame.key.get_pressed()[K_RETURN]:
				self.state = ButtonStates.Highlighted
					
		elif self.state == ButtonStates.Highlighted:
			self.change_to_color_scheme(ButtonStates.Highlighted)
			for event in events:
				if event.type == MOUSEBUTTONDOWN:
					if self.rect.collidepoint(mousePos):
						self.state = ButtonStates.Pressed
					else:
						self.state = ButtonStates.Default
				if event.type == KEYDOWN and event.key == K_RETURN:
					self.state = ButtonStates.Pressed
	
	def draw(self, surface):
		self.surface.fill(self.currentColor)
		borderRect = pygame.Rect(-self.borderWidth / 2, -self.borderWidth / 2, self.width + self.borderWidth, self.height + self.borderWidth)
		
		if self.bordered:
			pygame.draw.rect(self.surface, self.currentBorderColor, borderRect, self.borderWidth * 2)
		
		surface.blit(self.surface, self.rect)
	
	def execute_function(self):
		if self.function:
			self.function(self)
			
	def change_to_color_scheme(self, ButtonState):
		if ButtonState == ButtonStates.Default:
			self.currentColor = self.defaultColor
			self.currentBorderColor = self.defaultBorderColor
		elif ButtonState == ButtonStates.Pressed:
			self.currentColor = self.pressedColor
			self.currentBorderColor = self.pressedBorderColor
		elif ButtonState == ButtonStates.Highlighted:
			self.currentColor = self.highlightedColor
			self.currentBorderColor = self.highlightedBorderColor
		