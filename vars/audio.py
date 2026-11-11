import pygame
from vars.descriptions import AUDIO_DIR

pygame.mixer.init()

sounds = {
    "door": pygame.mixer.Sound(AUDIO_DIR / "temp door.ogg"),
    "stairs": pygame.mixer.Sound(AUDIO_DIR / "temp stairs.ogg"),
    "unlock": pygame.mixer.Sound(AUDIO_DIR / "temp unlock.ogg"),
    "locked": pygame.mixer.Sound(AUDIO_DIR / "temp locked.ogg"),
    "walk": pygame.mixer.Sound(AUDIO_DIR / "temp walk.ogg"),
    "punch": pygame.mixer.Sound(AUDIO_DIR / "temp punch.ogg"),
    "swoosh": pygame.mixer.Sound(AUDIO_DIR / "temp swoosh.ogg"),
    "sword hit": pygame.mixer.Sound(AUDIO_DIR / "temp light metal.ogg"),
    "kill": pygame.mixer.Sound(AUDIO_DIR / "temp kill.ogg"),
    "death": pygame.mixer.Sound(AUDIO_DIR / "temp gameover.ogg"),
    "lever": pygame.mixer.Sound(AUDIO_DIR / "temp lever.ogg"),
    "revolver": pygame.mixer.Sound(AUDIO_DIR / "temp revolver.ogg"),
    "r reload": pygame.mixer.Sound(AUDIO_DIR / "temp r reload.ogg")
}

music = {
    "exterior": pygame.mixer.Sound(AUDIO_DIR / "exterior bg.ogg"),
}