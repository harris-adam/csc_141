import pygame
import random
import sys
import os

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Alien Invasion")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Font settings
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 30)

# Game state variables
highest_score_file = "highest_score.txt"
highest_score = 0

# Load highest score from file
if os.path.exists(highest_score_file):
    with open(highest_score_file, 'r') as file:
        highest_score = int(file.read())

# Ship class
class Ship:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 50
        self.width = 50
        self.height = 50
        self.color = BLUE
        self.speed = 5
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False  # Add flag for vertical movement
        self.moving_down = False  # Add flag for downward movement

    def update(self):
        if self.moving_left and self.x > 0:
            self.x -= self.speed
        if self.moving_right and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed
        if self.moving_up and self.y > 0:  # Prevent the ship from going above the screen
            self.y -= self.speed
        if self.moving_down and self.y < SCREEN_HEIGHT - self.height:  # Prevent the ship from going below the screen
            self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Bullet class
class Bullet:
    def __init__(self, ship):
        self.x = ship.x + ship.width // 2
        self.y = ship.y
        self.width = 5
        self.height = 10
        self.color = WHITE
        self.speed = 7

    def update(self):
        self.y -= self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Alien class (advanced aliens with shapes)
class Alien:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - 50)
        self.y = random.randint(50, 200)
        self.width = 50
        self.height = 50
        self.color = RED
        self.speed = 1  # Speed increases later
        self.direction = 1  # Direction of alien movement (1 = downwards)

    def update(self):
        self.y += self.speed * self.direction
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-100, -50)  # Reset the alien to the top if it goes off-screen
            self.x = random.randint(0, SCREEN_WIDTH - self.width)

    def draw(self):
        # Draw an alien as a combination of a rectangle and a triangle
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height // 2))
        pygame.draw.polygon(screen, self.color, [(self.x, self.y + self.height // 2), 
                                                 (self.x + self.width // 2, self.y + self.height), 
                                                 (self.x + self.width, self.y + self.height // 2)])

# Game state class
class GameState:
    def __init__(self):
        self.score = 0
        self.game_active = False
        self.ship = Ship()
        self.bullets = []
        self.aliens = [Alien() for _ in range(5)]
        self.clock = pygame.time.Clock()

# Title screen
def show_title_screen():
    title_text = font.render("Alien Invasion", True, WHITE)
    press_text = small_font.render("Press SPACE to Start", True, WHITE)

    screen.fill(BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(press_text, (SCREEN_WIDTH // 2 - press_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    pygame.display.update()

# Game Over screen
def show_game_over_screen(score):
    game_over_text = font.render("GAME OVER", True, WHITE)
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    high_score_text = small_font.render(f"High Score: {highest_score}", True, WHITE)
    try_again_text = small_font.render("Press SPACE to Try Again", True, WHITE)

    screen.fill(BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(try_again_text, (SCREEN_WIDTH // 2 - try_again_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

    pygame.display.update()

# Scoreboard
def show_score(score):
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# High Score tracker
def update_high_score(score):
    global highest_score
    if score > highest_score:
        highest_score = score
        with open(highest_score_file, 'w') as file:
            file.write(str(highest_score))

# Draw stars in the background (slower stars)
def draw_stars():
    for _ in range(50):  # Slower moving stars
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        pygame.draw.circle(screen, WHITE, (x, y), random.randint(1, 3))

# Game loop
def game_loop():
    game_state = GameState()

    # Show title screen
    show_title_screen()
    waiting_for_start = True
    while waiting_for_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting_for_start = False
                    game_state.game_active = True

        pygame.display.update()

    # Main game loop
    while game_state.game_active:
        screen.fill(BLACK)

        # Draw stars in the background
        draw_stars()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game_state.ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    game_state.ship.moving_right = True
                elif event.key == pygame.K_UP:
                    game_state.ship.moving_up = True  # Move up
                elif event.key == pygame.K_DOWN:
                    game_state.ship.moving_down = True  # Move down
                elif event.key == pygame.K_SPACE:
                    game_state.bullets.append(Bullet(game_state.ship))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    game_state.ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    game_state.ship.moving_right = False
                elif event.key == pygame.K_UP:
                    game_state.ship.moving_up = False  # Stop moving up
                elif event.key == pygame.K_DOWN:
                    game_state.ship.moving_down = False  # Stop moving down

        # Update game elements
        game_state.ship.update()

        for bullet in game_state.bullets[:]:
            bullet.update()
            if bullet.y < 0:
                game_state.bullets.remove(bullet)

        for alien in game_state.aliens[:]:
            alien.update()
            if alien.y > SCREEN_HEIGHT:
                game_state.aliens.remove(alien)
                game_state.aliens.append(Alien())  # Add a new alien at the top

        # Check for bullet-alien collisions
        for bullet in game_state.bullets[:]:
            for alien in game_state.aliens[:]:
                if (bullet.x > alien.x and bullet.x < alien.x + alien.width) and \
                   (bullet.y > alien.y and bullet.y < alien.y + alien.height):
                    game_state.bullets.remove(bullet)
                    game_state.aliens.remove(alien)
                    game_state.aliens.append(Alien())
                    game_state.score += 10

        # Check for ship-alien collisions
        for alien in game_state.aliens[:]:
            if (game_state.ship.x > alien.x and game_state.ship.x < alien.x + alien.width) and \
               (game_state.ship.y > alien.y and game_state.ship.y < alien.y + alien.height):
                game_state.game_active = False
                update_high_score(game_state.score)
                show_game_over_screen(game_state.score)

        # Draw game elements
        game_state.ship.draw()
        for bullet in game_state.bullets:
            bullet.draw()
        for alien in game_state.aliens:
            alien.draw()

        # Draw score
        show_score(game_state.score)

        pygame.display.update()

        # Frame rate
        game_state.clock.tick(60)

    # After game over, allow player to press SPACE to try again
    waiting_for_retry = True
    while waiting_for_retry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()  # Restart the game

# Run the game
game_loop()

# Quit pygame
pygame.quit()
