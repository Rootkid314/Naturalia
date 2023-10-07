import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
x = 30
y = 30

clock = pygame.time.Clock()

#El tamaño del cuadro rojo y las cordenadas de donde va aparecer
red = (255, 0 ,0)


simulator_rect = pygame.Rect(225, 125, 30, 30)
quiz_rect = pygame.Rect(600, 125, 30, 30)
quit_rect = pygame.Rect(375, 425, 30, 30)
# Representa 3 rectoss de opcion
option_rects = [simulator_rect, quiz_rect, quit_rect]

# tu selector azul rect
selector_rect = pygame.Rect(50, 50, 60, 60)
# The 50, 50 xy cordenadas temporales
#aqui esta el evento que se sucita
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 0: y -= 5
    if pressed[pygame.K_DOWN] and y < 600 - 60: y += 5
    if pressed[pygame.K_LEFT] and x > 0: x -= 5
    if pressed[pygame.K_RIGHT] and x < 800 - 60: x += 5

    #selector x y y
    selector_rect.x, selector_rect.y = x, y

    screen.fill((0, 0, 0))

    color = (0, 128, 255)
    pygame.draw.rect(screen, color, selector_rect)

    myfont = pygame.font.SysFont("monospace", 15)
#nombre de los animales y la informacion que aparece en la pantalla
    label = myfont.render("Capibara insana", 1, (255,255,255))
    screen.blit(label, (100, 100))

    label2 = myfont.render("Venado", 1, (255,255,255))
    screen.blit(label2, (550, 100))

    label3 = myfont.render("Ocelote", 1, (255,255,255))
    screen.blit(label3, (350, 400))

    
    pygame.draw.rect(screen, red, simulator_rect)
    pygame.draw.rect(screen, red, quiz_rect)
    pygame.draw.rect(screen, red, quit_rect)

    # Compruebe si el usuario presiona la tecla enter
    if pressed[pygame.K_RETURN]:
        # compruebe si la selecion rect colisiona con otro recto
        for rect in option_rects:
        
            if selector_rect.colliderect(rect):
                if rect == simulator_rect:
                    
                    print('Simulating!')
                elif rect == quiz_rect:
                    
                    print('Quizzing!')
                elif rect == quit_rect:
                    # Quitar el rect
                    done = True




    pygame.display.flip()
    clock.tick(60)