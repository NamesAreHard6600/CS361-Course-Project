# from alarm import Alarm
from ui import UI
import pygame

def main():
    pygame.mixer.init()
    window = UI(True)
    window.display()

if __name__ == '__main__':
    main()