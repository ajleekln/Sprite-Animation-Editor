import pygame

class FrameBox:
    
    def __init__(self, width, height, color = (0,0,0,0), pos = (0,0)):
        
        self.__width = width
        self.__height = height
        self.__color = color
        self.__pos = pos
        self.__surface = pygame.Surface(self.__width, self.__height)
        
    def set_pos(self, pos):
        self.__pos = pos
        
    def set_size(self, width, height):
        self.__width = width
        self.__height = height
    
    def set_alpha(self, alpha):
        # cannot be negative 
        # cannot exceed 255  
        self.color[3] = alpha
    
    def set_color(self, color):
        self.__color = color
        
    def set_transparent(self):
        self.color[3] = 0