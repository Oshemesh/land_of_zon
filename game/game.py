import pygame
import os

pygame.init()
#Setting Display & Game Constants
window = pygame.display.set_mode((928, 793))
background = pygame.image.load("Background.png")
myfont = pygame.font.SysFont('Comic Sans MS', 30)
max_health = 100

#data structure for throwing stars
class Star(object):
    objID = "star"
    facingRight = True   
    def __init__(self,x,y,image , facingRight):
        self.x = x
        self.y = y
        img = pygame.image.load(image).convert_alpha()
        self.image = img
        self.facingRight = facingRight

    #Method to draw object
    def draw(self):
        window.blit(self.image,(self.x,self.y))

    #Method to move object (special input of speedx and speedy)
    def move(self,speedx,speedy):
        self.x += speedx
        self.y += speedy
#data structure for hero ( player)
class Player(object):
    health = max_health
    objID = "hero"
    #We start facing right
    facingRight = True
    gold = 0;
    #Array of imgs for animations
    run_Animation = [ pygame.image.load(os.getcwd() + r"\Ninja\run_0.png").convert_alpha() , \
                      pygame.image.load(os.getcwd() + r"\Ninja\run_1.png").convert_alpha() , \
                      pygame.image.load(os.getcwd() + r"\Ninja\run_2.png").convert_alpha() , \
                      pygame.image.load(os.getcwd() + r"\Ninja\run_3.png").convert_alpha() , \
                      pygame.image.load(os.getcwd() + r"\Ninja\run_4.png").convert_alpha() , \
                      pygame.image.load(os.getcwd() + r"\Ninja\run_5.png").convert_alpha()  ]
                      
    idle_Animation = [ pygame.image.load(os.getcwd() + r"\Ninja\idle_0.png").convert_alpha() , \
                       pygame.image.load(os.getcwd() + r"\Ninja\idle_1.png").convert_alpha() , \
                       pygame.image.load(os.getcwd() + r"\Ninja\idle_2.png").convert_alpha() , \
                       pygame.image.load(os.getcwd() + r"\Ninja\idle_3.png").convert_alpha() ]
                       
    attack_Animation = [ pygame.image.load(os.getcwd() + r"\Ninja\attack_0.png").convert_alpha() , \
                         pygame.image.load(os.getcwd() + r"\Ninja\attack_1.png").convert_alpha() , \
                         pygame.image.load(os.getcwd() + r"\Ninja\attack_2.png").convert_alpha() , ]


    jump_Animation = [ pygame.image.load(os.getcwd() + r"\Ninja\jump_0.png").convert_alpha() , \
                       pygame.image.load(os.getcwd() + r"\Ninja\jump_1.png").convert_alpha() , \
                       pygame.image.load(os.getcwd() + r"\Ninja\jump_2.png").convert_alpha() , ]

    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        img = pygame.image.load(image).convert_alpha()
        self.image = img

    #Method to draw object
    def draw(self):
        window.blit(self.image,(self.x,self.y))

    #Method to move object (special input of speedx and speedy)
    def move(self,speedx,speedy):
        self.x += speedx
        self.y += speedy

#data structure for monsters
class Monster(object):
    health = 25
    attack = 7
    objID = "monster"
    facingRight = True   

    def __init__(self,x,y,image , facingRight):
        self.x = x
        self.y = y
        img = pygame.image.load(image).convert_alpha()
        self.image = img
        self.facingRight = facingRight

    def draw(self):
        window.blit(self.image,(self.x,self.y))       
    
#create hero & 1 monster
hero = Player(500, 610, os.getcwd() + r"\Ninja\idle_0.png")
monsterA = Monster(750, 690, os.getcwd() + r"\monster\BasiliskRed.png" , False)

#These constants should be put in player data structre..
heroIsAttacking = False
throwStar = False
heroIsAttacking = False
throwStar = False
shootingStarCoolDown = 0
isJumping = False

#list on characters on map
char_list = [hero, monsterA]
##
spawnNewMonster = []
quit_signal = False
#ticker for game loop. 
i = 0

