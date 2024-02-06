from utils.colors import WHITE
from utils.constants import AU, EARTH_RADIUS, TIME_ELAPSED


class Structure:
    def __init__(self, x=0, y=0, radius=0, mass=0, color=WHITE,
                 initial_velocity_x=0, initial_velocity_y=0,
                 name='New Structure'):
        """
        Initializes a structure object with specified attributes.
        
        Parameters
        ----------
        `x`: `float`
            The x-coordinate of the structure's position in astronomical units.
            Defaults to 0.
        `y`: `float`
            The y-coordinate of the structure's position in astronomical units.
            Defaults to 0.
        `radius`: `float`
            The radius of the structure in meters. Defaults to 0.
        `mass`: `float`
            The mass of the structure in kilograms. Defaults to 0.
        `color`: RGB values
            Color value used to specify the color of the structure, represented
            as a tuple of RGB values, where each value ranges from 0 to 255.
            Defaults to white.
        `initial_velocity_x`: `float`
            The initial velocity in the x-direction of the structure in meters
            per second. Defaults to 0.
        `initial_velocity_y`: `float`
            The initial velocity in the y-direction of the structure in meters
            per second. Defaults to 0.
        `name`: `str`
            The name of the structure for visualization purposes. Defaults to
            'New Structure'.
            
        """

        # Position of the structure in the window in pixels
        self.x = x
        self.y = y

        # Radius of structure input in meters and converted to a percentage of
        # Earth's size
        self.radius = radius / EARTH_RADIUS
        
        # Color of structure
        self.color = color

        # Mass of structure in kilograms
        self.mass = mass
        
        # Save the points where the structure has been to so we can draw an
        # elliptical orbit
        self.orbit = []

        # Initial velocity of the structure in meters per second
        self.velocity_x = initial_velocity_x
        self.velocity_y = initial_velocity_y

        # Name of object for visualization purposes
        self.name = name


    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    def draw(self, window):
        pass


    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  

    def actingForce(self, other):
        pass


    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def updatePosition(self, structures):
        """
        Updates the position of a structure based on the net force acting on it
        and its velocity.
        
        Parameters
        ----------
        `structures`: `list`
            List of `Structure`s representing the structures in the system.
            
        """

        # Find the net force on x- and y-axis with respect to this structure
        # Start with zeros and keep incrementing/decrementing
        net_force_x = net_force_y = 0

        # For each object on our system
        for structure in structures:
            # The object itself doesn't exert any force on itself
            if self == structure:
                continue

            # Find interaction force between this and the other structure
            force_x, force_y = self.actingForce(structure)

            # Update net force on the axes
            net_force_x += force_x
            net_force_y += force_y

        # Now that we have the net force on both x- and y-axis on this structure,
        # update the structure's velocity
        self.velocity_x += net_force_x / self.mass * TIME_ELAPSED
        self.velocity_y += net_force_y / self.mass * TIME_ELAPSED

        # Update the structure's position given its velocity after a time
        # `TIME_ELAPSED` has passed
        self.x += self.velocity_x * TIME_ELAPSED
        self.y += self.velocity_y * TIME_ELAPSED

        # Add new point to the orbit
        self.orbit.append((self.x, self.y))