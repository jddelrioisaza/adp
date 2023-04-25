import pygame

class PygameVisualizer:
    
    def __init__(self, width, height):
        
        self.width = width
        self.height = height
        
        # Inicializar la ventana
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

        # Cambia el nombre de la ventana a "Pila"
        pygame.display.set_caption("Pila")
        
        # Colores
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        
        # Fuente
        self.font = pygame.font.SysFont('Arial', 20)
        
    def draw(self, pila):
        
        # Dibujar la pila en la pantalla
        self.clear()
        
        # Dibujar el fondo de la pila
        pygame.draw.rect(self.screen, self.black, [50, 50, 100, 300], 2)
        
        # Dibujar los elementos de la pila
        for i, elemento in enumerate(pila):
            texto = self.font.render(elemento, True, self.black)
            self.screen.blit(texto, (70, 320 - i * 20))
            pygame.draw.line(self.screen, self.black, (50, 320 - i * 20), (150, 320 - i * 20))
        
        # Actualizar la pantalla
        pygame.display.update()

    def clear(self):
        self.screen.fill((255, 255, 255))
        pygame.display.update()
