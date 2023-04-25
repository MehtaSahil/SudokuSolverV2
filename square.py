
class Square:
    def __init__(self, xpos: int, ypos: int, value: int = None): 
        # 1 means that (index+1) is an available option
        self.options = [1] * 9
        self.xpos = xpos
        self.ypos = ypos

        # None means that no value has been set
        self.value = value

        if value is not None:
            self.value = value
        else:
            self.value = None
    
    def getOptions(self) -> list[int]:
        return self.options

    def isSet(self) -> bool:
        return (self.value is not None)
    
    def get(self) -> int:
        return self.value
    
    def set(self, new_value) -> None:
        self.value = new_value
    
    def reset(self) -> None:
        self.value = None
    
    def allowOption(self, value) -> None:
        index = value - 1
        self.options[index] = 1
    
    def disallowOption(self, value) -> None:
        index = value - 1
        self.options[index] = 0