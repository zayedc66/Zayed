import pygame,sys
from invademap1 import bckgrnd1
from map import back2
from player import move
from physics import BouncePhysics
from shot import bullet
from EvilShips import BadShips
from evil import enemyshot
import random
pygame.init()
kerbx = 250
kerby = 550
x = 0
y = 0
# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
back_grounds = pygame.sprite.Group()
playable = pygame.sprite.Group()
walls = pygame.sprite.Group()
Bullets_player = pygame.sprite.Group()
invade_ships = pygame.sprite.Group()
shipEnds = pygame.sprite.Group()
Bullets_enemy = pygame.sprite.Group()
menuon = 0
gamestart = 1
startx =250
win = 0
starty =550
wall_rx = 1000
wall_ry = -200
wall_lx = -8
wall_ly = -200
wall_Tx = -8
wall_Ty = -8
b_time=1
e_shot = int(100)
wave = 1
ship_x = 15
ship_y = 15
stage = 0
#Setup of Starting objects
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
space = bckgrnd1()
logo = back2()
wall_r = BouncePhysics(wall_rx,wall_ry,10,1000)
wall_l = BouncePhysics(wall_lx,wall_ly,10,1000)
wall_T = BouncePhysics(wall_Tx,wall_Ty,10000,10)
kerbal = move(startx,starty)
back_grounds.add(space)
playable.add(kerbal)
walls.add(wall_r,wall_l,wall_T)

def spawn_ships():
    invade_ships.empty()
    invade_ships.add(BadShips(ship_x,ship_y,1))   
    invade_ships.add(BadShips(ship_x+80,ship_y,1))  
    invade_ships.add(BadShips(ship_x+160,ship_y,1))  
    invade_ships.add(BadShips(ship_x+240,ship_y,1))  
    invade_ships.add(BadShips(ship_x+320,ship_y,1))  
    invade_ships.add(BadShips(ship_x+400,ship_y,1))  
    invade_ships.add(BadShips(ship_x+480,ship_y,1))  
    invade_ships.add(BadShips(ship_x+560,ship_y,1))  
    invade_ships.add(BadShips(ship_x+640,ship_y,1))  

    invade_ships.add(BadShips(ship_x,ship_y+40,2))  
    invade_ships.add(BadShips(ship_x+80,ship_y+40,2))  
    invade_ships.add(BadShips(ship_x+160,ship_y+40,2))  
    invade_ships.add(BadShips(ship_x+240,ship_y+40,2))  
    invade_ships.add(BadShips(ship_x+320,ship_y+40,2))  
    invade_ships.add(BadShips(ship_x+400,ship_y+40,2))  
    invade_ships.add(BadShips(ship_x+480,ship_y+40,2))  
    invade_ships.add(BadShips(ship_x+560,ship_y+40,2))  
    invade_ships.add(BadShips(ship_x+640,ship_y+40,2))  

    invade_ships.add(BadShips(ship_x,ship_y+80,3))  
    invade_ships.add(BadShips(ship_x+80,ship_y+80,3))  
    invade_ships.add(BadShips(ship_x+160,ship_y+80,3))  
    invade_ships.add(BadShips(ship_x+240,ship_y+80,3))  
    invade_ships.add(BadShips(ship_x+320,ship_y+80,3))  
    invade_ships.add(BadShips(ship_x+400,ship_y+80,3))  
    invade_ships.add(BadShips(ship_x+480,ship_y+80,3))  
    invade_ships.add(BadShips(ship_x+560,ship_y+80,3))  
    invade_ships.add(BadShips(ship_x+640,ship_y+80,3))  

    invade_ships.add(BadShips(ship_x,ship_y+120,4))  
    invade_ships.add(BadShips(ship_x+80,ship_y+120,4))  
    invade_ships.add(BadShips(ship_x+160,ship_y+120,4))  
    invade_ships.add(BadShips(ship_x+240,ship_y+120,4))  
    invade_ships.add(BadShips(ship_x+320,ship_y+120,4))  
    invade_ships.add(BadShips(ship_x+400,ship_y+120,4))  
    invade_ships.add(BadShips(ship_x+480,ship_y+120,4))  
    invade_ships.add(BadShips(ship_x+560,ship_y+120,4))  
    invade_ships.add(BadShips(ship_x+640,ship_y+120,4))  

    invade_ships.add(BadShips(ship_x,ship_y+160,5))  
    invade_ships.add(BadShips(ship_x+80,ship_y+160,5))  
    invade_ships.add(BadShips(ship_x+160,ship_y+160,5))  
    invade_ships.add(BadShips(ship_x+240,ship_y+160,5))  
    invade_ships.add(BadShips(ship_x+320,ship_y+160,5))  
    invade_ships.add(BadShips(ship_x+400,ship_y+160,5))  
    invade_ships.add(BadShips(ship_x+480,ship_y+160,5))  
    invade_ships.add(BadShips(ship_x+560,ship_y+160,5))  
    invade_ships.add(BadShips(ship_x+640,ship_y+160,5))
