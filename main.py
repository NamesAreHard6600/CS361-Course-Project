# from alarm import Alarm
from ui import UI
import pygame

def main():
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
    window = UI(True)
    window.display()

if __name__ == '__main__':
    main()