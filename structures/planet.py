import pygame

from utils.colors import WHITE
from utils.constants import WIDTH, HEIGHT, FONT_PYGAME
from utils.constants import AU, G, SCALE, TIME_ELAPSED
from math import sqrt, atan2, cos, sin

from structures.star import Star
from structures.structure import Structure


class Planet(Structure):
    """
    Subclass of `Structure`. Represents a planet.
    """
    
    def __init__(self, x=0, y=0, radius=0, mass=0, color=WHITE,
                 initial_velocity_x=0, initial_velocity_y=0, name='New Planet'):
        """
        Initializes a planet object with specified attributes and sets the
        distance to the star as 0.
        
        Parameters
        ----------
        `x`: `float`
            The x-coordinate of the planet's position in astronomical units.
            Defaults to 0.
        `y`: `float`
            The y-coordinate of the planet's position in astronomical units.
            Defaults to 0.
        `radius`: `float`
            The radius of the planet in meters. Defaults to 0.
        `mass`: `float`
            The mass of the planet in kilograms. Defaults to 0.
        `color`: RGB values
            Color value used to specify the color of the planet, represented as
            a tuple of RGB values, where each value ranges from 0 to 255.
            Defaults to white.
        `initial_velocity_x`: `float`
            The initial velocity in the x-direction of the planet in meters per
            second. Defaults to 0.
            0.
        `initial_velocity_y`: `float`
            The initial velocity in the y-direction of the planet in meters per
            second. Defaults to 0.
            0.
        `name`: `str`
            The name of the planet for visualization purposes. Defaults to
            'New Planet'.
            
        """
        
        super().__init__(x=x, y=y, radius=radius, mass=mass, color=color,
                         initial_velocity_x=initial_velocity_x,
                         initial_velocity_y=initial_velocity_y,
                         name=name)
        
        self.distance_to_star = 0


    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def draw(self, window):
        """
        Draw a circle on a window at a specific position and with a specific
        radius and color that represents the planet.

        This also draws the orbit of the planet.

        Parameters
        ----------
        `window`: `Surface`
            pygame window surface on which all will be drawn
            
        """

        # Select font of text in the window
        pygame.init()
        FONT = pygame.font.SysFont(FONT_PYGAME, 16)

        # Change (0,0) position to the center of the screen
        x = self.x * SCALE + WIDTH / 2
        y = self.y * SCALE + HEIGHT / 2

        # Update this planet's orbit points on the window 
        updated_points = []
    
        # If the orbit exists
        if len(self.orbit) > 2:
            # For each point in the orbit
            for point in self.orbit:
                i, j = point
                # Change (0,0) position to the center of the screen
                i = i * SCALE + WIDTH / 2
                j = j * SCALE + HEIGHT / 2

                # Append the point in the orbit to updated points
                updated_points.append((i,j))
                
            # Draw the points on the window
            pygame.draw.lines(surface=window, color=self.color, closed=False, points=updated_points, width=2)
        
        # Draw a circle that represents the object within the window, with a
        # certain color, at a certain site, with a certain radius
        scale = 15
        pygame.draw.circle(window, self.color, (x,y), self.radius * scale)

        # Add the text to represent what planet it is and how far it is from the
        # center star
        
        # Distance from star
        distance_text = f'{round(self.distance_to_star/AU, 3)} AU'
        distance_text = FONT.render(distance_text, 1, WHITE)
        # Position of text "distance from star"
        window.blit(distance_text, (x-distance_text.get_width()/2, y+distance_text.get_height()))

        # Name of planet
        name_text = FONT.render(self.name, 1, WHITE)
        # Position of text "name of planet"
        window.blit(name_text, (x-name_text.get_width()/2, y-2*name_text.get_height()))


    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def actingForce(self, other):
        """
        Find the force another object produces on this object. This applies the
        formula
            F = G * m1 * m2 / d^2
        to the two bodies.

        Parameters
        ----------
        `other`: `Structure`
            Another `Structure` object.

        Returns
        -------
        `float`, `float`
            The force on x- and y-axis exerted on this object.
        
        """

        # Distance in x and y between the two objects
        dx = other.x - self.x
        dy = other.y - self.y
        # Total distance between two bodies
        d = sqrt(dx**2 + dy**2)

        force = G * self.mass * other.mass / d**2

        # Find the angle between the objects and the x-axis
        theta = atan2(dy, dx)

        # Find the force on each axis
        force_x = force * cos(theta)
        force_y = force * sin(theta)

        # For visualization purposes, keep track of the distance of the planet
        # the star it revolves around
        if isinstance(other, Star):
            self.distance_to_star = d

        return force_x, force_y