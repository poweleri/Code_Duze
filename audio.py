import pygame


pygame.mixer.init()
sounds = {}

def handler(e):
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_SPACE:
            play_sound('button.ogg')
        if e.key == pygame.QUIT:
            pygame.mixer.music.stop()

def quit(e):
    global run 
    if e.type == pygame.QUIT:
        run = False

def play_sound(file):
    global sounds
    sound = sounds.get(file)
    if sound == None:
        sound = pygame.mixer.Sound(file)
        sounds[file] = sound
    sound.play()

def init():
    pygame.mixer.music.load('background_music.ogg')
    pygame.mixer.music.play(-1)