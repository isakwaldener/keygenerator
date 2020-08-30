from enum import Enum

class Modes(Enum):
    abc = ((97,122), False)
    lower = ((97,122), True) 
    upper = ((65, 90), True)
    # reverse mode maybe

    def get_name(self):
        return self.name
            
    def get_limits(self):
        limits = self.value[0]
        return limits

    def should_shuffle(self):
        return self.value[1]
