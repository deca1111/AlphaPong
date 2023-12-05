from typing import Tuple

import pygame


class PlayerPong:
    """
    Classe représentant un joueur de pong (une raquette)
    """

    def __init__(
            self, x: float, y: float, width: float, height: float, speed: int, color: Tuple[int, int, int],
            screen: pygame.Surface, name: str = "Bob"
            ):
        """
        Constructeur de la classe PlayerPong
        """
        self.speed = speed
        self.color = color

        self.originalX = x
        self.originalY = y

        # Écran sur lequel afficher la raquette
        self.screen = screen

        # Création de la raquette
        self.rect = pygame.Rect(x, y, width, height)

        # Nom du joueur
        self.name = name

        self.score = 0
        self.hit = 0

        # Police d'écriture
        self.font = pygame.font.SysFont("Arial", 15, bold=True)

    def display(self):
        """
        Affiche la raquette sur l'écran
        """
        pygame.draw.rect(self.screen, self.color, self.rect)

        # Affichage du nom du joueur dans la raquette
        text = self.font.render(self.name, True, (0, 0, 0))
        # Rotation du texte
        angleRotate = 90 if self.rect.x > self.screen.get_width() / 2 else -90
        text = pygame.transform.rotate(text, angleRotate)
        # Affichage du texte
        textRect = text.get_rect()
        textRect.center = (self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2)
        self.screen.blit(text, textRect)

    def move(self, direction: int):
        """
        Déplace la raquette dans une certaine direction
        """
        if direction == 1:
            self.rect.y -= self.speed
        elif direction == -1:
            self.rect.y += self.speed

        # Vérification des bords
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > self.screen.get_height() - self.rect.height:
            self.rect.y = self.screen.get_height() - self.rect.height

    def reset(self):
        """
        Remet la raquette à sa position initiale
        """
        self.rect.x = self.originalX
        self.rect.y = self.originalY
