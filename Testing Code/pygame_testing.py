import pygame
from pygame import mixer

pygame.init()
pygame.mixer.pre_init()
pygame.mixer.init()

channel1 = pygame.mixer.Channel(0) # argument must be int
channel2 = pygame.mixer.Channel(1)





sound1 = pygame.mixer.Sound("Choir.wav")

channel1.play(sound1)

