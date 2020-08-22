import pygame
import random
import time 
pygame.init()

WIDTH = 2560
HEIGHT = 1440

win = pygame.display.set_mode((WIDTH, HEIGHT))

beginning_time = time.time()
print(beginning_time)

x = int(WIDTH/4)
y = int(HEIGHT/2)
x_2 = int(WIDTH/2)
y_2 = int(HEIGHT/2)
x_3 = int(WIDTH*0.75)
y_3 = int(HEIGHT/2)
radius = 20
radius_2 = 20
radius_3 = 20
speed = 3
speed2 = 3
speed3 = 3

# foods = [[674,145], [523,521], [532,672], [267,267], [231,350], [342,231], [412,214], [231,343], [250,348]]

foods = []

for i in range(20):
  foods.append((random.randint(10,WIDTH-10), random.randint(10,HEIGHT-10)))



def distance(x1,y1,x2,y2):
  return ((x1-x2)**2+(y1-y2)**2)**0.5


#background
while 1+1==2:
  win.fill((0,0,0))
  pygame.time.delay(10)

  # Change speed
  speed = 3 - radius/300
  speed2 = 3 - radius_2/300
  speed3 = 3 - radius_3/300


  # controls 
  pygame.event.pump()
  keys=pygame.key.get_pressed()
  if keys[pygame.K_w]:
    y = int(y - speed)
  if keys[pygame.K_s]:
    y = int(y + speed)
  if keys[pygame.K_d]:
    x = int(x + speed)
  if keys[pygame.K_a]:
    x = int(x - speed)

  if keys[pygame.K_i]:
    y_2 = int(y_2 - speed2)
  if keys[pygame.K_k]:
    y_2 = int(y_2 + speed2)
  if keys[pygame.K_l]:
    x_2 = int(x_2 + speed2)
  if keys[pygame.K_j]:
    x_2 = int(x_2 - speed2)

  if keys[pygame.K_UP]:
    y_3 = int(y_3 - speed3 )
  if keys[pygame.K_DOWN]:
    y_3 = int(y_3 + speed3)
  if keys[pygame.K_RIGHT]:
    x_3 = int(x_3 + speed3)
  if keys[pygame.K_LEFT]:
    x_3 = int(x_3 - speed3)

  ###############################################
  
  # drawing foods
  for food in foods:
    xfood, yfood = food
    pygame.draw.circle(win, (250, 250 ,250),
    (xfood, yfood), 10)

  ##############################################

  # eating foods
  eaten = None
  eaten2 = None
  eaten3 = None
  for food in foods:
    xfood, yfood = food
    if distance(xfood,yfood,x,y) < radius:
      eaten = food
    if distance(xfood,yfood,x_2,y_2) < radius_2:
      eaten2 = food
    if distance(xfood,yfood,x_3,y_3) < radius_3:
      eaten3 = food
    
  if eaten != None:  
    try:
      foods.remove(eaten)
      foods.append((random.randint(10,WIDTH-10),random.randint(10,HEIGHT-10)))
      radius += 4
    except:
      pass

  if eaten2 != None:  
    try:
      foods.remove(eaten2)
      foods.append((random.randint(10,WIDTH-10),random.randint(10,HEIGHT-10)))
      radius_2 += 4
    except:
      pass

  if eaten3 != None:  
    try:
      foods.remove(eaten3)
      foods.append((random.randint(10,WIDTH-10),random.randint(10,HEIGHT-10)))
      radius_3 += 4
    except:
      pass

  ##############################################


  # players
  pygame.draw.circle(win,(255,0,0),(x,y), radius)
  if y < 20:
    y = 20
  if y > HEIGHT-20:
    y = HEIGHT-20
  if x < 20:
    x = 20
  if x > WIDTH-20:
    x = WIDTH-20   

  pygame.draw.circle(win,(0,255,0),(x_2,y_2), radius_2)
  if y_2 < 20:
    y_2 = 20
  if y_2 > HEIGHT-20:
    y_2 = HEIGHT-20
  if x_2 < 20:
    x_2 = 20
  if x_2 > WIDTH-20:
    x_2 = -20   

  pygame.draw.circle(win,(0,0,255),(x_3,y_3), radius_3)
  if y_3 < 20:
    y_3 = 20
  if y_3 > HEIGHT-20:
    y_3 = HEIGHT-20
  if x_3 < 20:
    x_3 = 20
  if x_3 > WIDTH-20:
    x_3 = WIDTH-20

  #players eaten
  distance1_2 = distance(x,y,x_2,y_2)
  if distance1_2 < radius:
    # 1 has eaten 2
    radius = radius + radius_2
    radius_2 = 0
  elif distance1_2 < radius_2:
    # 2 has eaten 1
    radius_2 = radius_2 + radius
    radius = 0

  distance2_3 = distance(x_3,y_3,x_2,y_2)
  if distance2_3 < radius_3:
    # 3 has eaten 2
    radius_3 = radius_3 + radius_2
    radius_2 = 0
  elif distance2_3 < radius_2:
    # 2 has eaten 3
    radius_2 = radius_3 + radius_2
    radius_3 = 0
    
  distance1_3 = distance(x,y,x_3,y_3)
  if distance1_3 < radius:
    # 1 has eaten 3
    radius = radius + radius_3
    radius_3 = 0
  elif distance1_3 < radius_3:
    # 3 has eaten 1
    radius_3 = radius_3 + radius
    radius = 0

  pygame.display.update()

ending_time = time.time()
print(ending_time - beginning_time)
