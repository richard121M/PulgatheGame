import pygame

class Pulga:
    def __init__(self, x, y, debug=False):
        self.position = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.acel = pygame.Vector2(0, 0)
        self.debug = debug
        self.isfloor = False
        self.width = 20
        self.height = 20
        self.img = pygame.Surface((self.width, self.height))
        self.img.fill((0, 255, 0)) 

    def drawing(self, tela):
        tela.blit(self.img, (self.position.x, self.position.y))
        if self.debug:
            self.debugging(tela)

    def controle(self, CONTROLE):
        self.vel.x = 0
        if "LEFT" in CONTROLE:
            self.vel.x = -5
        if "RIGHT" in CONTROLE:
            self.vel.x = 5
        if "UP" in CONTROLE and self.isfloor:
            self.acel.y = -3
        
    def update(self):
        self.vel.y += self.acel.y
        self.position.x += self.vel.x
        self.position.y += self.vel.y

        if (self.position.y + self.height) >= 600:
            self.isfloor = True
            self.position.y = 600 - self.height
            self.vel.y = 0
            self.acel.y = 0
        else:
            self.isfloor = False
        self.acel.y += 0.5 if self.acel.y < 1 else 0 

    def debugging(self, tela):

        texto = f"POS: ({self.position.x:.0f}, {self.position.y:.0f}) \n VEL: ({self.vel.x:.2f}, {self.vel.y:.2f}) \nACE: ({self.acel.x:.2f}, {self.acel.y:.2f})"

        fonte = pygame.font.SysFont("arial", 12, bold=True)
        superficie_texto = fonte.render(texto, True, (255, 255, 255))
        retangulo_texto = superficie_texto.get_rect()
        retangulo_texto.bottomleft = (self.position.x + self.width, self.position.y)
        tela.blit(superficie_texto, retangulo_texto)
        