#leftE = shipEnds.add(ship_x,ship_y)
#RightE = shipEnds.add(ship_x+640,ship_y)
spawn_ships()
ship_direction=1
end_direction=1
current_y=15
destroyed = 0
score = 0

pygame.display.set_caption("Space Invaders")
font = pygame.font.SysFont('Futura', 60)
font_score = pygame.font.SysFont('Consolas', 30)
def display():
    global menuon,bull1,x_start,y_start
    window.fill((255,255,255)) #White background
    #object_draw_name=pygame.draw.rect(window,(COLOR_CODE),(locX,locY,sizeX,sizeY))
    back_grounds.draw(window)
    walls.draw(window)
    if win == 1: 
        window.blit(font.render("You Win..", True, (230, 203, 0)), (280,500))
    if menuon == 1:
        window.blit(font.render("Press Enter to Continue...", True, (230, 203, 0)), (280,500)) 
    if gamestart == 1:
        playable.draw(window)
        Bullets_player.draw(window)
        invade_ships.draw((window))
        shipEnds.draw(window)
        Bullets_enemy.draw(window)
        window.blit(font_score.render(f"Score: {score}", True, (0, 0, 0)), (500,650))
while True:
    key_input = pygame.key.get_pressed()
    display()
    for event in pygame.event.get():
        # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        
    b_time-=1  
    if gamestart==0:
        if key_input[pygame.K_RETURN]: 
            back_grounds.remove(logo)
            menuon = 0
            gamestart = 1
            spawn_ships()
    if pygame.sprite.spritecollide(kerbal, walls, False, collided=pygame.sprite.collide_mask):
        kerbal.rect.x-=kerbal.x
    if gamestart == 1:
        if key_input[pygame.K_SPACE] and b_time <0:
            Bullets_player.add(bullet(kerbal.rect.x+40,550))
            b_time=5 
        
    for enemy in invade_ships:
        gets_hit = pygame.sprite.spritecollide(enemy, walls, False, collided=pygame.sprite.collide_mask)
        if gets_hit:
            ship_direction= -ship_direction
            stage = -stage
            current_y = enemy.rect.y
            break

    for shot in Bullets_player:
        gets_hit = pygame.sprite.spritecollide(shot, invade_ships, True, collided=pygame.sprite.collide_mask)
        if gets_hit:
            Bullets_player.remove(shot)
            score += 10
    if score == 450:
        gamestart = 0
        win = 1 
        btn = window.blit(font.render("Exit", True, (197, 180, 130)), (600, 500))
        playagn = window.blit(font.render("Play Again?", True, (255,255,255)), (250, 300))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            ## check if cursor is on button ##
            if btn.collidepoint(pos):
                pygame.quit()
                sys.exit()
            """if playagn.collidepoint(pos):
                spawn_ships()
                display() """

    e_shot-=100
    if e_shot<=int(0) and gamestart ==1:        
        chosesn = random.choice(invade_ships.sprites())
        Bullets_enemy.add(enemyshot(chosesn.rect.x+30,chosesn.rect.y+30))
        e_shot = 750 
    Bullets_player.update()
    Bullets_enemy.update()   
    invade_ships.update(ship_direction,current_y,stage)  
    kerbal.moveguy(kerbx,kerby,gamestart) 
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw