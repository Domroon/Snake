import pygame


class Square:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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


def main():
    pygame.init()

    screen_width = 1280
    screen_height = 720

    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()

    square = Square(0, 0, 20, 20, (255, 0, 0))

    direction = 'right'

    run = True
    while run:
        clock.tick(2)

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

        redraw(square, window)


if __name__ == '__main__':
    main()