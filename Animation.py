import pygame
from Image import Image
from Movement import Movement 


class FrameProperty:
    
    def __init__(self, image : Image, time : float):
        self.__image = image
        self.__time = time
        self.movement = Movement()
        
    def set_image(self, image : Image):
        self.__image = image
    def get_image(self) -> Image:
        return self.__image
    
    def set_time(self, time : float):
        self.__time = time
    def get_time(self) -> float:
        return time
    
class Animation:
    
    def __init__(self, frame_properties = []): 
        self.__frames = image_animation_properties
        self.__slight_pause = 0
        self.__counter = 0 
        self.__animation_completed = False
        
    def run(self) -> pygame.Surface:
        pass
    
    def add_frame(self, image : Image, time : float): 
        self.__frames.append(FrameProperty(image, time))
    def add_frame(self, frame : FrameProperty):
        self.__frames.append(frame)
    def add_frame_at(index : int, image : Image, time : float, ):
        self.__frames.insert(index, FrameProperty(image, time) )
    def add_frame_at(index : int, frame : FrameProperty):
        self.__frames.insert(index, frame)
        
    def remove_frame(self, frame: FrameProperty):
        self.__frames.remove(frame)
    def remove_frame_by_image(self, image: Image):
        # removes first occurence of image
        for frame in self.__frames:
            frame_image = frame.get_image()
            
            if frame_image == image:
                self.__frames.remove(frame)
                return 
        # raise error if not found
    def get_frame_at(self , index : int):
        return self.__frames[index]
    def get_frames(self):
        return self.__frames
    
    def total_time(self):
        total_time = 0
        for frame in self.__frames:
            total_time += frame.get_time() 
        return total_time