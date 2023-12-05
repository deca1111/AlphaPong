import pygame
from pongGame import PongGame


class GameMaster:

    def __init__(self):
        self.game = PongGame()

    def playHumainVsHuman(self):
        # Nommage des joueurs
        self.game.playerGauche.name = "Humain 1"
        self.game.playerDroite.name = "Humain 2"
        running = True
        while running:
            self.game.clock.tick(self.game.FPS)

            keys = pygame.key.get_pressed()

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    print("Fermeture du jeu")
                    running = False
                    break

            # Mouvement des joueurs
            if keys[pygame.K_UP]:
                self.game.mouvementRaquette('D', 1)
            elif keys[pygame.K_DOWN]:
                self.game.mouvementRaquette('D', -1)
            if keys[pygame.K_z]:
                self.game.mouvementRaquette('G', 1)
            elif keys[pygame.K_s]:
                self.game.mouvementRaquette('G', -1)

            self.game.loop()
            self.game.draw()

        pygame.quit()

    def playHumanVsIa(self):
        # Nommage du joueur et de l'IA
        self.game.playerGauche.name = "Humain"
        self.game.playerDroite.name = "IA"

        running = True
        while running:
            self.game.clock.tick(self.game.FPS)

            keys = pygame.key.get_pressed()

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    print("Fermeture du jeu")
                    running = False
                    break

            # Mouvement du joueur humain
            if keys[pygame.K_UP] or keys[pygame.K_z]:
                self.game.mouvementRaquette('G', 1)
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.game.mouvementRaquette('G', -1)

            self.game.loop()
            self.game.draw()

        pygame.quit()

    def playIaVsIa(self, fpsMax: int = 60):
        running = True
        while running:
            self.game.clock.tick(fpsMax)
            keys = pygame.key.get_pressed()

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    print("Fermeture du jeu")
                    running = False
                    break

            self.game.loop()
            self.game.draw()

        pygame.quit()


if __name__ == '__main__':
    """
    Fonction principale du programme
    
    Elle permet de lancer un cycle d'entrainement et de test.
    Elle permet aussi de lancer un test contre un joueur humain.
    """

    master = GameMaster()
    master.playHumanVsIa()
