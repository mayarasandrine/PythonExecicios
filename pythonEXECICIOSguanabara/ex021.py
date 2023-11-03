'''crie um programa que toque uma musica em MP3 aqui'''

'''import pygame
pygame.init()
pygame.mixer.music.load('ex21B.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

import pygame
#chamamos o programa com a biblioteca
pygame.init()
#aqui iniciamos o programa
pygame.mixer.music.load('ex21B.mp3')
#informamos o caminho do qual anexamos no nosso pycharm
pygame.mixer.music.play()
#comando para iniciar a musica
input()
# precisa que seja anexado o input nessa nova versão do python
pygame.event.wait()
# finalização do programa
