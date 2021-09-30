from sys import exit
import pygame
from pygame.locals import *
from random import randint

pygame.init()

largura = 640
altura = 480

x = int(largura/2)
y = int(altura/2) 

comidaX = randint(50, 590)
comidaY = randint(50, 430)

tamanho = 20
velocidade = 10
controleX = velocidade
controleY = 0

pontos = 0

fonte = pygame.font.SysFont('roboto', 40, True, False)

janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo da cobrinha')
relogio = pygame.time.Clock()

listaCobra = []
comprimentoInicial = 5

morreu = False

def cobraAlimenta(listaCobra):
    for XeY in listaCobra: # XeY = Lista de valores
        pygame.draw.rect(janela, (255, 255, 255), (XeY[0], XeY[1], tamanho, tamanho))

def reStart():
    global pontos, comprimentoInicial, x, y, listaCobra, listaCabeça, comidaX, comidaY, morreu
    pontos = 0
    comprimentoInicial = 5
    x = int(largura/2)
    y = int(altura/2) 
    listaCobra = []
    listaCabeça = []
    comidaX = randint(50, 590)
    comidaY = randint(50, 430)
    morreu = False

while True:
    relogio.tick(30)
    janela.fill((0, 0, 0))
    
    msg = f'Score: {pontos}'
    textoFormato = fonte.render(msg, False, (255, 255, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if controleX == velocidade:
                    pass
                else:
                    controleX = -velocidade
                    controleY = 0
            if event.key == K_d:
                if controleX == -velocidade:
                    pass
                else:
                    controleX = velocidade
                    controleY = 0
            if event.key == K_w:
                if controleY == velocidade:
                    pass
                else:
                    controleY = -velocidade
                    controleX = 0
            if event.key == K_s:
                if controleY == -velocidade:
                    pass
                else:
                    controleY = velocidade
                    controleX = 0
        
        x += controleX
        y += controleY

        cobrinha = pygame.draw.rect(janela, (255, 255, 255), (x, y, tamanho, tamanho))
        comida = pygame.draw. rect(janela, (255, 0, 0), (comidaX, comidaY, 20, 20))

        if cobrinha.colliderect(comida):
            comidaX = randint(50, 590)
            comidaY = randint(50, 430)
            pontos += 1
            comprimentoInicial += 1

        listaCabeça = []
        listaCabeça.append(x)
        listaCabeça.append(y)

        listaCobra.append(listaCabeça)
        
        if listaCobra.count(listaCabeça) > 1:
            fonte2 = pygame.font.SysFont('roboto', 20, True, True)
            msg2 = 'Game Over! Press "space" to play again'
            textoFormatado = fonte2.render(msg2, True, (0, 0, 0))
            textoRet = textoFormatado.get_rect()
            morreu = True
            while morreu:
                janela.fill((255, 255, 255))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()

                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            reStart()

                textoRet.center =  (largura//2, altura//2)
                janela.blit(textoFormatado, textoRet)
                pygame.display.update()


        if len(listaCobra) > comprimentoInicial:
            del listaCobra[0]

        cobraAlimenta(listaCobra)


        janela.blit(textoFormato, (450, 40))
        pygame.display.update()


