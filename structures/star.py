import pygame

from constants import WIDTH, HEIGHT
from constants import SCALE
from math import sqrt, atan2, cos, sin

from structures.structure import Structure


class Star(Structure):
    def __init__(self, x, y, radius, color, mass, name='New Star') -> None:
        super().__init__(x, y, radius, color, mass)
        
        self.name = name

    
    def draw(self, window):
        x = self.x * SCALE + WIDTH / 2
        y = self.y * SCALE + HEIGHT / 2

        pygame.draw.circle(window, self.color, (x,y), self.radius)


    def actingForce(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        d = sqrt(dx**2 + dy**2)

        theta = atan2(dy, dx) # Angle of star with respect to x axis
        force = self.G * self.mass * other.mass / d**2
        force_x = cos(theta) * force
        force_y = sin(theta) * force

        return force_x, force_y
    

    def updatePosition(self, structures):
        # nothing happens to stars... yet
        pass