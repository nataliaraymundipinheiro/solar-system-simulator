from utils import colors

class Structure:
    def __init__(self, x, y, radius, mass, color=colors.WHITE, initial_velocity_x=0, initial_velocity_y=0) -> None:
        self.x = x
        self.y = y
        self.radius = radius # meters
        self.color = color
        self.mass = mass # kilograms
        # Save the points where the structure has traveled along so we can draw
        # a circular orbit representing the orbit of the planet
        self.orbit = []

        self.velocity_x = initial_velocity_x
        self.velocity_y = initial_velocity_y

    
    def draw(self, window):
        pass


    def actingForce(self, other):
        pass


    def updatePosition(self, structures):
        pass