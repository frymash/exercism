import string
import random

class Robot:

    def __init__(self):
        self.name = None
        self.generate_name() # Generate a name for the robot during initialization

    def generate_name(self):
        alpha = ''.join(random.choices(list(string.ascii_uppercase),k=2))
        numStr = ''.join(str(random.randrange(0,9,1)) for i in range(3))
        self.name = alpha + numStr
        return self.name

    def reset(self):
        # 'Ensure every existing robot has a unique name.''
        # w3schools: 'By default the random number generator uses the current system time.'
        random.seed()
        self.generate_name()
