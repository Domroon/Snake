import pygame
import random


class Square:
    def __init__(self, x, y, square_lengths):
        self.x = x
        self.y = y
        self.width = square_lengths
        self.height = square_lengths
        self.color = (255, 0, 0)

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))


class Head(Square):
    def __init__(self, x, y, square_lengths):
        super().__init__(x, y, square_lengths)
        self.last_position = {'x': 0, 'y': 0}
        self.body_squares = []

    def make_step(self, x_step, y_step):
        self.x += x_step * self.width
        self.y += y_step * self.height

    def save_position(self):
        self.last_position['x'] = self.x
        self.last_position['y'] = self.y


class Body(Square):
    def __init__(self, x, y, square_length):
        super().__init__(x, y, square_length)


class Food(Square):
    def __init__(self, x, y, square_lengths):
        super().__init__(x, y, square_lengths)
        self.color = (255, 255, 0)


def redraw(snake_head, snake_body_list, food_list, window):
    window.fill((0, 0, 0))
    snake_head.draw(window)
    for food in food_list:
        food.draw(window)
    pygame.display.update()


def check_screen_border(square, screen_width, screen_height, square_lengths):
    top_screen_y = 0
    bottom_screen_y = screen_height - square_lengths
    right_screen_x = screen_width - square_lengths
    left_screen_x = 0

    if square.y < top_screen_y:
        square.y = bottom_screen_y
    elif square.y > bottom_screen_y:
        square.y = top_screen_y
    elif square.x < left_screen_x:
        square.x = right_screen_x
    elif square.x > right_screen_x:
        square.x = left_screen_x


def eat_check(head, food_list, square_lengths, screen_width, screen_height):
    for food in food_list:
        if food.x == head.x and food.y == head.y:
            food_list.pop()
            print('The snake has eat the food')
            random_food_position(food_list, square_lengths, screen_width, screen_height)


def random_food_position(food_list, square_lengths, screen_width, screen_height):
    food_x = random.randint(0, round((screen_width - square_lengths) / square_lengths)) * square_lengths
    food_y = random.randint(0, round((screen_height - square_lengths) / square_lengths)) * square_lengths
    food = Food(food_x, food_y, square_lengths)
    food_list.append(food)


def main():
    pygame.init()

    screen_width = 1280
    screen_height = 720

    square_lengths = 20

    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()

    head = Head(0, 0, square_lengths)
    direction = 'right'

    snake_body_list = []

    food_list = []
    # for testing
    random_food_position(food_list, square_lengths, screen_width, screen_height)

    run = True
    game_speed = 8
    while run:
        clock.tick(game_speed)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print('UP')
            direction = 'up'
        elif keys[pygame.K_RIGHT]:
            print('RIGHT')
            direction = 'right'
        elif keys[pygame.K_DOWN]:
            print('DOWN')
            direction = 'down'
        elif keys[pygame.K_LEFT]:
            print('LEFT')
            direction = 'left'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if direction == 'up':
            head.make_step(0, -1)
        elif direction == 'right':
            head.make_step(1, 0)
        elif direction == 'down':
            head.make_step(0, 1)
        elif direction == 'left':
            head.make_step(-1, 0)

        check_screen_border(head, screen_width, screen_height, square_lengths)
        eat_check(head, food_list, square_lengths, screen_width, screen_height)

        redraw(head, snake_body_list, food_list, window)


if __name__ == '__main__':
    main()