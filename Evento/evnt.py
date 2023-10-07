import pygame
import sys

pygame.init()

# Definir las coordenadas donde se producirá la transición
coordenadas_transicion = (300, 300)

# Definir el mapa de destino y la posición en ese mapa
mapa_destino = "mapa2"
posicion_destino = (100, 100)

# Inicializar pygame y la pantalla
ancho, alto = 640, 480
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Transición de Mapa")

# Loop principal del juego
jugador_x, jugador_y = 50, 50
jugador_velocidad = 5

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                jugador_x += jugador_velocidad
            elif evento.key == pygame.K_LEFT:
                jugador_x -= jugador_velocidad
            elif evento.key == pygame.K_DOWN:
                jugador_y += jugador_velocidad
            elif evento.key == pygame.K_UP:
                jugador_y -= jugador_velocidad

    # Comprobar si el jugador ha llegado a las coordenadas de transición
    if (jugador_x, jugador_y) == coordenadas_transicion:
        # Aquí deberías cargar el nuevo mapa y posicionar el jugador en la posición de destino
        # Por simplicidad, este ejemplo solo cambia las coordenadas del jugador
        jugador_x, jugador_y = posicion_destino

    pantalla.fill((0, 0, 0))
    pygame.draw.rect(pantalla, (255, 0, 0), (jugador_x, jugador_y, 20, 20))
    pygame.display.flip()
    reloj.tick(60)