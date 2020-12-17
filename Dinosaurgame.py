import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Dinosaur Game")

icon=pygame.image.load('gorgosaurus-dinosaur-shape.png')
pygame.display.set_icon(icon)


moon_pic = pygame.image.load('moon.png')
moonX = 760
moonY = 40

star_pic1 = pygame.image.load('stars.png')
starX1 = 720
starY1 = random.randint(50, 170)

star_pic2 = pygame.image.load('stars.png')
starX2 = 500
starY2 = random.randint(50, 170)

star_pic3 = pygame.image.load('stars.png')
starX3 = 250
starY3 = random.randint(50, 170)

cloud_pic1 = pygame.image.load('clouds.png')
cloudX1 = 500
cloudY1 = random.randint(100, 250)

cloud_pic2 = pygame.image.load('clouds.png')
cloudX2 = 860
cloudY2 = random.randint(100, 250)

surface_pic = pygame.image.load('Surface.png')
surfaceX = 0
surfaceY = 150

cactus_pic1 = pygame.image.load('cactus.png')
cactusX1 = 400
cactusY1 = 334

cactus_pic2 = pygame.image.load('cactus.png')
cactusX2 = 800
cactusY2 = 334

dinosaur_pic1 = pygame.image.load('dinostanding.jpg')
dinosaurX = 200
dinosaurY = 310

dinosaur_pic2 = pygame.image.load('dinorightfoot.jpg')

dinosaur_pic3 = pygame.image.load('dinoleftfoot.jpg')

dinosaur_pic4 = pygame.image.load('dinocollided.jpg')

moon_change = 0.15
star_change = 0.25
cloud_change = 0.60
dino_change = 2.5
cactus_change = 2
loop_count = 0
walk_point = 0
over_font = pygame.font.Font('freesansbold.ttf',64)
textX = 10
textY = 10
score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
count1 = 0
score_change = 1

state = None
scorer = None

def stars1(x,y):
    screen.blit(star_pic1,(x,y))

def stars2(x,y):
    screen.blit(star_pic2,(x,y))

def stars3(x,y):
    screen.blit(star_pic3,(x,y))

def moon(x,y):
    screen.blit(moon_pic,(x,y))

def surface(x,y):
    screen.blit(surface_pic,(x,y))

def cactus1(x,y):
    screen.blit(cactus_pic1,(x,y))

def cactus2(x,y):
    screen.blit(cactus_pic2,(x,y))

def cloud1(x,y):
    screen.blit(cloud_pic1,(x,y))

def cloud2(x,y):
    screen.blit(cloud_pic2,(x,y))

def dinosaur1(x,y):
    screen.blit(dinosaur_pic1,(x,y))

def dinosaur2(x,y): 
    screen.blit(dinosaur_pic2,(x,y))

def dinosaur3(x,y):
    screen.blit(dinosaur_pic3,(x,y))

def dinosaur4(x,y):
    screen.blit(dinosaur_pic4,(x,y))




def game_over_text():
    over_text= over_font.render("GAME OVER", True, (0,0,0))  
    screen.blit(over_text, (200,250))

def isCollision(x,y,x1,y1,x2,y2):
    if x1<=x+64 and x1>=x or x2<=x+64 and   x2>=x:
        if y+64 >= y1 or y+64 >= y2:
            return True
        else:
            return False
    else:
        return False

def showscore(x,y):
    score = font.render("Score : "+str(score_value)+"m",True,(0,0,0))
    screen.blit(score,(x,y))

def continuing(x,y):
    cont = font.render("Press space to restart",True,(0,0,0))
    screen.blit(cont,(x,y))
    ev = pygame.event.get()
    if ev.type == pygame.K_SPACE :
        return True

running = True

while running:
    screen.fill(((255,255,255)))

    if loop_count >=5000:
        moon_change += 0.001
        star_change += 0.001
        cloud_change += 0.001
        cactus_change+=0.001
        dino_change +=0.00001

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.K_SPACE or event.type == pygame.KEYUP and state == None:
            state = "Rise"
    if state == "Rise":   
        if dinosaurY <=210:
            state = "Descent"
        dinosaurY-=dino_change
    elif state == "Descent":
        if dinosaurY >= 310:
            state = None
        dinosaurY+=dino_change


    starX1-=star_change
    starX2-=star_change
    starX3-=star_change
    moonX-=moon_change
    cactusX1-=cactus_change
    cactusX2-=cactus_change
    cloudX1-=cloud_change
    cloudX2-=cloud_change

    if moonX < -150:
        moonX=850
    if starX1 < -100:
        starX1 = 840
        starY1 = random.randint(50, 170)
    if starX2 < -100:
        starX2 = 840
        starY2 = random.randint(50, 170)
    if starX3 < -100:
        starX3 = 840
        starY3 = random.randint(50, 170)

    if cactusX1 < -100:
        cactusX1 = 800
    if cactusX2 < -100:
        cactusX2 = 800

    if cloudX1 < -100:
        cloudX1 = 840
        cloudY1 = random.randint(100, 250)

    if cloudX2 < -100:
        cloudX2 = 840
        cloudY2 = random.randint(100, 250)

    
    moon(moonX,moonY)
    stars1(starX1,starY1)
    stars2(starX2,starY2)
    stars3(starX3,starY3)
    surface(surfaceX,surfaceY)
    cactus1(cactusX1,cactusY1)
    cactus2(cactusX2,cactusY2)
    cloud1(cloudX1,cloudY1)
    cloud2(cloudX2,cloudY2)
    if loop_count==1:
        dinosaur1(dinosaurX,dinosaurY)
    elif loop_count%2==0:
        dinosaur2(dinosaurX,dinosaurY)
    elif loop_count%2!=0:
        dinosaur3(dinosaurX,dinosaurY)
    Collision = isCollision(dinosaurX,dinosaurY,cactusX1,cactusY1,cactusX2,cactusY2)
    if Collision ==True:
        dinosaur4(dinosaurX,dinosaurY)
        moon_change = 0
        star_change = 0
        cloud_change = 0
        dino_change = 0
        cactus_change =0
        loop_count = 0
        score_change = 0

        game_over_text()

    score_value += score_change
    showscore(textX,textY)
    loop_count+=1
    pygame.display.update()
        
