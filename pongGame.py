import pygame

from ballPong import BallPong
from playerPong import PlayerPong


class PongGame:

    def __init__(self, width: int = 1000, height: int = 600, fps: int = 60):
        """
        Constructeur de la classe pongGame
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = fps

        # Création de la fenêtre
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pong")

        # Couleurs
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.GREY = (128, 128, 128)

        # Polices d'écriture
        self.fontFPS = pygame.font.SysFont("Arial", 15)
        self.fontScore = pygame.font.SysFont("Arial", 30, bold=True)
        self.fontHit = pygame.font.SysFont("Arial", 20, bold=True)

        # Création des joueurs
        self.playerHeight = height / 5
        self.playerWidth = 20
        self.playerSpeed = 5
        self.playerGauche = PlayerPong(10, (self.HEIGHT / 2) - (self.playerHeight / 2), self.playerWidth,
                                       self.playerHeight, self.playerSpeed, self.WHITE, self.screen, "Gauche")
        self.playerDroite = PlayerPong(self.WIDTH - self.playerWidth - 10, (self.HEIGHT / 2) - (self.playerHeight / 2),
                                       self.playerWidth, self.playerHeight, self.playerSpeed, self.WHITE, self.screen,
                                       "Droite")
        self.players = [self.playerGauche, self.playerDroite]

        # Création de la balle
        self.ballRadius = 10
        self.ball = BallPong(self.WIDTH / 2, self.HEIGHT / 2, self.ballRadius, self.WHITE, self.screen)

    def loop(self):
        """
        Exécute la boucle principale du jeu
        """

        self.ball.move()
        self.gestionCollision()

    def draw(self, drawScore: bool = True, drawFPS: bool = True, drawHit: bool = True):
        """
        Dessine les éléments du jeu
        """
        self.screen.fill(self.BLACK)

        if drawFPS:
            self.displayFPS()

        # Affichage des joueurs
        for player in self.players:
            player.display()

        # Affichage de la balle
        self.ball.display()

        # Dessin du filet
        pygame.draw.line(self.screen, self.WHITE, (self.WIDTH / 2, 0), (self.WIDTH / 2, self.HEIGHT), 2)

        # Affichage des scores
        if drawScore:
            scoreGauche = self.fontScore.render(str(self.playerGauche.score), True, self.WHITE)
            textGaucheRect = scoreGauche.get_rect()
            textGaucheRect.center = (self.WIDTH / 2 - 30, 15)
            scoreDroite = self.fontScore.render(str(self.playerDroite.score), True, self.WHITE)
            textDroiteRect = scoreDroite.get_rect()
            textDroiteRect.center = (self.WIDTH / 2 + 30, 15)

            self.screen.blit(scoreGauche, textGaucheRect)
            self.screen.blit(scoreDroite, textDroiteRect)

        # Affichage des hits
        if drawHit:
            hitGauche = self.fontHit.render(str(self.playerGauche.hit), True, self.GREY)
            textGaucheRect = hitGauche.get_rect()
            textGaucheRect.center = (self.WIDTH / 2 - 30, 50)
            hitDroite = self.fontHit.render(str(self.playerDroite.hit), True, self.GREY)
            textDroiteRect = hitDroite.get_rect()
            textDroiteRect.center = (self.WIDTH / 2 + 30, 50)

            self.screen.blit(hitGauche, textGaucheRect)
            self.screen.blit(hitDroite, textDroiteRect)

        # Update de l'écran
        pygame.display.update()

    def mouvementRaquette(self, player: chr, direction) -> bool:
        """
        Déplace la raquette du joueur dans une certaine direction

        :param player: 'G' pour le joueur de gauche, 'D' pour le joueur de droite
        :param direction: 1 pour monter, -1 pour descendre
        :return: True si le mouvement est possible, False sinon
        """
        # Mouvement du joueur de gauche
        if player == 'G':
            if (
                    (direction == 1 and self.playerGauche.rect.y - self.playerSpeed >= 0) or
                    (direction == -1 and self.playerGauche.rect.y + self.playerHeight + self.playerSpeed <= self.HEIGHT)
            ):
                self.playerGauche.move(direction)
            else:
                return False

        # Mouvement du joueur de droite
        elif player == 'D':
            if (
                    (direction == 1 and self.playerDroite.rect.y - self.playerSpeed >= 0) or
                    (direction == -1 and self.playerDroite.rect.y + self.playerHeight + self.playerSpeed <= self.HEIGHT)
            ):
                self.playerDroite.move(direction)
            else:
                return False

        return True

    def gestionCollision(self):
        """
        Gère les collisions entre les joueurs et la balle
        """
        # Collision avec les joueurs
        # Joueur de gauche
        if self.ball.x - self.ball.radius <= self.playerGauche.rect.x + self.playerWidth:
            if self.playerGauche.rect.y <= self.ball.y <= self.playerGauche.rect.y + self.playerHeight:
                # Axe des ordonnées
                self.ball.velX *= -1
                # Axe des abscisses
                self.ball.velY = (self.ball.y - (self.playerGauche.rect.y + self.playerHeight / 2)) / (
                        self.playerHeight / 2) * self.ball.MaxVel
                self.playerGauche.hit += 1

        # Joueur de droite
        if self.ball.x + self.ball.radius >= self.playerDroite.rect.x:
            if self.playerDroite.rect.y <= self.ball.y <= self.playerDroite.rect.y + self.playerHeight:
                # Axe des ordonnées
                self.ball.velX *= -1
                # Axe des abscisses
                self.ball.velY = (self.ball.y - (self.playerDroite.rect.y + self.playerHeight / 2)) / (
                        self.playerHeight / 2) * self.ball.MaxVel
                self.playerDroite.hit += 1

        # Collision avec les bords (haut et bas)
        if self.ball.y - self.ball.radius <= 0 or self.ball.y + self.ball.radius >= self.HEIGHT:
            self.ball.velY *= -1

        # Collision avec les bords (gauche et droite)
        if self.ball.x - self.ball.radius <= 0:
            self.playerDroite.score += 1
            self.resetManche()
        elif self.ball.x + self.ball.radius >= self.WIDTH:
            self.playerGauche.score += 1
            self.resetManche()

    def displayFPS(self):
        """
        Affiche le nombre de FPS dans le coin supérieur droit
        """
        fps = str(int(self.clock.get_fps()))
        fps = self.fontFPS.render(fps, True, self.GREEN)
        self.screen.blit(fps, (self.WIDTH - 20, 0))

    def resetManche(self):
        """
        Reset le jeu au début d'une manche
        """
        self.playerGauche.reset()
        self.playerDroite.reset()
        self.ball.reset()

    def resetGame(self):
        """
        Reset le jeu au début d'une partie
        """
        self.playerGauche.score = 0
        self.playerDroite.score = 0
        self.playerGauche.hit = 0
        self.playerDroite.hit = 0
        self.resetManche()
