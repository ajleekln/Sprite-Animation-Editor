import pygame
from Movement import Movement

class PageEntity:
    
    def __init__(self):
        self.__width = width 
        self.__height = height
        self.movement = Movement()
        
    def set_width(self, width):
        self.width = width
    def get_width(self) -> int:
        return self.__width
    def set_height(self, height):
        self.__height = height
    def get_height(self) -> int:
        return self.__height
    
    def get_size(self) -> tuple(int, int):
        return (self.__width, self.__height)
    def draw(self, screen):
        pass
    def update(self):
        pass
    
class Text(PageEntity):
    
    def __init__(self, style : str, size : str, text : str):
        super().__init__()
        self.__font_style = style
        self.__font_size = size
        self.__text = text
        
    def set_font_style(self, style):
        self.__font_style = style
    def get_font_style(self) -> str:
        return self.__font_style
    def set_font_size(self, size):
        self.__font_size = size
    def get_font_size(self) -> str:
        return self.__font_size
    def set_text(self, text):
        self.__text = text
    def get_text(self):
        return self.__text
    
    def draw(self, screen):
        #move center of surface to screen object
        pass
    

class Button(PageEntity):
    
    def __init__(self, width, height, color, text = "", link = None, hov_color = (0,0,0), press_color = (0,0,0)):
        super.__init__()
        self.set_height(height)
        self.set_width(width)
        self.__button_color = color
        self.__hover_color = hov_color
        self.__pressed_down_color = press_color
        self.__link = link
        self.__click_start = (-1,-1)
        #self.__text = Text()
        
        self.__surface = pygame.Surface(self.get_size())
        
    def is_over(self, pos) -> bool:
        pass
    def open_link(self):
        return self.__link
    
    def get_button_color(self) -> tuple(int,int,int):
        return self.__button_color
    def set_button_color(self, color : tuple(int,int,int)):
        self.__button_color = color    
    def get_hover_color(self) -> tuple(int,int,int):
        return self.__hover_color
    def set_hover_color(self, color : tuple(int,int,int)):
        self.__hover_color = color
    def get_press_down_color(self) -> tuple(int,int,int):
        return self.__pressed_down_color
    def set_press_down_color(self, color : tuple(int,int,int)):
        self.__pressed_down_color = color
        
class Panel(PageEntity):
    
    def __init__(self, entities = []):
        super.__init__()
        self.__background = None # background object
        
    def is_over(self, pos) -> bool:
        pass
    def get_background(self):
        return self.__background
    
class Border(PageEntity):
    
    def __init__(self, width, height, color, thickness = 1):
        super.__init__()
        self.set_height(height)
        self.set_width(width)        
        self.__color = color
        self.__thickness = thickness # by pixel 
        
    def get_color(self) -> tuple(int,int,int):
        return self.__color 
    def set_color(self, color : tuple(int,int,int)):
        self.__color = color
    
    def get_thickness(self) -> int:
        return self.__thickness
    def set_thickness(self, thickness : int):
        self.__thickness = thickness
        
    def form_to_surface(self, surface : pygame.Surface):
        self.set_height(surface.get_height())
        self.set_width(surface.get_width())
        
    def form_to_entity(self, entity : PageEntity):
        self.set_height(entity.get_height())
        self.set_width(entity.get_width())        