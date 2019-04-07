import pygame
from pygame.locals import *
import os

class Wall():

	def __init__(self):		 
		self.wall = [
		 pygame.image.load(os.path.join('images','wall_001.png')),
		 pygame.image.load(os.path.join('images','wall_002.png')),
		 pygame.transform.flip(pygame.image.load(os.path.join('images','wall_001.png')),False,True) 
		]
	
	def set_wall(self,r,wall_x,screen):

		if r == 0:
			screen.blit(self.wall[1],(wall_x,0))
			screen.blit(self.wall[1],(wall_x,40))
			screen.blit(self.wall[0],(wall_x,80))
			
			screen.blit(self.wall[2],(wall_x,220))
			screen.blit(self.wall[1],(wall_x,260))
			screen.blit(self.wall[1],(wall_x,300))
		
			return [115,186]
		if r == 1:
			screen.blit(self.wall[1],(wall_x,0))
			screen.blit(self.wall[1],(wall_x,40))
			screen.blit(self.wall[1],(wall_x,80))
			screen.blit(self.wall[0],(wall_x,120))
			
			screen.blit(self.wall[2],(wall_x,260))
			screen.blit(self.wall[1],(wall_x,300))
		
			return [155,226]
		if r == 2:
			screen.blit(self.wall[1],(wall_x,0))
			screen.blit(self.wall[0],(wall_x,40))
			
			screen.blit(self.wall[2],(wall_x,180))
			screen.blit(self.wall[1],(wall_x,220))
			screen.blit(self.wall[1],(wall_x,260))
			screen.blit(self.wall[1],(wall_x,300))
		
			return [75,146]
		if r == 3:
			screen.blit(self.wall[0],(wall_x,0))
			
			screen.blit(self.wall[2],(wall_x,140))
			screen.blit(self.wall[1],(wall_x,180))
			screen.blit(self.wall[1],(wall_x,220))
			screen.blit(self.wall[1],(wall_x,260))
			screen.blit(self.wall[1],(wall_x,300))
		
			return [35,106]
