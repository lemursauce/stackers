from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
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
		x = 0
		while self.gaming:
			for i in range(0,8):
				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)

				sense.set_pixel((x+i-1)%8,i, (0,0,0))
				sense.set_pixel((x+i)%8,i, (r,g,b))
			time.sleep(.01)
			x = (x+1)%8

if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
