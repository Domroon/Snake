import pygame


class Square:
    def __init__(self, x, y, square_lengths, color):
        self.x = x
        self.y = y
        self.width = square_lengths
        self.height = square_lengths
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def make_step(self, x_step, y_step):
        self.x += x_step * self.width
        self.y += y_step * self.height


def redraw(square, window):
    window.fill((0, 0, 0))
    square.draw(window)
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


def main():
    pygame.init()

    screen_width = 1280
    screen_height = 720

    square_lengths = 20

    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()

    square = Square(0, 0, square_lengths, (255, 0, 0))

    direction = 'right'

    run = True
    while run:
        clock.tick(3)

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
            square.make_step(0, -1)
        elif direction == 'right':
            square.make_step(1, 0)
        elif direction == 'down':
            square.make_step(0, 1)
        elif direction == 'left':
            square.make_step(-1, 0)

        check_screen_border(square, screen_width, screen_height, square_lengths)

        redraw(square, window)


if __name__ == '__main__':
    main()