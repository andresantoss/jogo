import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.05)
musica_fundo = pygame.mixer.music.load('BoxCat Games - Storm.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('Super_Mario_Bros_Coin_Sound_Effect.mp3')

largura = 640
altura = 480

x = int(largura/2)
y = int(altura/2)

x_azul = randint(40,600)
y_azul = randint(50,430)

pontos = 0

fonte = pygame.font.SysFont('arial',40,True, True,)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('SkullWarrior')
relogio = pygame.time.Clock()


while True:
    relogio.tick(30)
    tela.fill((0,0,0))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem,True,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20'''
    if pygame.key.get_pressed()[K_a]:
        x=x-20
    if pygame.key.get_pressed()[K_d]:
        x=x+20
    if pygame.key.get_pressed()[K_w]:
        y=y-20
    if pygame.key.get_pressed()[K_s]:
        y=y+20
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x, y, 40,50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 250), (x_azul, y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40,600)
        y_azul = randint(50,430)
        pontos = pontos + 1
        barulho_colisao.play()

    # if y >= altura:
    #     y = 0
    # y = y + 1
    #x = x + 1
    #pygame.draw.circle(tela, (0, 0, 255), (300,260), 40)
    #pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5 )
    tela.blit(texto_formatado,(400,40))


    pygame.display.update()
