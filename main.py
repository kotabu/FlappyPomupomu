import pygame
from pygame.locals import *
import random
import os
import sys
from wall import Wall

def gameover_text(text,screen):
	screen.blit(text,(50,130))
	return 1

def main():
	pygame.init()
	screen = pygame.display.set_mode((300,300))
	pygame.display.set_caption("Flappy Pomupomu")

	clock = pygame.time.Clock()

	c_0 = (242,242,242)
	
	pomupomu = [
	 pygame.image.load(os.path.join('images','punipuni_001.png')),
	 pygame.image.load(os.path.join('images','punipuni_002.png')),
	 pygame.image.load(os.path.join('images','punipuni_003.png')),
	 pygame.image.load(os.path.join('images','punipuni_004.png'))
	]

	font = pygame.font.Font(os.path.join('fonts','Comfortaa[wght].ttf'),30)
	gameover = font.render("GAME OVER",True,(33,33,33))

	pygame.mixer.music.load(os.path.join('music','bgm.ogg'))
	pygame.mixer.music.set_volume(0.2)
	pygame.mixer.music.play(-1)

	pomu_view = 0
	count_x = 0
	count_y = 0
	pomu_x = 130
	pomu_y = 130
	wall_x = 300
	wall_y = 0
	up_mode = 0
	offset = 0
	r = 0
	stop = 0
	point = 0
	se = 0
	
	SPEED = 5

	while(1):
		clock.tick(30)
		count_x += 1
		count_y += 1

		screen.fill(c_0)	

		if stop == 0:
			if up_mode == 0:
				if pomu_y > 262 or pomu_y < 0:
					stop = gameover_text(gameover,screen)
				elif pomu_y < 301:
					pomu_y += offset
					offset += 0.2
			elif up_mode == 1:
				if pomu_y < 0:
					stop = gameover_text(gameover,screen)
				pomu_y -= SPEED - offset
				offset += 0.2
				if SPEED - offset < 0:
					up_mode = 0
					offset = 0
		
		
		screen.blit(pomupomu[pomu_view],(pomu_x,pomu_y))
		if count_x == 5:
			if pomu_view < 3:
				pomu_view += 1
			elif pomu_view > 2:
				pomu_view = 0
			count_x = 0

		if stop == 0:
			wall_x -= 2

		wall = Wall()
		danger_zone = wall.set_wall(r,wall_x,screen)
		
		if wall_x < -40:
			wall_x = 300
			r = random.randint(0,3)

		if wall_x > 100 and wall_x < 160:
			if pomu_y < danger_zone[0]:
				stop = gameover_text(gameover,screen)
			elif pomu_y > danger_zone[1]:
				stop = gameover_text(gameover,screen)
		if stop == 1:
			stop = gameover_text(gameover,screen)
			if se == 0:
				pygame.mixer.music.load(os.path.join('music','SE.ogg'))
				pygame.mixer.music.set_volume(0.2)
				pygame.mixer.music.play()
				se = 1

		if wall_x == 94:
			point += 1
		point_text = font.render(str(point),True,(33,33,33))
		screen.blit(point_text,(10,10))

		pygame.display.update()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					offset = 0
					up_mode = 1
				if event.key == K_r:
					pygame.quit()
					main()
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

if __name__ == "__main__":
	main()

