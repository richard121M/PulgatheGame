import pygame

LISTA_INPUTS = [
    [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN],
    [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]
]

class ControleJogador:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def controle(self):
        inputs = []
        Entrada = LISTA_INPUTS[self.id]
        teclas = pygame.key.get_pressed()


        if teclas[Entrada[0]]:
            inputs.append("LEFT")
        if teclas[Entrada[1]]:
            inputs.append("RIGHT")
        if teclas[Entrada[2]]:
            inputs.append("UP")
        if teclas[Entrada[3]]:
            inputs.append("DOWN")

        return inputs