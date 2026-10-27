import pygame
import sys
import random

pygame.init()

LARGURA = 600
ALTURA = 600
VAO_LIVRE = 150
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo do Flappy Bird")

relogio = pygame.time.Clock()

pygame.font.init()
fonte_pontos = pygame.font.SysFont("arial", 40, bold=True)

COR_CEU = (135, 206, 235)
verde = (136, 231, 136)
BRANCO = (255, 255, 255) 

imagem_passaro = pygame.image.load("passaro.png")

imagem_passaro = pygame.transform.scale(imagem_passaro, (40, 30))

passaro_largura = imagem_passaro.get_width()
passaro_altura = imagem_passaro.get_height()

passaro_x = 100
passaro_y = 300
forca_pulo = -8

velocidade = 0
gravidade = 0.5

cano_x = 500          
cano_largura = 70     
cano_velocidade = 4 

pontos = 0
passou_pelo_cano = False 

def gerar_posicao_cano():
    altura_cano_de_cima = random.randint(50, 400)
    posicao_y_cano_embaixo = altura_cano_de_cima + VAO_LIVRE
    return altura_cano_de_cima, posicao_y_cano_embaixo

cano_cima_y, cano_baixo_y = gerar_posicao_cano()

while True:
    relogio.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                velocidade = forca_pulo


    velocidade += gravidade
    passaro_y += velocidade


    if passaro_y > ALTURA - passaro_altura:
        passaro_y = ALTURA - passaro_altura
        velocidade = 0


    cano_x -= cano_velocidade


    if cano_x < -cano_largura:
        cano_x = LARGURA
        cano_cima_y, cano_baixo_y = gerar_posicao_cano()
        passou_pelo_cano = False 


    if cano_x + cano_largura < passaro_x and not passou_pelo_cano:
        pontos += 1
        passou_pelo_cano = True 



    rect_passaro = pygame.Rect(passaro_x, passaro_y, passaro_largura, passaro_altura)
    rect_cano_cima = pygame.Rect(cano_x, 0, cano_largura, cano_cima_y)
    
    altura_cano_baixo = ALTURA - cano_baixo_y
    rect_cano_baixo = pygame.Rect(cano_x, cano_baixo_y, cano_largura, altura_cano_baixo)


    if rect_passaro.colliderect(rect_cano_cima) or rect_passaro.colliderect(rect_cano_baixo):
        print(f"Game Over! Pontuação Final: {pontos}")
        break


    tela.fill(COR_CEU)


    tela.blit(imagem_passaro, (int(passaro_x), int(passaro_y)))
    

    pygame.draw.rect(tela, verde, rect_cano_cima)
    pygame.draw.rect(tela, verde, rect_cano_baixo)


    texto_placar = fonte_pontos.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto_placar, (20, 20))

    pygame.display.flip()
