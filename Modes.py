from enum import Enum

class Modes(Enum):
    abc = ((97,122), "lower", False)
    lower = ((97,122), "lower", True) 
    upper = ((65, 90), "upper", True)
    all_keys = ((32, 122), "both", True)
    # reverse mode maybe

    def get_name(self):
        return self.name
            
    def get_limits(self):
        limits = self.value[0]
        return limits
    
    def get_mode_type(self):
        mode_type = self.value[1]
        return mode_type

    def should_shuffle(self):
        return self.value[2]
