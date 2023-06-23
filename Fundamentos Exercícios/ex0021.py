# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
# usar módulos. Existem várias soluções.

import pygame
pygame.init()
pygame.mixer.music.load('ex0021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