while not quit_signal:
        #Ticker dependent on computer speed, should use fps instead of i
        i += 1
        #add delay between throwing stars
        if(shootingStarCoolDown >= 1):
            shootingStarCoolDown += 1
        if(shootingStarCoolDown == 50):
            shootingStarCoolDown = 0
        pygame.display.update()
        heroIsMoving = False
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                 quit_signal = True
          
        # HANDLING KEYBOARD INPUT 
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            hero.facingRight  = False
            hero.x -= 1
            heroIsMoving = True
        if keys[pygame.K_RIGHT]:
            hero.facingRight  = True
            hero.x += 1
            heroIsMoving = True
        if keys[pygame.K_SPACE] and not heroIsAttacking:
            i = 0
            heroIsAttacking = True
        if keys[pygame.K_RETURN] and not heroIsAttacking:
            throwStar = True
        if keys[pygame.K_UP] and not isJumping :
            i = 0
            isJumping = True
        
        # HANDLING ANIMATIONS
        #JUMP LOGIC #
        if(isJumping):
            if i < 30:
                hero.y -= 2
                if(hero.facingRight):                   
                    hero.image = hero.jump_Animation[0]
                else:
                    hero.image = pygame.transform.flip(hero.jump_Animation[0] , True, False)
            elif i < 60:
                hero.y += 2
                if(hero.facingRight):
                    hero.image = hero.jump_Animation[1]
                else:
                    hero.image = pygame.transform.flip(hero.jump_Animation[1] , True, False)
            elif i < 65:
                if(hero.facingRight):
                    hero.image = hero.jump_Animation[2]
            elif i < 20:
                    hero.image = pygame.transform.flip(hero.jump_Animation[2] , True, False)
            else:
                i = 0
                isJumping = False
                hero.y = 610
        #RUN LOGIC #    
        elif(heroIsMoving):
            if i < 5:
                if(hero.facingRight):
                    hero.image = hero.run_Animation[0]
                else:
                    hero.image = pygame.transform.flip(hero.run_Animation[0] , True, False)
            elif i < 10:
                if(hero.facingRight):
                    hero.image = hero.run_Animation[1]
                else:
                    hero.image = pygame.transform.flip(hero.run_Animation[1] , True, False)
            elif i < 15:
                if(hero.facingRight):
                    hero.image = hero.run_Animation[2]
                else:
                    hero.image = pygame.transform.flip(hero.run_Animation[2] , True, False)
            elif i < 20:
                if(hero.facingRight):
                    hero.image = hero.run_Animation[3]
                else:
                    hero.image = pygame.transform.flip(hero.run_Animation[3] , True, False)
            elif i < 25:
                if(hero.facingRight):
                    hero.image = hero.run_Animation[4]
                else:
                    hero.image = pygame.transform.flip(hero.run_Animation[4] , True, False)
            elif i < 30:
                if(hero.facingRight):
                    hero.image = hero.run_Animation[5]
                else:
                    hero.image = pygame.transform.flip(hero.run_Animation[5] , True, False)
            else:
                i = 0        
        
         #ATTACK LOGIC # 
        elif(heroIsAttacking):
            if i < 7:
                if(hero.facingRight):
                    hero.image = hero.attack_Animation[0]
                else:
                    hero.image = pygame.transform.flip(hero.attack_Animation[0] , True, False)
            elif i < 14:
                if(hero.facingRight):
                    hero.image = hero.attack_Animation[1]
                else:
                    hero.image = pygame.transform.flip(hero.attack_Animation[1] , True, False)
            elif i < 21:
                if(hero.facingRight):
                    hero.image = hero.attack_Animation[2]
                else:
                    hero.image = pygame.transform.flip(hero.attack_Animation[2] , True, False)
            else:
                i = 0   
                heroIsAttacking = False
            
         #IDLE LOGIC # 
        else:
            if i < 10:
                if(hero.facingRight):
                    hero.image = hero.idle_Animation[0]
                else:
                    hero.image = pygame.transform.flip(hero.idle_Animation[0] , True, False)
            elif i < 20:
                if(hero.facingRight):
                    hero.image = hero.idle_Animation[1]
                else:
                    hero.image = pygame.transform.flip(hero.idle_Animation[1] , True, False)
            elif i < 30:
                if(hero.facingRight):
                    hero.image = hero.idle_Animation[2]
                else:
                    hero.image = pygame.transform.flip(hero.idle_Animation[2] , True, False)
            elif i < 40:
                if(hero.facingRight):
                    hero.image = hero.idle_Animation[3]
                else:
                    hero.image = pygame.transform.flip(hero.idle_Animation[3], True, False)
            else:
                i = 0
        
        # refresh background
        window.fill((0,0,0))
        window.blit(background, (0, 0))
     
        # put star in screen if user clicks return ( enter ) key
        if(throwStar and shootingStarCoolDown == 0):
            shootingStarCoolDown = 1
            char_list.append(Star( hero.x + 60, hero.y + 60, os.getcwd() + r"/stars/ThrowingStar.png", hero.facingRight))
            throwStar = False;
        
        # list of objects to delete ( they have health <= 0  or offscreen thowing star )
        toDelete = []       
        
        for c in char_list:
            # This makes monsters chase the hero
            if c.objID == "monster" : 
                if c.x - hero.x > 0 :
                    c.x -= 1
                else:
                    c.x += 1           
            
            #when hero attacks a monster
            if c.objID == "monster" and heroIsAttacking and (c.x - hero.x)  < 143 and i > 14 :
                c.x += 50
                c.health -= 10
                if(c.health < 0 ):
                    toDelete.append(c)
            # Delete objects off the map
            if(c.x < 0 or c.x > 900):
                toDelete.append(c)
                
            # logic for when monsters touch the hero
            if c.objID == "monster" and (c.x - hero.x)  < 100 :
                hero.health -= c.attack
                if hero.x - c.x  < 0 :
                    hero.x -= 70
                else:
                    hero.x += 70
            else:
                # logic for throwing star to move across map
                if(c.objID == "star"):                 
                    if(c.facingRight):
                        c.x += 5                       
                    else:
                        c.x -= 5
                c.draw() 
        #delete objects in toDelete Array , Dont Delete Hero!!! add gold equal to monser attack
        for item in toDelete:
            if(item.objID != "hero"):
                char_list.remove(item)
                if item.objID == "monster":
                    hero.gold += item.attack
       
       #relevant text on top left
        gold = myfont.render('Gold: ' + str(hero.gold), False, (0, 0, 0))
        health = myfont.render('Health: ' + str(hero.health) + r"/" + str(max_health) , False, (0, 0, 0))
        window.blit(gold,(20,20))
        window.blit(health,(20,50))
        
        #load page
        pygame.display.flip()
         