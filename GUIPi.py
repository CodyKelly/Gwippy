################################################################################
#                      GUIPi: A GUI Framework for Pygame                       #
#                           Developed by Cody Kelly                            #
#                     Use with Python 2.7 and Pygame 1.9.1                     #
################################################################################

import pygame

class GUIManager(object):
	def __init__(self):
		self.elements = []
		
	def update(self):
		for element in elements:
			if element.isActive:
				element.update()
	
	def draw(self, surface):
		for element in elements:
			if element.isActive:
				element.draw
				
	def add_element(self, element):
		self.elements.append(element)
		element.GUIManager = self
		
class Element(object):
	def __init__(self, x=0, y=0)
		self.x = x
		self.y = y
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
	def __init__(self, x=0, y=0, width=10, height=10, text="", defaultGraphic=None, onPressGraphic=None, function=None):
		super(Button, self).__init__(x, y)
		self.width = width
		self.height = height
		self.text = text
		self.defaultGraphic = defaultGraphic
		self.onPressGraphic = onPressGraphic
		self.function = function
		