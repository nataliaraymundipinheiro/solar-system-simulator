import pygame

from utils import colors
from utils.constants import WIDTH, HEIGHT
from utils.constants import AU

from structures.planet import Planet
from structures.star import Star


pygame.init()
# Take in coordinates for the size of our window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # pygame surface
# Window caption
pygame.display.set_caption("Star System Simulation")


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def createStructures():
    # Stars
    sun = Star(x=0,
               y=0,
               radius=696.34e6,
               color=colors.YELLOW,
               mass=1.989e30,
               name='Sun')
    
    # Planets
    mercury = Planet(x=-0.387*AU,
                     y=0,
                     radius=2.4397e6,
                     color=colors.GREY,
                     mass=3.30104e23,
                     name='Mercury',
                     initial_velocity_y=47.9e3)
    
    venus   = Planet(x=-0.72*AU,
                     y=0, 
                     radius=6.0518e6,
                     color=colors.ORANGE,
                     mass=4.867e24,
                     name='Venus',
                     initial_velocity_y=35.0e3)
    
    earth   = Planet(x=-1*AU,
                     y=0,
                     radius=6.371e6,
                     color=colors.BLUE,
                     mass=5.972e24,
                     name='Earth',
                     initial_velocity_y=29.8e3)
    
    mars    = Planet(x=-1.449*AU,
                     y=0,
                     radius=3.3895e6,
                     color=colors.RED,
                     mass=6.39e23,
                     name='Mars',
                     initial_velocity_y=24.1e3)

    return [sun, mercury, venus, earth, mars]


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def run_simulation():
    run = True
    # Run simulation at the same speed independent of computer, regulating
    # frame rate
    clock = pygame.time.Clock()

    structures = createStructures()

    while run:
        # Maximum fps: 60
        clock.tick(60)
        # Fill screen with white
        WINDOW.fill(colors.BLACK)

        # Get the different events that are occurring in pygame
        # The only event I handle is when the user presses 'X' to exit the
        # window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False # Exit the window
        
        # Draw the structures
        for structure in structures:
            structure.updatePosition(structures)
            structure.draw(WINDOW)

        # Update display
        pygame.display.update()


    # Quit pygame
    pygame.quit()


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
def main():
    run_simulation()


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
if __name__ == "__main__":
    main()

