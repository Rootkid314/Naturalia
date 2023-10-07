import pygame

screen = pygame.display.set_mode([720, 720])
Clock =  pygame.time.Clock()

done = False

background = pygame.image.load ("background.png").convert()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =  True
            
    screen.blit(background, [0, 0])
    pygame.display.flip()
    Clock.tick(60)

pygame.quit()