__author__ = 'William'
import pygame


class Visual:

    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("arial", 15)
        self.screen = pygame.display.set_mode((640, 480))
        self.text = "Graph goes here"
        pygame.display.set_caption("GPX Visualizer")

    def update(self):
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.font.render(self.text, True, (0, 0, 0)), (100, 100))
            pygame.display.update()