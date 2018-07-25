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
		y = 7
		v = 1
		while self.gaming and y >= 0:

			sense.set_pixel((x-v)%8,y, (0,0,0) )
			sense.set_pixel(x,y, (0,0,255) )
			time.sleep(.1)
			sense.set_pixel(x,y, (0,0,255) )

			for event in pygame.event.get():
				if event.type == KEYDOWN:
					sense.set_pixel(x,y, (0,0,255) )
					y -= 1
			
			x = (x+v)%8
			
			if (x == 0) or (x == 7):
				v *= -1

if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
time.sleep(1)
sense.clear()
