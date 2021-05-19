import pygame
import os
import random
from pygame import mixer

pygame.init()
pygame.font.init()
pygame.mixer.init()

FPS = 60
WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Eylul Sayilari Dogru Ogren")

#Loading images
ONE_IMG = pygame.image.load(os.path.join("assets", "1.png"))
TWO_IMG = pygame.image.load(os.path.join("assets", "2.png"))
THREE_IMG = pygame.image.load(os.path.join("assets", "3.png"))
FOUR_IMG = pygame.image.load(os.path.join("assets", "4.png"))
FIVE_IMG = pygame.image.load(os.path.join("assets", "5.png"))
SIX_IMG = pygame.image.load(os.path.join("assets", "6.png"))
SEVEN_IMG = pygame.image.load(os.path.join("assets", "7.png"))
EIGTH_IMG = pygame.image.load(os.path.join("assets", "8.png"))
NINE_IMG = pygame.image.load(os.path.join("assets", "9.png"))
YAZIK_KAFANA_IMG = pygame.image.load(os.path.join("assets", "yazik_kafana.jpg"))

#Rescaling Images
ONE_IMG = pygame.transform.scale(ONE_IMG, (100,100))
TWO_IMG = pygame.transform.scale(TWO_IMG, (100,100))
THREE_IMG = pygame.transform.scale(THREE_IMG, (100,100))
FOUR_IMG = pygame.transform.scale(FOUR_IMG, (100,100))
FIVE_IMG = pygame.transform.scale(FIVE_IMG, (100,100))
SIX_IMG = pygame.transform.scale(SIX_IMG, (100,100))
SEVEN_IMG = pygame.transform.scale(SEVEN_IMG, (100,100))
EIGTH_IMG = pygame.transform.scale(EIGTH_IMG, (100,100))
NINE_IMG = pygame.transform.scale(NINE_IMG, (100,100))
YAZIK_KAFANA_IMG = pygame.transform.scale(YAZIK_KAFANA_IMG, (900,900))

#Loading TTS messages.
ONE_MP3 = pygame.mixer.Sound(os.path.join("assets/tts", "tts_1.mp3"))
TWO_MP3 = pygame.mixer.Sound(os.path.join("assets/tts", "tts_2.mp3"))
THREE_MP3 = pygame.mixer.Sound(os.path.join("assets/tts", "tts_3.mp3"))
FOUR_MP3 = pygame.mixer.Sound(os.path.join("assets/tts", "tts_4.mp3"))
FIVE_MP3 = pygame.mixer.Sound(os.path.join("assets/tts", "tts_5.mp3"))
SIX_MP3 = pygame.mixer.Sound(os.path.join("assets/tts", "tts_6.mp3"))
SEVEN_MP3 = pygame.mixer.Sound(os.path.join("assets/tts", "tts_7.mp3"))
EIGHT_MP3 = pygame.mixer.Sound(os.path.join("assets/tts", "tts_8.mp3"))
NINE_MP3 = pygame.mixer.Sound(os.path.join("assets/tts", "tts_9.mp3"))

LOSE_MP3 = pygame.mixer.Sound(os.path.join("assets/tts", "tts_fail.mp3"))
FAIL_MP3 = pygame.mixer.Sound(os.path.join("assets/tts", "tts_lose.mp3"))



#Background
background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Number():
    def __init__(self,value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.image = self.getImage(value)
        self.rect = pygame.Rect(self.x,self.y,100,100)
        self.mp3 = self.getMP3(value)
        
    
    def getImage(self, value):
        images={
            1:ONE_IMG,
            2:TWO_IMG,
            3:THREE_IMG,
            4:FOUR_IMG,
            5:FIVE_IMG,
            6:SIX_IMG,
            7:SEVEN_IMG,
            8:EIGTH_IMG,
            9:NINE_IMG
        }
        return images.get(value)
    
    def getMP3(self, value):
        mp3List={
            1:ONE_MP3,
            2:TWO_MP3,
            3:THREE_MP3,
            4:FOUR_MP3,
            5:FIVE_MP3,
            6:SIX_MP3,
            7:SEVEN_MP3,
            8:EIGHT_MP3,
            9:NINE_MP3
        }
        return mp3List.get(value)






def main():
    lost = False
    run = True
    level = 0
    lives = 3
    lost_count = 0
    numbersList = []
    isTTSPlayed = False
    changeNumber = True
    number = None
    
    clock = pygame.time.Clock()
    

    #Velocity values for both player and enemy.
    

    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)
    
    #Function for redrawing window.
    def redraw_window():
        #Drawing background
        WIN.blit(background, (0,0))
        
        #Initializing level fonts.
        lives_text = main_font.render(f"Can: {lives}", 1, (255,255,255))
        level_text = main_font.render(f"Seviye: {level}", 1, (255,255,255))
        
        #Drawing text.
        WIN.blit(level_text, (10,10))
        WIN.blit(lives_text, (WIDTH - lives_text.get_width()- 10,10))

        
        for image in numbersList:
             WIN.blit(image.image, (image.x,image.y))

        pygame.display.update()
    
    def lost_game():
        lose = True
        WIN.blit(background, (0,0))
        while lose:
            WIN.blit(YAZIK_KAFANA_IMG, (350,0))
            pygame.display.update()
            for i in range(3):
                pygame.mixer.Sound.play(LOSE_MP3)
                while pygame.mixer.get_busy():
                    print("LMAO")
            quit()



    
    while run:
        clock.tick(FPS) 
        #Drawing lost text for 3 seconds then ending the loop.
    
        if len(numbersList) == 0:
            level += 1
            numbersAlreadyAdded = []
            while(len(numbersList) != 5):
                value = random.randint(1,9)
                #This loop avoids duplicate numbers.
                while value in numbersAlreadyAdded:
                    value = random.randint(1,9)
                temp = Number(value,  200*len(numbersList) + 300 , HEIGHT / 2 -150)
                numbersAlreadyAdded.append(value)
                numbersList.append(temp)
        
        #Picking number to click.
        if len(numbersList) != 0:
            if changeNumber:
                number = random.choice(numbersList)
                changeNumber = False

        redraw_window()

            
        #Playing TTS message.
        if not(isTTSPlayed):
            pygame.mixer.Sound.play(number.mp3)
            number_tts = 0
            isTTSPlayed = True
            while pygame.mixer.get_busy():
                print("TTS is being played")

        # TODO:FIX TTS
        #Checking if quit button pressed.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                print(x, y)
                click = pygame.Rect(x,y,1,1)
                if click.colliderect(number.rect):
                    numbersList.remove(number)
                    isTTSPlayed = False                    
                    changeNumber = True
                else:
                    pygame.mixer.Sound.play(FAIL_MP3)
                    while pygame.mixer.get_busy():
                        print("Playing FAIL_MP3")
                    changeNumber = False
                    isTTSPlayed = False
                    lives -= 1

        #Checking if we lost the game.
        if lives <= 0:
            run = False
            lost_game()             
                        
                   

                    

main()


    
    
