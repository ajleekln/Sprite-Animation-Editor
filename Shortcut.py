class Shortcut:
    def __init__(self, keys : list, action):
        self.__action = action
        self.__keys = keys
        self.__enable = True
        
    def is_enabled(self) -> bool:
        return self.__enable
    def enable(self):
        self.__enable = True
    def disable(self):
        self.__enable = False
        
    def set_keys(self, keys):
        self.__keys = keys
    
    def keys_match(self, keys : list):
        for key in keys:
            if key not in self.__keys:
                return False
        return True
    
    def activate(self) -> object:
        if self.is_enabled():
            self.__action()