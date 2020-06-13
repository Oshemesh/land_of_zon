import pygame
import random
import os

HIGH  = 8
MEDIUM = 5
LOW = 3


WIDTH = 1000
HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#load graphics
background = pygame.image.load( os.getcwd() + r"\\Battleground4.png")
font_name = pygame.font.match_font("Pokemon GB.ttf", 32)

def draw_text(text, size, color, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(midtop =(x, y))
    screen.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    speed = 0
    max_health = 0
    current_health = 0
    attack = 0
    defense = 0
    attack_speed = 0
    
    char_img_l = pygame.Surface((500, 40))
    char_img_r = pygame.Surface((500, 40))
        
    
    walk_array_right = []
    
    def __init__(self , speed, max_h , attack, defense, attack_s, char_img_l, char_img_r):
        pygame.sprite.Sprite.__init__(self)
        self.max_health = max_h
        self.current_health = max_h
        self.attack = attack
        self.defense = defense
        self.attack_speed = attack_s
        self.image = pygame.Surface((500, 40))
        x = pygame.image.load(char_img_r)
        x = pygame.transform.scale(x, (200, 130))
        self.image = x
        self.char_img_r = x;
        
        y = pygame.image.load(char_img_l)
        y = pygame.transform.scale(y, (200, 130))
        self.char_img_l = y
        #self.image.fill((55, 121, 179))
        self.rect = self.image.get_rect()
        self.radius = 19
        self.speed = speed
        #pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)
        self.rect.center = (50, 300)
    def update(self):
        self.vx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.vx += self.speed
            self.image = self.char_img_r;
        if keystate[pygame.K_LEFT]:
            self.vx -= self.speed
            self.image = self.char_img_l
        if keystate[pygame.K_UP]:
            if( self.rect.y >= 420):
                if(self.rect.y >= 20):
                    self.rect.y -= self.speed*15
        self.rect.x += self.vx 
        
        if(self.rect.y < 420 ):
            self.rect.y += 4
        
        if(self.rect.y >= 420):
            self.rect.y = 420
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
all_sprites = pygame.sprite.Group()

rogue_left_path = os.getcwd() + r"\rogue_left.png"
rogue_right_path = os.getcwd() + r"\rogue_right.png"

mage_left_path = os.getcwd() + r"\mage_left.png"
mage_right_path = os.getcwd() + r"\mage_right.png"

viking_left_path = os.getcwd() + r"\viking_left.png"
viking_right_path = os.getcwd() + r"\viking_right.png"

#speed, max_h , attack, defense, attack_s):
rogue = Player(HIGH, 50, MEDIUM, LOW, HIGH , rogue_left_path, rogue_right_path )
mage = Player(MEDIUM, 100, HIGH, LOW, MEDIUM , mage_left_path, mage_right_path)
viking = Player(LOW, 150, HIGH, HIGH, LOW , viking_left_path, viking_right_path)

selectPlayer = [rogue, mage, viking]

characterChosen = int(input("Choose your character! : (0-rogue, 1-mage, 2-viking)"))

all_sprites.add(selectPlayer[characterChosen])

running = True
score = 0

# Game Loop
while running:
    clock.tick(FPS)
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()
    # Draw
    #screen.fill( (40, 40, 40) )
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    draw_text("HEALTH: " + str(selectPlayer[characterChosen].current_health) + "/" + str(selectPlayer[characterChosen].max_health) , 20,  (255, 0, 0) , 60 , 10 )
    pygame.display.flip() # do this last
pygame.quit()
