import pygame, sys, math
from pygame.locals import QUIT

pygame.init()


DISPLAYSURF = pygame.display.set_mode((750, 750))


x = 100
y = 150
hx = 500
hy = 500
lx = 0
ly = 0
dx = 0
dy = 0
k = 10 

aiming = False
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    
  a = 5
  b = 1000
  DISPLAYSURF.fill((0,0,0))
  
  while a < b:
    a = a + 10
    for i in range(100):
      pygame.draw.circle(DISPLAYSURF,(0, 200, 0),(i * 10, a), 3) 

  
  

  
  hole = pygame.draw.circle(DISPLAYSURF,(255,255,255),(hx,hy),10)
  ball = pygame.draw.circle(DISPLAYSURF,(200,200,200),(x,y),10)
  
  if x > 500:
    dx = dx * -0.99
  if y > 500:
    dy = dy * -0.99
  if x < 0:
    dx = dx * 0.99
  if y < 0:
    dy = dy * 0.99

  x = x + dx
  y = y + dy

  dx = dx * 0.99
  dy = dy * 0.99
      
  
  if event.type == pygame.MOUSEBUTTONDOWN:
    aiming = True
    pos = pygame.mouse.get_pos()
    x1, y1 = pos[0], pos[1]
    c1 = x - x1
    c2 = y - y1
    distance = math.sqrt(c1*c1 + c2*c2)
    if distance < 100:
      dx = c1 / k 
      aiming = False
      
  if aiming == True:
    pygame.draw.circle(DISPLAYSURF,(255,255,255),(x,y),100, 5)

  lx = hx - x
  ly = hy - y

  length_to_hole = math.sqrt(lx * lx + ly * ly)

  if length_to_hole <= 10:
    print("You win")
    break
    

  pygame.display.update()