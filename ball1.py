import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, y, speed, surf, score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(1000, y))
        self.speed = speed
        self.score = score
        self.add(group)

    def update(self, *args):
        if self.rect.x < args[0]:
            self.rect.x -= self.speed
        else:
            self.kill()