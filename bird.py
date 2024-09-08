import pygame
import random 
import sys 
from random import randint 
pygame.init()
WIDTH = 1000
HIGHT = 600
screen = pygame.display.set_mode((WIDTH , HIGHT))
pygame.display.set_caption('Flappy Bird')
running = True
BLACK = (0, 0, 0)
BLUE = ( 0 , 0 , 255 )
RED = (255 , 0 , 0 )
WHITE  = (255 , 255 , 255)
GREEN = ( 0 , 255 , 0 )
clock = pygame.time.Clock()
# cấu trúc chim
bird_y = 300 
BIRD_WIDTH = 50 
BIRD_HIGHT = 50 
BIRD_VALOCITY = 15 
# cấu trúc quả
fruit_x1 = 400 
fruit_x2 = 600
fruit_x3 = 800
fruit_x4 = 1000
fruit_x5 = 1200
fruit_y1 = randint(150 , 500) 
fruit_y2 = randint(150 , 500)
fruit_y3 = randint(150 , 500)
fruit_y4 = randint(150 , 500)
fruit_y5 = randint(150 , 500)
FRUIT_HIGHT1 = 30
FRUIT_HIGHT2 = 30
FRUIT_HIGHT3 = 30
FRUIT_HIGHT4 = 30
FRUIT_HIGHT5 = 30
FRUIT_WIDTH1 =30
FRUIT_WIDTH2 =30
FRUIT_WIDTH3 =30
FRUIT_WIDTH4 =30
FRUIT_WIDTH5 =30
# cấu trúc quả đặc biệt 
FRUIT_HIGHT_SPECIAL = 40 
FRUIT_WIDTH_SPECIAL = 40 
fruit_y_special = randint(150 , 500)
fruit_x_special = 1100 

# vận tốc 
FRUIT_VELOCITY = 3 
# Score and font 
score = 0 
font = pygame.font.SysFont('sans' , 20 )
check_score1 = False  
check_score2 = False  
check_score3 = False  
check_score4 = False  
check_score5 = False  
#check spacial 
check_speciial1 = False 
check_speciial2 = False  
check_speciial3 = False 
check_speciial4 = False 
check_speciial5 = False 
# life 
life = 3 
# menu 
check_menu = True 
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.button_font = pygame.font.Font(None, 50)
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        self.buttons = [
            {"text": "Start", "rect": pygame.Rect(300, 200, 200, 50)},
            {"text": "Options", "rect": pygame.Rect(300, 300, 200, 50)},
            {"text": "Quit", "rect": pygame.Rect(300, 400, 200, 50)}
        ]

    def draw(self):
        self.screen.fill(BLACK)
        for button in self.buttons:
            pygame.draw.rect(self.screen, WHITE, button["rect"])
            text = self.button_font.render(button["text"], True, BLACK)
            self.screen.blit(text, (button["rect"].x + 20, button["rect"].y + 10))
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for button in self.buttons:
                if button["rect"].collidepoint(pos):
                    if button["text"] == "Quit":
                        pygame.quit()
                        sys.exit()
                    elif button["text"] == "Start":
                        check_menu = False 
                    elif button["text"] == "Options":
                        print("Options")
menu = Menu(screen)

