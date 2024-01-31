# Tocando MP3
import pygame

musica = r'C:\Users\ander\Music\celebridade.mp3'

pygame.init()

pygame.mixer.music.load(musica)

pygame.mixer.music.play()

x = input('Digite algo para parar a musica.....')
