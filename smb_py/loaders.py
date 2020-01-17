import pygame
import pytmx
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def get_image(image):
    return pygame.image.load(os.path.join(dir_path, image)).convert_alpha()


def get_map(map_file):
    return pytmx.load_pygame(os.path.join(dir_path, map_file))


def get_font(font_path, size=20):
    return pygame.font.Font(os.path.join(dir_path, font_path), size)


def get_sound(sound_path):
    return pygame.mixer.Sound(os.path.join(dir_path, sound_path))
