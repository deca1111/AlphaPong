import math
import random
from typing import Tuple
import pygame


class BallPong:
    """
    Classe représentant une balle de pong
    """

    def __init__(self, x, y, radius: int, color: Tuple[int, int, int], screen: pygame.Surface):
        """
        Constructeur de la classe ballPong
        """
        self.MaxVel = 7
        self.color = color

        self.x = self.originalX = x
        self.y = self.originalY = y
        self.radius = radius

        angle = self._get_random_angle(-30, 30, [0])
        pos = 1 if random.random() < 0.5 else -1

        self.velX = pos * abs(math.cos(angle) * self.MaxVel)
        self.velY = math.sin(angle) * self.MaxVel

        # Écran sur lequel afficher la balle
        self.screen = screen

    def _get_random_angle(self, min_angle, max_angle, excluded):
        angle = 0
        while angle in excluded:
            angle = math.radians(random.randrange(min_angle, max_angle))

        return angle

    def display(self):
        """
        Affiche la balle sur l'écran
        """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        """
        Déplace la balle dans selon sa vitesse
        """
        self.x += self.velX
        self.y += self.velY

    def reset(self):
        """
        Remet la balle à sa position initiale
        """
        self.x = self.originalX
        self.y = self.originalY

        angle = self._get_random_angle(-30, 30, [0])
        y_vel = math.sin(angle) * self.MaxVel

        self.velX *= -1
        self.velY = y_vel
