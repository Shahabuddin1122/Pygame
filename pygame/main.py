import pygame as py
from time import sleep
py.init()
window=py.display.set_mode((0,0),py.FULLSCREEN)
py.mixer.init()
py.mixer.music.load("Scary Ghost Voices - QuickSounds.com.mp3")
py.mixer.music.play()
image=py.image.load('lan-gao-m3pfOQKgVAM-unsplash.jpg')
window.blit(image,(0,0))
py.display.update()
sleep(20)


