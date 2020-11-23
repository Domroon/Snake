import pygame


class Square:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.x_step = 0
        self.y_step = 0

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def make_step(self):
        self.x += self.x_step
        self.y += self.y_step


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

    square = Square(10, 10, 20, 20, (255, 0, 0))

    run = True
    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        redraw(square, window)


if __name__ == '__main__':
    main()