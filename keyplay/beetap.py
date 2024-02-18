import os
import random
from threading import Thread

import pygame
from pynput import keyboard
from pynput.keyboard import Key

from keyplay.map import sounds_dict


SOUNDS_DIR = "./beats/sounds/"
TRACKS_DIR = "./beats/tracks/"


def play_beat(music_file):
    sound = pygame.mixer.Sound(SOUNDS_DIR + music_file)
    sound.play()


def play_background():
    beat_rhythm = ""
    beat_rhythm += "3443443443443434"
    beat_rhythm += "5665665665665656"
    beat_rhythm += "7887887887887878"
    beat_rhythm += "9119119119119191"
    while True:
        for beat in beat_rhythm:
            pygame.mixer.music.load(TRACKS_DIR + beat + "beat.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass


def on_press(key):
    try:
        result = sounds_dict.get(key.char, "")
        if result != "":
            play_beat(result)
    except AttributeError:
        result = sounds_dict.get(key, "")
        if result != "":
            play_beat(result)


def on_release(key):
    try:
        pass
    except AttributeError:
        if key == Key.esc:
            return False


pygame.mixer.init()
thread1 = Thread(target=play_background)
thread1.daemon = True
thread1.start()

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
