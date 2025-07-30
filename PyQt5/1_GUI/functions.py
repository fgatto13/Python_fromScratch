# we could also use a sound effect when opening the window:
import pygame

def start_sound():
    sound_file = "music/sound.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()