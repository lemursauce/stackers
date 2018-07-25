from sense_hat import SenseHat
from pygame.locals import *
import pygame
import random

sense = SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640,480))
		self.gaming = True
	
	def startGame(self):
		pygame.time.set_timer(USEREVENT +1, 800)
		while self.gaming:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					r = random.randint(0,255)
					g = random.randint(0,255)
					b = random.randint(0,255)
					x = random.randint(0,7)
					y = random.randint(0,7)
					sense.set_pixel(x,y, (r,g,b) )
				elif event.type == KEYUP:
					sense.clear()

if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