while running:		
	clock.tick(60)
	screen.fill(BLACK)
	# vẽ quả 
	if check_menu == False :
		fruit1_rect=pygame.draw.rect(screen , BLUE , (fruit_x1 , fruit_y1 , FRUIT_WIDTH1 , FRUIT_HIGHT1  ))
		fruit2_rect=pygame.draw.rect(screen , BLUE , (fruit_x2 , fruit_y2 , FRUIT_WIDTH2 , FRUIT_HIGHT2  ))
		fruit3_rect=pygame.draw.rect(screen , BLUE , (fruit_x3 , fruit_y3 , FRUIT_WIDTH3 , FRUIT_HIGHT3  ))
		fruit4_rect=pygame.draw.rect(screen , BLUE , (fruit_x4 , fruit_y4 , FRUIT_WIDTH4 , FRUIT_HIGHT4  ))
		fruit5_rect=pygame.draw.rect(screen , BLUE , (fruit_x5 , fruit_y5 , FRUIT_WIDTH5 , FRUIT_HIGHT5  ))
		fruit_x1 = fruit_x1 - FRUIT_VELOCITY
		fruit_x2 = fruit_x2 - FRUIT_VELOCITY
		fruit_x3 = fruit_x3 - FRUIT_VELOCITY
		fruit_x4 = fruit_x4 - FRUIT_VELOCITY
		fruit_x5 = fruit_x5 - FRUIT_VELOCITY
		#fruit = [fruit1_rect ,fruit2_rect , fruit3_rect , fruit4_rect , fruit5_rect]
		#fruit_special = random.choice(fruit)
		#print(fruit_special)
		# vẽ chim 
		bird_rect = pygame.draw.rect(screen , RED , (0 , bird_y , BIRD_WIDTH , BIRD_HIGHT) )
		if bird_y > HIGHT - BIRD_HIGHT :
			bird_y =  HIGHT - BIRD_HIGHT
		if bird_y < 0 :
			bird_y = 0 
		# tạo quả mới
		if fruit_x1 < 0 :
			fruit_x1 = HIGHT + 400
			life -= 1 
		if fruit_x2 < 0 :
			fruit_x2 = HIGHT + 400
			life -= 1
		if fruit_x3 < 0 :
			fruit_x3 = HIGHT + 400
			life -= 1
		if fruit_x4 < 0 :
			fruit_x4 = HIGHT + 400
			life -= 1
		if fruit_x5 < 0 :
			fruit_x5 = HIGHT + 400
			life -= 1
		if bird_y > HIGHT - BIRD_HIGHT :
			bird_y = HIGHT - BIRD_HIGHT
		if bird_y < 0 :
			bird_y = 0 
		# check va chạm
		if 0 <= fruit_x1 <= 40 and ((  bird_y <= fruit_y1 + 30 <= bird_y + BIRD_HIGHT )  or (bird_y <= fruit_y1 <= bird_y + BIRD_HIGHT) ) and check_score1 == False: 
			score += 1 
			fruit_x1 = HIGHT + 400
			check_score1 = True
		if 0 <= fruit_x2 <= 40 and ((  bird_y <= fruit_y2 + 30 <= bird_y + BIRD_HIGHT )  or (bird_y <= fruit_y2 <= bird_y + BIRD_HIGHT) ) and check_score2 == False: 
			score += 1
			fruit_x2 = HIGHT + 400
			check_score2 = True 
		if 0 <= fruit_x3 <= 40 and ((  bird_y <= fruit_y3 + 30 <= bird_y + BIRD_HIGHT )  or (bird_y <= fruit_y3 <= bird_y + BIRD_HIGHT) ) and check_score3 == False : 
			score += 1
			fruit_x3 = HIGHT + 400
			check_score3 = True 
		if 0 <= fruit_x4 <= 40 and ((  bird_y <= fruit_y4 + 30 <= bird_y + BIRD_HIGHT ) or  (bird_y <= fruit_y4 <= bird_y + BIRD_HIGHT)) and check_score4 == False: 
			score += 1
			fruit_x4 = HIGHT + 400
			check_score4 = True
		if 0 <= fruit_x5 <= 40 and ((  bird_y <= fruit_y5 + 30 <= bird_y + BIRD_HIGHT ) or  (bird_y <= fruit_y5 <= bird_y + BIRD_HIGHT) )  and check_score5 == False: 
			score += 1
			fruit_x5 = HIGHT + 400
			check_score5 = True
		if fruit_x1 == HIGHT + 400: 
			fruit_y1 = randint(150 , 500)
			check_score1 = False
		if fruit_x2 == HIGHT + 400  :
			fruit_y2 = randint(150 , 500)
			check_score2 = False 
		if fruit_x3 == HIGHT + 400 :
			fruit_y3 = randint(150 , 500)
			check_score3 = False
		if fruit_x4== HIGHT + 400 :		
			fruit_y4 = randint(150 , 500)
			check_score4 = False
		if fruit_x5 == HIGHT + 400 :
			fruit_y5 = randint(150 , 500)
			check_score5 = False
		# dừng màn hình 
		if life == 0 :
			FRUIT_VELOCITY = 0
			BIRD_VALOCITY = 0 

	# in điểm 
	score_txt = font.render('Your Score : ' + str(score) , True  , WHITE  )
	screen.blit(score_txt , (5 , 5 ))
	life_txt = font.render('Your Life : ' + str(life ) , True , WHITE  )
	screen.blit(life_txt , (5 , 25 ))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN :
			if event.key == pygame.K_UP : 
				bird_y = bird_y - BIRD_VALOCITY
			if event.key == pygame.K_DOWN : 
				bird_y = bird_y + BIRD_VALOCITY
		menu.handle_event(event)		
	if check_menu== True : 
		menu.draw()	
	pygame.display.flip()

pygame.quit()