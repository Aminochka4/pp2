import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
radius = 25
color = (255, 0, 0)
x = 250
y = 250
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>= radius: y -= 2
    if pressed[pygame.K_DOWN] and y<=500-radius: y += 2
    if pressed[pygame.K_RIGHT] and x<=500-radius: x += 2
    if pressed[pygame.K_LEFT] and x>radius: x -= 2

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)