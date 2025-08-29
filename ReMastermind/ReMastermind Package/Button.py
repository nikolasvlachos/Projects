# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import pygame
class Button ():
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	def __init__ (self, x, y, picture, scale):
		height = picture.get_height ()
		width = picture.get_width ()
		self.picture = pygame.transform.scale \
			(picture, (int (width * scale), int (height * scale)))
		self.rectangle = self.picture.get_rect ()
		self.rectangle.topleft = (x, y)
		self.clicked = False
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	def draw (self, surface):
		action = False
		# Gets mouse position
		pos = pygame.mouse.get_pos()

		# Checks mouseover and clicked conditions
		if (self.rectangle.collidepoint (pos)):
			if ((pygame.mouse.get_pressed() [0] == 1) and
					(self.clicked == False)):
				self.clicked = True
				action = True

		if (pygame.mouse.get_pressed () [0] == 0):
			self.clicked = False

		# Draws button on screen
		surface.blit (self.picture, (self.rectangle.x, self.rectangle.y))

		return action
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
