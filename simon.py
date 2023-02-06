import sys, pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

seq = None
def make_random_pattern():
    seq = []
    for i in range(5):
        seq = seq + [random.randint(0, 3)]
    return seq


def check_click(pos, pattern, step):
    x, y = pos
    if x <= 250 and y <= 250:
        return 0 == pattern[step]
    elif x <= 250 and y > 250:
        return 1 == pattern[step]
    elif x > 250 and y > 250:
        return 2 == pattern[step]
    elif x > 250 and y <= 250:
        return 3 == pattern[step]
    return False


convert = {0: "a", 1: "b", 2: "c", 3: "d"}
pattern = make_random_pattern()
show_colour = -1
step = 0

while True:
    events = pygame.event.get()
    screen.fill((0, 0, 0))
    a = pygame.draw.rect(screen, (100, 0, 0), (0, 0, 250, 250))
    b = pygame.draw.rect(screen, (0, 0, 100), (0, 250, 250, 250))
    c = pygame.draw.rect(screen, (100, 100, 0), (250, 250, 250, 250))
    d = pygame.draw.rect(screen, (0, 100, 0), (250, 0, 250, 250))
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if check_click(pos, pattern, step):
                step += 1
                if step == len(pattern):
                    pattern = make_random_pattern()
                    step = 0
            else:
                pattern = make_random_pattern()
                step = 0

            if show_colour >= 0:
                con = convert[pattern[step]]
                if con == "a":
                    pygame.draw.rect(screen, (255, 0, 0), (0, 0, 250, 250))
                    print("1")
                elif con == "b":
                    pygame.draw.rect(screen, (0, 255, 0), (250, 0, 250, 250))
                    print("2")

                elif con == "c":
                    pygame.draw.rect(screen, (0, 0, 255), (0, 250, 250, 250))
                    print("3")

                else:
                    pygame.draw.rect(screen, (255, 255, 0),
                                     (250, 250, 250, 250))
                    print("4")

                show_colour = (show_colour + 1) % 5
            else:
                screen.fill((0, 0, 0))

    clock.tick(10)
    pygame.display.update()
    show_colour = (show_colour + 1) % 5