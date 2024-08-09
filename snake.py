# snake.py

import pygame
from config import BLACK, SNAKE_SIZE


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.length = 1
        self.body = []

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.body.append([self.x, self.y])
        if len(self.body) > self.length:
            del self.body[0]

    def draw(self, window):
        for segment in self.body:
            pygame.draw.rect(window, BLACK, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])

    def check_collision(self):
        if self.body[-1] in self.body[:-1]:
            return True
        return False

    def change_direction(self, x_velocity, y_velocity):
        self.velocity_x = x_velocity
        self.velocity_y = y_velocity
