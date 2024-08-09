# food.py

import pygame
import random
from config import RED, SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE


class Food:
    def __init__(self):
        self.x = random.randint(20, SCREEN_WIDTH // 2)
        self.y = random.randint(20, SCREEN_HEIGHT // 2)

    def spawn(self):
        self.x = random.randint(20, SCREEN_WIDTH // 2)
        self.y = random.randint(20, SCREEN_HEIGHT // 2)

    def draw(self, window):
        pygame.draw.rect(window, RED, [self.x, self.y, SNAKE_SIZE, SNAKE_SIZE])
