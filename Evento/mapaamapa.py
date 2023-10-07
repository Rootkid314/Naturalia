import pygame,  sys
pygame.init()
screen = pygame.display.set_mode([900, 600])
r = pygame.Color("red")
w = pygame.Color("white")

lead_x = 200
lead_y = 200

data = [
  [ w, w, r, r, r, r, r, w, w ],
  [ w, w, r, w, r, w, r, w, w ],
  [ w, w, r, r, r, r, r, w, w ],
  [ w, r, r, r, w, r, r, r, w ],
  [ r, w, w, r, r, r, w, w, r ],
  [ r, r, w, w, w, w, w, r, r ]
  ]

def dibujar():
    for y, row in enumerate(data):
        for x, colour in enumerate(row):
            rect = pygame.Rect(x*50, y*50, 50, 50)
            rect.move_ip(lead_x,lead_y)
            screen.fill(colour, rect=rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x +=10
            if event.key == pygame.K_UP:
                lead_y -=10
            if event.key == pygame.K_DOWN:
                lead_y +=10
    screen.fill(w)
    dibujar()
    pygame.display.update()