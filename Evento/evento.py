import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Desbloqueo de Misiones en Pygame")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Fuente para el texto
font = pygame.font.Font(None, 36)

# Estado de las misiones
missions = {
    "mission_1": {"name": "Misión 1", "unlocked": False},
    "mission_2": {"name": "Misión 2", "unlocked": False},
}

# Función para desbloquear una misión
def unlock_mission(mission_id):
    missions[mission_id]["unlocked"] = True

# Función para dibujar el estado de las misiones en pantalla
def draw_mission_status():
    y_offset = 100
    for mission_id, mission_info in missions.items():
        mission_text = mission_info["name"] + " - "
        if mission_info["unlocked"]:
            mission_text += "Desbloqueada"
        else:
            mission_text += "Bloqueada"
        text_surface = font.render(mission_text, True, white)
        screen.blit(text_surface, (width // 2 - 100, y_offset))
        y_offset += 50

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Comprobar si se hizo clic en el botón de desbloquear misión
            if unlock_button_rect.collidepoint(event.pos):
                # Desbloquear la Misión 1
                unlock_mission("mission_1")

    # Limpiar la pantalla
    screen.fill(black)

    # Dibujar el estado de las misiones
    draw_mission_status()

    # Dibujar el botón de desbloquear misión
    unlock_button_rect = pygame.draw.rect(screen, white, (width // 2 - 50, height - 50, 100, 40))
    unlock_button_text = font.render("Desbloquear", True, black)
    screen.blit(unlock_button_text, (width // 2 - 40, height - 40))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()