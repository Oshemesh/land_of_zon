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
background = pygame.image.load( os.getcwd() + r"\\images\\Battleground4.png")
font_name = pygame.font.match_font("Pokemon GB.ttf", 32)

def draw_text(text, size, color, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(midtop =(x, y))
    screen.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    idleCounter = 0
    currentlyFacingRight = True
    goingUp = True
    highestPoint = False
    isJumping = False
    isAnimating = False # IDLE DOES NOT COUNT
    animationCounter = 0
    facingRight = False
    speed = 0
    max_health = 0
    current_health = 0
    attack = 0
    defense = 0
    attack_speed = 0
    
    current_image = pygame.Surface((500, 40))
        
    
    run_array_right = []
    run_array_left = [] 
    
    jump_array_right = []
    jump_array_left = []
    
    idle_array = []
 
    def __init__(self , speed, max_h , attack, defense, attack_s, idle_img_array, run_img_array, jump_img_array, starting_img, facingRight):
        self.facingRight = facingRight
        pygame.sprite.Sprite.__init__(self)
        self.max_health = max_h
        self.current_health = max_h
        self.attack = attack
        self.defense = defense
        self.attack_speed = attack_s
        self.current_image = starting_img
        self.image = starting_img
        
        self.jump_array = jump_img_array
        self.idle_array = idle_img_array
        
        #Load left and right running animation imgs
        if (facingRight):
            self.run_array_right = run_img_array
            self.jump_array_right = jump_img_array
            
            for img in run_img_array:
                self.run_array_left.append( pygame.transform.flip( img , True, False) )
            for img in jump_img_array:
                self.jump_array_left.append( pygame.transform.flip( img , True, False) )
                      
        else:
            self.run_array_left = run_img_array
            self.jump_array_left = jump_img_array
            for img in run_img_array:
                self.run_array_right.append( pygame.transform.flip( img , True, False) )       
            for img in jump_img_array:
                self.jump_array_right.append( pygame.transform.flip( img , True, False) ) 
                
        self.rect = self.image.get_rect()
        self.radius = 19
        self.speed = speed
        self.rect.center = (50, 300)
    # THIS GETS CALLED EVERY TIME all_sprites.update() happens
    def update(self):
        idleState = True   
        self.vx = 0
        keystate = pygame.key.get_pressed()
        #Moving to the right
        
        if(self.isJumping):
            jump_imgs = []
            if(self.currentlyFacingRight):
                jump_imgs = self.jump_array_right
            else:
                jump_imgs = self.jump_array_left
            
            self.isAnimating = True
            self.animationCounter += 1
            if self.animationCounter < 5:
                self.image = jump_imgs[0]

            elif self.animationCounter < 10:
                self.image = jump_imgs[1]
              
            elif self.animationCounter < 15:
                self.image = jump_imgs[2]
         
            elif self.animationCounter < 20:
                self.image = jump_imgs[3]
                self.highestPoint = True
                         
            elif self.animationCounter < 25:
                self.highestPoint = False
                self.goingUp = False
                self.image = jump_imgs[4]
            elif self.animationCounter < 30:
                self.image = jump_imgs[5]
            elif self.animationCounter < 35:
                self.image = jump_imgs[6]
            elif self.animationCounter < 40:
                self.isJumping = False
                self.animationCounter = 0;  
                self.goingUp = True
        
        
        if keystate[pygame.K_UP]: 
            idleState = False
            if(self.isJumping == False):
                self.animationCounter = 0
            self.isJumping = True
        if keystate[pygame.K_RIGHT]:
            idleState = False
            self.currentlyFacingRight = True
            self.vx += self.speed
            if(not self.isJumping):
                self.isAnimating = True
                self.animationCounter += 1
                if self.animationCounter < 5:
                    self.image = self.run_array_right[0]
                elif self.animationCounter < 10:
                    self.image = self.run_array_right[1]
                elif self.animationCounter < 15:
                    self.image = self.run_array_right[2]
                elif self.animationCounter < 20:
                    self.image = self.run_array_right[3]
                elif self.animationCounter < 25:
                    self.image = self.run_array_right[4]
                elif self.animationCounter < 30:
                    self.image = self.run_array_right[5]
                elif self.animationCounter < 35:
                    self.image = self.run_array_right[6]
                elif self.animationCounter < 40:
                    self.image = self.run_array_right[7]                
                elif self.animationCounter < 45:
                    self.image = self.current_image 
                    self.animationCounter = 0;
                
        elif keystate[pygame.K_LEFT]:
            idleState = False
            self.currentlyFacingRight = False
            self.vx -= self.speed
            if(not self.isJumping):
                self.isAnimating = True
                self.animationCounter += 1
                if self.animationCounter < 5:
                    self.image = self.run_array_left[0]
                elif self.animationCounter < 10:
                    self.image = self.run_array_left[1]
                elif self.animationCounter < 15:
                    self.image = self.run_array_left[2]
                elif self.animationCounter < 20:
                    self.image = self.run_array_left[3]
                elif self.animationCounter < 25:
                    self.image = self.run_array_left[4]
                elif self.animationCounter < 30:
                    self.image = self.run_array_left[5]
                elif self.animationCounter < 35:
                    self.image = self.run_array_left[6]
                elif self.animationCounter < 40:
                    self.image = self.run_array_left[7]                
                elif self.animationCounter < 45:
                    self.animationCounter = 0;
   
        
               
        
        self.rect.x += self.vx 
        if(self.isJumping):
            if not self.highestPoint:
                if(self.goingUp):
                    self.rect.y -= self.speed
                else:
                    self.rect.y += self.speed
       

        if(not self.isJumping):
            if(self.rect.y < 420 ):
                self.rect.y += 4
        
        if(self.rect.y >= 420):
            self.rect.y = 420
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
all_sprites = pygame.sprite.Group()


rogue_run_animation = [ pygame.image.load(os.getcwd() + r"\images\Rogue\Run\run1.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Run\run2.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Run\run3.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Run\run4.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Run\run5.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Run\run6.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Run\run7.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Run\run8.png").convert_alpha() ]
                          
rogue_jump_animation = [ pygame.image.load(os.getcwd() + r"\images\Rogue\Jump\jump1.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Jump\jump2.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Jump\jump3.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Jump\jump4.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Jump\jump5.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Jump\jump6.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Jump\jump7.png").convert_alpha() ]
 
rogue_idle_animation = [  pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle1.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle2.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle3.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle4.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle5.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle6.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle7.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle8.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle9.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle10.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle11.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle12.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle13.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle14.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle15.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle16.png").convert_alpha() , \
                          pygame.image.load(os.getcwd() + r"\images\Rogue\Idle\idle17.png").convert_alpha()]
                          
for img in rogue_run_animation:
    img = pygame.transform.scale(img, (200, 130))
for img in rogue_jump_animation:
    img = pygame.transform.scale(img, (200, 130))
for img in rogue_idle_animation:
    img = pygame.transform.scale(img, (200, 130))    

#speed, max_h , attack, defense, attack_s):
rogue = Player(LOW + 2, 50, MEDIUM, LOW, HIGH , rogue_idle_animation , rogue_run_animation , rogue_jump_animation , rogue_run_animation[0] , True )
#mage = Player(MEDIUM, 100, HIGH, LOW, MEDIUM , mage_left_path, mage_right_path)
#viking = Player(LOW, 150, HIGH, HIGH, LOW , viking_left_path, viking_right_path)

selectPlayer = [rogue]#, mage, viking]

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


#if(idleState):
 #           self.idleCounter += 1
  #          if(not self.isJumping and len(self.idle_array) >= 17 ): 
   #             if self.idleCounter < 5:
   #                 self.image = self.idle_array[0]
   #             if self.idleCounter < 10:
   #                 self.image = self.idle_array[1]
   #             if self.idleCounter < 15:
   #                 self.image = self.idle_array[2]
   ##             if self.idleCounter < 20:
   #                 self.image = self.idle_array[3]
   #             if self.idleCounter < 25:
   #                 self.image = self.idle_array[4]
   #             if self.idleCounter < 30:
   #                 self.image = self.idle_array[5]
   #             if self.idleCounter < 35:
   #                 self.image = self.idle_array[6]
   #             if self.idleCounter < 40:
   #                 self.image = self.idle_array[7]
   #             if self.idleCounter < 45:
   #                 self.image = self.idle_array[8]
   #             if self.idleCounter < 50:
   #                 self.image = self.idle_array[9]
   ##             if self.idleCounter < 55:
    #                self.image = self.idle_array[10]
    #            if self.idleCounter < 60:
    #                self.image = self.idle_array[11]
    #            if self.idleCounter < 65:
    #                self.image = self.idle_array[12]
    #            if self.idleCounter < 70:
    #                self.image = self.idle_array[13]
    #            if self.idleCounter < 75:
    #                self.image = self.idle_array[14]
    #            if self.idleCounter < 80:
    #                self.image = self.idle_array[15]
    #            if self.idleCounter < 85:
    #                self.image = self.idle_array[16]                    
    #            self.idleCounter = 0
