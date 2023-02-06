import pygame
import math

def tixy(t, i, x, y):
    circle_size = abs(math.sin(t + i) * 15)
    return circle_size

def draw_circles(screen, t):
    i = 0
    for y in range(16):
        for x in range(16):
            circle_size = tixy(t, i, x, y)
            x_location = x * (500 / 16) + (500 / 32)
            y_location = y * (500 / 16) + (500 / 32)
          
            if math.sin(t + i) > 0:
                color = (255, 0, 0)
              
            else:
                color = (0, 0, 255)
              
            i = i +1
            pygame.draw.circle(screen, color, (int(x_location), int(y_location)), int(circle_size))


pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
frame_rate = 5
t = 0

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      
  screen.fill((0, 0, 0))
  draw_circles(screen, t)
  pygame.display.update()
  t += 1 / frame_rate
  clock.tick(frame_rate)