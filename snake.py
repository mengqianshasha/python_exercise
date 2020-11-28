import pygame
import random


class SnakeNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Direction:
    Up = 0
    Down = 1
    Left = 2
    Right = 3


class Color:
    Black = (0, 0, 0)
    Blue = (50, 153, 213)
    Yellow = (255, 255, 102)
    Green = (0, 255, 0)
    Red = (213, 50, 80)


class Snake:
    def __init__(self, startX, startY):
        self.body = [SnakeNode(startX, startY)]
        self.currentX = startX
        self.currentY = startY
        self.length = 1
        self.direction = random.randint(0, 3)

    def move(self, block_size):
        if self.direction == Direction.Up:
            self.move_up(block_size)
        elif self.direction == Direction.Down:
            self.move_down(block_size)
        elif self.direction == Direction.Left:
            self.move_left(block_size)
        else:
            self.move_right(block_size)

    def move_up(self, block_size):
        pass

    def move_down(self, block_size):
        pass

    def move_left(self, block_size):
        pass

    def move_right(self, block_size):
        pass

    def change_direction(self, direction):
        self.direction = direction

    def hit_himself(self):
        pass

    def __move_body__(self):
        pass


class Food:
    def __init__(self, initialX, initialY):
        self.x = initialX
        self.y = initialY

    def update_location(self, x, y):
        self.x = x
        self.y = y


class Game:
    def __init__(self):
        pygame.init()
        self.dis_width = 800
        self.dis_height = 600

        self.surface = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Snake game by Tubaobao')
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.game_lose = False
        self.food = None
        self.score = 0
        self.block_size = 10
        self.move_speed = 3
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 25)
        self.snake = None
        self.game_loop()

    def show_speed(self):
        value = self.score_font.render("Your Speed (3-15): " + str(self.move_speed), True, Color.Yellow)
        self.surface.blit(value, [540, 0])

    def show_score(self):
        value = self.score_font.render("Your Score: " + str(self.score), True, Color.Yellow)
        self.surface.blit(value, [20, 0])

    def message(self, msg, color):
        msg = self.font_style.render(msg, True, color)
        self.surface.blit(msg, [self.dis_width / 6, self.dis_height / 3])

    def game_loop(self):
        self.score = 0
        self.game_over = False
        self.game_lose = False
        self.snake = Snake(self.dis_width/2, self.dis_height/2)
        self.food = Food(round(random.randrange(0, self.dis_width - self.block_size) / 10.0) * 10.0, round(random.randrange(0, self.dis_height - self.block_size) / 10.0) * 10.0)
        while not self.game_over:
            while self.game_lose:
                self.surface.fill(Color.Blue)
                self.message("You Lost! Press C-Play Again or Q-Quit", Color.Red)
                self.show_score()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                        if event.key == pygame.K_c:
                            self.game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.change_direction(Direction.Left)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(Direction.Right)
                    elif event.key == pygame.K_UP:
                        self.snake.change_direction(Direction.Up)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(Direction.Down)
                    elif event.key == pygame.K_w:
                        self.add_speed()
                    elif event.key == pygame.K_s:
                        self.reduce_speed()

            self.surface.fill(Color.Blue)
            self.snake.move(self.block_size)
            self.eat_food()

            if self.snake_hit_himself() or self.snake_hit_wall():
                self.game_lose = True

            self.draw_snake()
            self.draw_food()
            self.show_score()
            self.show_speed()

            pygame.display.update()
            self.clock.tick(self.move_speed)
        pygame.quit()
        quit()

    def add_speed(self):
        if self.move_speed < 15:
            self.move_speed += 1

    def reduce_speed(self):
        if self.move_speed > 3:
            self.move_speed -= 1

    def eat_food(self):
        pass

    def snake_hit_wall(self):
        pass

    def snake_hit_himself(self):
        return self.snake.hit_himself()

    def draw_snake(self):
        for node in self.snake.body:
            pygame.draw.rect(self.surface, Color.Black, [node.x, node.y, self.block_size, self.block_size])

    def draw_food(self):
        pygame.draw.rect(self.surface, Color.Green, [self.food.x, self.food.y, self.block_size, self.block_size])


if __name__ == "__main__":
    game = Game()