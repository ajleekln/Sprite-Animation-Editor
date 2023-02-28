import pygame
from  FrameBox import FrameBox

class Image:
    
    def __init__(self, path : str):
        
        self.__path_location = path
        self.__surface = pygame.image.load(self.__path_location)
        self.__hitboxes = [] 
        self.__witdth = 0 
        self.__height = 0
        self.__pivot_pos = (0,0)
        
    def load(self, path : str):
        self.__path_location = path
        self.__surface = pygame.image.load(self.__path_location)
        
    def save(self, surface : pygame.Surface, path : str):
        pygame.image.save(surface, path)
        
    def flip_image(x_axis : bool , y_axis : bool) -> pygame.Surface: 
        return pygame.transform.flip(self.__surface, x_axis, y_axis)
    
    def set_pivot_position(self, pos):
        self.__pivot_pos = pos
    def get_pivot_position(self) -> tuple:
        return self.__pivot_pos
        
    def add_hitbox(self, hitbox : FrameBox):
        self.__hitboxes.append(hitbox)
    def remove_hitbox(self, hitbox : FrameBox):
        self.__hitboxes.remove(hitbox)
        
    def find_color_in_image(color, unique_flag = False) -> list:
        # will find all occurances of color and return location of all 
        # if unique flag is set to true, if there is more than one occurance rasie error
        pass
    
    def set_height(self, height):
        self.__height = height
    def get_height(self) -> int:
        return self.__height
    
    def set_width(self, width):
        self.__width = width
    def get_width(self) -> int:
        return self.__width 
    
    def get_surface(self):
        return self.__surface
