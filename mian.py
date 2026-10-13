import sys
import pygame
from controles.jogador.controleJogador import ControleJogador
from pulga.pulga import Pulga

pygame.init()

largura = 800
altura = 600
screen = pygame.display.set_mode((largura, altura),pygame.RESIZABLE)
tela = pygame.surface.Surface((largura, altura))

# 3. Define o título da janela
pygame.display.set_caption("Meu Jogo em Pygame")

relogio = pygame.time.Clock()


pulga1 = Pulga(100, 100)
controle1 = ControleJogador(1, "Jogador 1")
def main():
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False


        ## CONTROLES ##
        ## ========================== ##
        pulga1.controle(controle1.controle())
        ## ========================== ##

        ## UPDATE ##
        ## ========================== ##
        pulga1.update()
        ## ========================== ##
        
        ## DESENHO ##
        ## ========================== ##
        pulga1.drawing(tela)
        ## ========================== ##

        ## REDERIZACAO DA JANELA DO JOGO ##
        ##
        ## tudo do jogo sera desenhado dentro de
        ## tela, e depois sera desenhado na screen
        ##
        ##==================================##
        screen.fill((150, 0, 0))
        screen.blit(tela, (0, 0))
        tela.fill((0, 0, 0))
        pygame.display.flip()
        relogio.tick(60)
        ##==================================##

if __name__ == "__main__":
    main()

pygame.quit()
sys.exit()
