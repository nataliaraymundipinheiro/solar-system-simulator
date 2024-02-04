import pygame

from utils import colors
from utils.constants import WIDTH, HEIGHT, FONT_PYGAME
from utils.constants import AU, G, SCALE, TIMESTEP
from math import sqrt, atan2, cos, sin

from structures.star import Star
from structures.structure import Structure


class Planet(Structure):
    def __init__(self, x, y, radius, color, mass, name='New Planet', initial_velocity_x=0, initial_velocity_y=0) -> None:
        super().__init__(x, y, radius, color, mass, initial_velocity_x=initial_velocity_x, initial_velocity_y=initial_velocity_y)
        
        self.name = name
        self.distance_to_star = 0


    def draw(self, window):
        pygame.init()
        FONT = pygame.font.SysFont(FONT_PYGAME, 16)

        x = self.x * SCALE + WIDTH / 2
        y = self.y * SCALE + HEIGHT / 2

        updated_points = []
    
        if len(self.orbit) > 2:
            for point in self.orbit:
                x2, y2 = point
                x2 = x2 * SCALE + WIDTH / 2
                y2 = y2 * SCALE + HEIGHT / 2
                updated_points.append((x2,y2))
                
            pygame.draw.lines(surface=window, color=self.color, closed=False, points=updated_points, width=2)
        
        pygame.draw.circle(window, self.color, (x,y), self.radius)

        distance_text = f'{round(self.distance_to_star/AU, 3)} AU'
        distance_text = FONT.render(distance_text, 1, colors.WHITE)
        window.blit(distance_text, (x-distance_text.get_width()/2, y+distance_text.get_height()))

        name_text = FONT.render(self.name, 1, colors.WHITE)
        window.blit(name_text, (x-name_text.get_width()/2, y-2*name_text.get_height()))


    def actingForce(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        d = sqrt(dx**2 + dy**2)

        if isinstance(other, Star):
            self.distance_to_star = d

        theta = atan2(dy, dx) # Angle of star with respect to x axis
        force = G * self.mass * other.mass / d**2
        force_x = cos(theta) * force
        force_y = sin(theta) * force

        return force_x, force_y
    

    def updatePosition(self, structures):
        net_force_x = net_force_y = 0
        
        for structure in structures:
            if self == structure:
                continue
                
            force_x, force_y = self.actingForce(structure)
            net_force_x += force_x
            net_force_y += force_y

        # F = m * a = m * dv / dt
        # v += dv = F / m * dt
        self.velocity_x += net_force_x / self.mass * TIMESTEP
        self.velocity_y += net_force_y / self.mass * TIMESTEP

        # Update position
        self.x += self.velocity_x * TIMESTEP
        self.y += self.velocity_y * TIMESTEP

        # Add point in orbit
        self.orbit.append((self.x, self.y))
