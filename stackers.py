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

		cont = True
		
		blocks = [None]*8
		while self.gaming and y >= 0 and cont == True:
			
			sense.set_pixel((x-v)%8,y, (0,0,0) )
			sense.set_pixel(x,y, (0,0,255) )
			time.sleep(.1)
			sense.set_pixel(x,y, (0,0,0) )

			for event in pygame.event.get():
				if event.type == KEYDOWN:
					blocks[y] = x
					if y >= 7:
						sense.set_pixel(x,y, (0,0,255) )
						y -= 1
					else:
						if not blocks[y] == blocks[y+1]:
							v = 0
							cont = False
						else:
							sense.set_pixel(x,y, (0,0,255) )
							y -= 1
			
			x = (x+v)%8
			
			if (x == 0) or (x == 7):
				v *= -1
		if cont == False:
			for i in range(5):
				sense.set_pixel(x,y, (0,0,255) )
				time.sleep(.25)
				sense.set_pixel(x,y, (0,0,0) )
				time.sleep(.25)
		else:
			for i in range(5):
				for j in range(len(blocks)):
					sense.set_pixel(blocks[j],j, (0,0,255) )
				time.sleep(.25)
				sense.clear()
				time.sleep(.25)

if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
sense.clear()
