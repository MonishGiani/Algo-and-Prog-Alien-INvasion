import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.topleft = (self.rect.width, self.rect.height)

        # Store the alien's exact position as float for smoother movement.
        self.x_position = float(self.rect.x)

    def draw(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def is_at_edge(self):
        """Return True if the alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def update(self):
        """Move the alien right or left."""
        self.x_position += (self.settings.alien_speed_factor *
                            self.settings.fleet_direction)
        self.rect.x = round(self.x_position)  # Update rect's x-coordinate
