# Movement

class Movement(object):
    """
    A class in which incorperates movement for pygame sprites
    
    ...
    
    Attributes
    ----------
    pos : tuple(int, int)
        an xy position 
    speed_x : float 
        a x-axis rate of change (speed in x direction)
    speed_y : float
        a y-axis rate of change (speed in y direction)
    accel_x : float
        a rate of change in speed (acceleration in the x direction)
    accel_y : float
        a rate of change in speed (acceleration in the y direction)
        
    Methods
    -------
    move(new_pos)
        changes the position to the new position 
    stop()
        sets speed and acceleration to zero 
    get_speed_x()
        returns the speed in the x direction value
    get_speed_y()
        returns the speed in the y direction value
    get_accel_x()
        returns the acceleration in the x direction
    get_accel_y()
        returns the acceleration in the y direction
    set_speed_x(num)
        sets the speed in the x direction to a new value
    set_speed_y(num)
        sets the speed in the y direction to a new value
    set_accel_x(num)
        sets the acceleration in the x direction to a new value
    set_accel_y(num)
        sets the acceleration int the y direction to a new value
    update()
        updates the speed in accordance to each game frame cycle
    """
    def __init__(self):
        self.__pos = (0, 0)
        self.__speed_x = 0
        self.__speed_y = 0
        self.__accel_x = 0
        self.__accel_y = 0
        
    def move (self, new_pos):
        """
        Sets the position to the new position
        
        Parameters
        ----------
        new_pos : tuple(int, int)
            the new position to be switched to 
        """
        self.__pos = new_pos
        
    def stop (self):
        """
        Sets all speed and acceleration values to zero
        """
        self.__speed_x = 0
        self.__speed_y = 0
        self.__accel_x = 0
        self.__accel_y = 0
    
    def get_speed_x (self):
        """
        Returns the value of the speed in the x direction
        
        Returns
        -------
        float
            the speed in the x direction 
        """
        return self.__speed_x
    def get_speed_y (self):
        """
        Returns the value of the speed in the y direction
        
        Returns
        -------
        float
            the speed in the y direction 
        """        
        return self.__speed_y
    def get_accel_x (self):
        """
        Returns the value of the acceleration in the x direction
        
        Returns
        -------
        float
            the acceleration in the x direction 
        """        
        return self.__accel_x
    def get_accel_y (self):
        """
        Returns the value of the acceleration in the x direction
        
        Returns
        -------
        float
            the acceleration in the x direction 
        """                
        return self.__accel_y
    def get_pos (self):
        """
        Returns the value of the position 
        
        Returns
        -------
        tuple(int, int) 
            the xy position 
        """                
        return self.__pos
    
    def set_speed_x (self, num : float):
        """
        Sets the speed in the x direction
        
        Parameters
        ----------
        num : float
            the speed in the x direction
        """
        self.__speed_x = num
    def set_speed_y (self, num : float):
        """
        Sets the speed in the y direction
        
        Parameters
        ----------
        num : float
            the speed in the y direction
        """        
        self.__speed_y = num
    def set_accel_x (self, num : float):
        """
        Sets the acceleration in the x direction
        
        Parameters
        ----------
        num : float
            the acceleration in the x direction
        """            
        self.__accel_x = num
    def set_accel_y (self, num : float):
        """
        Sets the acceleration in the y direction
        
        Parameters
        ----------
        num : float
            the acceleration in the y direction
        """        
        self.__accel_y = num    
    
    def update (self):
        """
        Updates the speed and acceleration
        """
        new_pos = (self.get_pos()[0] + self.__speed_x, self.get_pos()[1] + self.__speed_y)
        self.move( new_pos )
        
        self.__speed_x += self.__accel_x
        self.__speed_y += self.__accel_y
    