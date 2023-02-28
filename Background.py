import pygame
from Animation import Animation
class Background:
    
    def __init__(self, surface : pygame.Surface, width : int, height : int):
        self.__width = width
        self.__height = height
        self.__surface = surface
        
    def __init__(self, surface : pygame.Surface, size : tuple(int, int)):
        self.__width = size[0]
        self.__height = size[1]
        self.__surface = surface
        
    def get_surface(self) -> pygame.Surface:
        return self.__surface
    def set_surface(self, surface : pygame.Surface):
        self.__surface = surface 
        

class BackgroundAnimated(Background):
    
    def __init__(self, animation : Animation)