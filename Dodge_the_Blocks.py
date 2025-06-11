# Dodge_the_Block Game
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 700
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 2

# Block settings
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50
BLOCK_SPEED = 3

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 36)


def draw_text(text, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2 - PLAYER_WIDTH//2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)


class Block:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - BLOCK_WIDTH), -BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
        self.speed = BLOCK_SPEED + random.random() * 2

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.reset()

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - BLOCK_WIDTH)
        self.rect.y = -BLOCK_HEIGHT
        self.speed = BLOCK_SPEED + random.random() * 2

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)


def game_loop():
    player = Player()
    blocks = [Block() for _ in range(6)]
    game_over = False

    while True:
        clock.tick(FPS)
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game_loop()  # Restart the game

        if not game_over:
            player.move(keys)
            player.draw()

            for block in blocks:
                block.update()
                block.draw()

                if block.rect.colliderect(player.rect):
                    game_over = True

        else:
            draw_text("Game Over!", RED, WIDTH//2 - 100, HEIGHT//2 - 50)
            draw_text("Press R to Restart", BLACK, WIDTH//2 - 140, HEIGHT//2)

        pygame.display.flip()


# Start the game
game_loop()
