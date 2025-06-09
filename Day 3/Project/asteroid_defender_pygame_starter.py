"""
Asteroid Defender - PyGame Version
Day 3 Starter Code

This template provides the basic structure for a graphical asteroid shooter game
using PyGame. You'll need to implement the game mechanics.
"""

import pygame
import random
import math
import os

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Game constants
FPS = 60

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroid Defender")

# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Game state
game_state = {
    "score": 0,
    "lives": 3,
    "level": 1,
    "game_over": False,
    "asteroids": [],
    "bullets": [],
    "last_shot_time": 0  # To control shooting rate
}

# Ship class
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # TODO: Load ship image
        # For now, create a triangle ship
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, WHITE, [(15, 0), (0, 30), (30, 30)])
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5
    
    def update(self):
        # Handle movement based on key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
        # Keep the ship on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Asteroid class
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, size="large"):
        super().__init__()
        # TODO: Load asteroid images
        # For now, create circular asteroids
        if size == "large":
            radius = 40
            self.speed = 1
            self.worth = 10
        elif size == "medium":
            radius = 20
            self.speed = 2
            self.worth = 20
        else:  # small
            radius = 10
            self.speed = 3
            self.worth = 30
        
        self.size = size
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (150, 150, 150), (radius, radius), radius)
        self.rect = self.image.get_rect()
        
        # Start position (top of screen, random x)
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        
        # Random movement
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(1, 4)
    
    def update(self):
        # Move the asteroid
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # If asteroid goes off bottom of screen, respawn at top
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(1, 4)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10  # Negative because moving upward
    
    def update(self):
        self.rect.y += self.speedy
        # Remove bullet if it moves off screen
        if self.rect.bottom < 0:
            self.kill()

# Initialize sprite groups
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create player ship
player = Ship()
all_sprites.add(player)

# Create initial asteroids
for i in range(8):
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

# Game functions
def spawn_new_asteroids(count):
    """Spawn new asteroids"""
    for i in range(count):
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroids.add(asteroid)

def draw_text(surf, text, size, x, y, color=WHITE):
    """Draw text on the screen"""
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_lives(surf, x, y, lives, img=None):
    """Draw player lives on screen"""
    # TODO: Use ship image for lives
    # For now, draw rectangles
    for i in range(lives):
        pygame.draw.rect(surf, WHITE, (x + 30 * i, y, 20, 20))

def show_game_over_screen():
    """Show game over screen"""
    screen.fill(BLACK)
    draw_text(screen, "ASTEROID DEFENDER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(screen, f"Score: {game_state['score']}", 36, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(screen, "Press any key to play again", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3/4)
    pygame.display.flip()
    
    # Wait for player to press a key
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYUP:
                waiting = False
    return True

# Main game loop
def game_loop():
    running = True
    game_over = False
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Fire bullet
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
        
        if not game_over:
            # Update all sprites
            all_sprites.update()
            
            # Check for bullet/asteroid collisions
            hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
            for hit in hits:
                game_state["score"] += hit.worth
                # TODO: Add explosion animation
                # Spawn new asteroid
                asteroid = Asteroid()
                all_sprites.add(asteroid)
                asteroids.add(asteroid)
            
            # Check for ship/asteroid collisions
            hits = pygame.sprite.spritecollide(player, asteroids, True)
            for hit in hits:
                game_state["lives"] -= 1
                # TODO: Add ship explosion animation
                if game_state["lives"] <= 0:
                    game_over = True
            
            # Draw everything
            screen.fill(BLACK)
            all_sprites.draw(screen)
            
            # Draw UI
            draw_text(screen, f"Score: {game_state['score']}", 18, SCREEN_WIDTH // 2, 10)
            draw_lives(screen, SCREEN_WIDTH - 100, 10, game_state["lives"])
            
            pygame.display.flip()
        else:
            # Game over screen
            if show_game_over_screen():
                # Reset game
                game_over = False
                game_state["score"] = 0
                game_state["lives"] = 3
                
                # Remove all sprites and recreate
                all_sprites.empty()
                asteroids.empty()
                bullets.empty()
                
                player = Ship()
                all_sprites.add(player)
                
                for i in range(8):
                    asteroid = Asteroid()
                    all_sprites.add(asteroid)
                    asteroids.add(asteroid)
            else:
                running = False
        
        # Control frame rate
        clock.tick(FPS)

# Start the game
if __name__ == "__main__":
    game_loop()
    pygame.quit()
