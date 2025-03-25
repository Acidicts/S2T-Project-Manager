import pygame


class Obj:
    def __init__(self, parent, x, y, w, h):
        self.parent = parent
        self.rect = pygame.Rect(x, y, w, h)
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
        self.color = (255, 255, 255)
        self.surface.fill(self.color)

        self.id = len(self.parent.parent.objs)

    def draw(self):
        self.surface.fill(self.color)
        self.parent.screen.blit(self.surface, self.rect.center)

    def update(self):
        pass
