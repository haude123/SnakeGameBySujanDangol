# game.py

import pygame
import os
from config import *
from snake import Snake
from food import Food


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake By SUJAN")

        self.snake = Snake(45, 55)
        self.food = Food()
        self.score = 0
        self.highscore = self.load_highscore()
        self.game_over = False

        self.bg_image = pygame.image.load(SCREEN_FOLDER + "bg2.jpg")
        self.intro_image = pygame.image.load(SCREEN_FOLDER + "intro1.png")
        self.outro_image = pygame.image.load(SCREEN_FOLDER + "outro.png")
        self.font = pygame.font.SysFont('Harrington', 35)
        self.clock = pygame.time.Clock()

    def load_highscore(self):
        if not os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, "w") as f:
                f.write("0")
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read())

    def save_highscore(self):
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(self.highscore))

    def text_screen(self, text, color, x, y):
        screen_text = self.font.render(text, True, color)
        self.window.blit(screen_text, [x, y])

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake.change_direction(INIT_VELOCITY, 0)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(-INIT_VELOCITY, 0)
                elif event.key == pygame.K_UP:
                    self.snake.change_direction(0, -INIT_VELOCITY)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(0, INIT_VELOCITY)
                elif event.key == pygame.K_q:
                    self.score += 10
        return False

    def check_collision(self):
        if abs(self.snake.x - self.food.x) < 12 and abs(self.snake.y - self.food.y) < 12:
            self.score += 10
            self.food.spawn()
            self.snake.length += 5
            if self.score > self.highscore:
                self.highscore = self.score

        if self.snake.check_collision() or self.snake.x < 0 or self.snake.x > SCREEN_WIDTH or self.snake.y < 0 or self.snake.y > SCREEN_HEIGHT:
            self.game_over = True
            pygame.mixer.music.load(MUSIC_FOLDER + 'bgm1.mp3')
            pygame.mixer.music.play(-1)

    def welcome_screen(self):
        while True:
            self.window.blit(self.intro_image, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    pygame.mixer.music.load(MUSIC_FOLDER + 'bgm.mp3')
                    pygame.mixer.music.play(-1)
                    return False
            pygame.display.update()
            self.clock.tick(FPS)

    def game_loop(self):
        while not self.game_over:
            if self.handle_events():
                break

            self.snake.move()
            self.check_collision()

            self.window.blit(self.bg_image, (0, 0))
            self.text_screen(f"Score: {self.score}  Highscore: {self.highscore}", SNAKE_GREEN, 5, 5)
            self.food.draw(self.window)
            self.snake.draw(self.window)

            pygame.display.update()
            self.clock.tick(FPS)

        self.save_highscore()
        self.game_over_screen()

    def game_over_screen(self):
        while True:
            self.window.blit(self.outro_image, (0, 0))
            self.text_screen(f"Score: {self.score}", SNAKE_GREEN, 385, 350)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.reset_game()
                    return
            pygame.display.update()
            self.clock.tick(FPS)

    def reset_game(self):
        self.snake = Snake(45, 55)
        self.food.spawn()
        self.score = 0
        self.game_over = False
        self.game_loop()

    def start(self):
        pygame.mixer.music.load(MUSIC_FOLDER + 'wc.mp3')
        pygame.mixer.music.play(-1)
        if not self.welcome_screen():
            self.game_loop()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.start()
