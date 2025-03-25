import pygame
import objs


class Main:
    def __init__(self, parent):
        pygame.init()
        
        self.parent = parent
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space")
                    self.parent.audio()
                if event.key == pygame.K_n:
                    self.parent.process.new("id")

    def run(self):
        while self.running:
            self.draw()
            self.events()
            self.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

        for obj in self.parent.objs:
            obj.draw()

        pygame.display.flip()

    def update(self):
        for obj in self.parent.objs:
            obj.update()
