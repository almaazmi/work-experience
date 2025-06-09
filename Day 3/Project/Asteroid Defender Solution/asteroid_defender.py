"""
Asteroid Defender - A PyGame space shooter game
Day 3 - Complete Solution
"""

import pygame
import random
import math
import os

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 20)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroid Defender")

# Load images
def load_image(name, scale=1):
    try:
        path = os.path.join("assets", name)
        image = pygame.image.load(path).convert_alpha()
        if scale != 1:
            size = image.get_size()
            image = pygame.transform.scale(image, (int(size[0] * scale), int(size[1] * scale)))
        return image
    except pygame.error as e:
        print(f"Couldn't load image: {name}")
        print(e)
        return pygame.Surface((50, 50))

# Check if assets folder exists, if not create a basic ship and asteroid
if not os.path.exists("assets"):
    os.makedirs("assets")
    
    # Create a simple ship image if none exists
    ship_surf = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.polygon(ship_surf, WHITE, [(0, 50), (25, 0), (50, 50), (25, 40)])
    pygame.image.save(ship_surf, os.path.join("assets", "player_ship.png"))
    
    # Create a simple asteroid image if none exists
    asteroid_surf = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.circle(asteroid_surf, (169, 169, 169), (20, 20), 20)
    pygame.image.save(asteroid_surf, os.path.join("assets", "asteroid.png"))
    
    # Create a simple laser image if none exists
    laser_surf = pygame.Surface((5, 15), pygame.SRCALPHA)
    pygame.draw.rect(laser_surf, GREEN, (0, 0, 5, 15))
    pygame.image.save(laser_surf, os.path.join("assets", "laser.png"))
    
    # Create a simple explosion image if none exists
    explosion_surf = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.circle(explosion_surf, YELLOW, (25, 25), 25)
    pygame.image.save(explosion_surf, os.path.join("assets", "explosion.png"))

# Load images
player_img = load_image("player_ship.png", 1)
asteroid_img = load_image("asteroid.png", 1)
laser_img = load_image("laser.png", 1)
explosion_img = load_image("explosion.png", 1)

# Load fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Game classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5
        self.health = 100
        self.score = 0
        self.shoot_delay = 250  # milliseconds
        self.last_shot = pygame.time.get_ticks()
        self.shield_active = False
        self.shield_time = 0
        self.shield_duration = 5000  # 5 seconds

    def update(self):
        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            
        # Check shield status
        current_time = pygame.time.get_ticks()
        if self.shield_active and current_time - self.shield_time > self.shield_duration:
            self.shield_active = False
    
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            return Laser(self.rect.centerx, self.rect.top)
        return None
        
    def activate_shield(self):
        self.shield_active = True
        self.shield_time = pygame.time.get_ticks()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = asteroid_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 4)
        self.speedx = random.randrange(-2, 2)
        self.size = random.choice(["large", "medium", "small"])
        
        # Scale asteroid based on size
        if self.size == "large":
            scale = 1.5
            self.health = 3
        elif self.size == "medium":
            scale = 1.0
            self.health = 2
        else:  # small
            scale = 0.6
            self.health = 1
            
        size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(size[0] * scale), int(size[1] * scale)))
        self.rect = self.image.get_rect(center=self.rect.center)
        
        # Rotate the asteroid image for variety
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()
        self.original_image = self.image.copy()

    def update(self):
        # Rotate asteroid
        self.rotate()
        
        # Move asteroid
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        
        # If asteroid goes off screen, respawn it
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 25:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)
            self.speedx = random.randrange(-2, 2)
            
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:  # rotate every 50 milliseconds
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.original_image, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = laser_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # Kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        super().__init__()
        self.image = explosion_img
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.frame_rate = 50
        self.last_update = pygame.time.get_ticks()
        
        # Scale explosion based on size
        if size == "large":
            scale = 1.5
        elif size == "medium":
            scale = 1.0
        else:  # small
            scale = 0.5
            
        img_size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(img_size[0] * scale), int(img_size[1] * scale)))
        self.rect = self.image.get_rect(center=self.rect.center)
        
        # Set how long the explosion lasts
        self.lifetime = 500  # milliseconds
        self.birth_time = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.birth_time > self.lifetime:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type  # "shield", "health", "rapid_fire"
        self.image = pygame.Surface((20, 20))
        
        if type == "shield":
            self.image.fill(BLUE)
        elif type == "health":
            self.image.fill(GREEN)
        elif type == "rapid_fire":
            self.image.fill(YELLOW)
            
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 3)

    def update(self):
        self.rect.y += self.speedy
        # If powerup goes off screen, remove it
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

def show_game_over():
    """Display game over screen"""
    screen.fill(BACKGROUND_COLOR)
    draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(screen, f"Score: {player.score}", 36, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(screen, "Press SPACE to play again", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3/4)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                    return True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False
    return True

def show_start_screen():
    """Show the start screen with game instructions"""
    screen.fill(BACKGROUND_COLOR)
    draw_text(screen, "ASTEROID DEFENDER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(screen, "Arrow keys to move, Space to fire", 22, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(screen, "Press SPACE to begin", 18, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3/4)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                    return True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False
    return True

def draw_text(surf, text, size, x, y):
    """Draw text on the screen"""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_health_bar(surf, x, y, pct):
    """Draw a health bar"""
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_shield(surf, x, y, radius):
    """Draw shield around player"""
    pygame.draw.circle(surf, BLUE, (x, y), radius, 2)

def new_game():
    """Initialize a new game"""
    global player, all_sprites, asteroids, lasers, explosions, powerups, score
    
    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    lasers = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    
    # Create player
    player = Player()
    all_sprites.add(player)
    
    # Create initial asteroids
    for i in range(8):
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroids.add(asteroid)
    
    score = 0

# Game loop
clock = pygame.time.Clock()
running = True
game_over = False
start_screen = True

# Main game loop
while running:
    # Start screen
    if start_screen:
        if not show_start_screen():
            running = False
        start_screen = False
        new_game()
    
    # Game over screen
    if game_over:
        if show_game_over():
            game_over = False
            new_game()
        else:
            running = False
            
    # Keep loop running at the right speed
    clock.tick(60)
    
    # Process input (events)
    for event in pygame.event.get():
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser = player.shoot()
                if laser:
                    all_sprites.add(laser)
                    lasers.add(laser)
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Update
    all_sprites.update()
    
    # Check for laser hitting asteroids
    hits = pygame.sprite.groupcollide(asteroids, lasers, False, True)
    for asteroid in hits:
        asteroid.health -= 1
        if asteroid.health <= 0:
            # Determine score based on asteroid size
            if asteroid.size == "large":
                score_value = 20
                expl_size = "large"
            elif asteroid.size == "medium":
                score_value = 10
                expl_size = "medium"
            else:  # small
                score_value = 5
                expl_size = "small"
                
            player.score += score_value
            
            # Create explosion
            explosion = Explosion(asteroid.rect.center, expl_size)
            all_sprites.add(explosion)
            explosions.add(explosion)
            
            # Remove asteroid
            asteroid.kill()
            
            # Chance to spawn a power-up
            if random.random() > 0.9:  # 10% chance
                pu_type = random.choice(["shield", "health", "rapid_fire"])
                pu = PowerUp(pu_type)
                pu.rect.center = asteroid.rect.center
                all_sprites.add(pu)
                powerups.add(pu)
            
            # Create new asteroid
            if len(asteroids) < 8 + player.score // 50:  # Increase difficulty
                asteroid = Asteroid()
                all_sprites.add(asteroid)
                asteroids.add(asteroid)
    
    # Check for asteroid hitting player
    hits = pygame.sprite.spritecollide(player, asteroids, True)
    for hit in hits:
        if not player.shield_active:
            # Determine damage based on asteroid size
            if hit.size == "large":
                damage = 20
                expl_size = "large"
            elif hit.size == "medium":
                damage = 10
                expl_size = "medium"
            else:  # small
                damage = 5
                expl_size = "small"
                
            player.health -= damage
        
        # Create explosion
        explosion = Explosion(hit.rect.center, expl_size)
        all_sprites.add(explosion)
        explosions.add(explosion)
        
        # Create new asteroid
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroids.add(asteroid)
        
        # Check if player is dead
        if player.health <= 0:
            death_explosion = Explosion(player.rect.center, "large")
            all_sprites.add(death_explosion)
            player.kill()
            game_over = True
    
    # Check for powerup collection
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == "shield":
            player.activate_shield()
        elif hit.type == "health":
            player.health = min(100, player.health + 20)
        elif hit.type == "rapid_fire":
            player.shoot_delay = max(100, player.shoot_delay - 50)
    
    # Draw / render
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)
    
    # Draw UI elements
    draw_text(screen, f"Score: {player.score}", 30, SCREEN_WIDTH // 2, 10)
    draw_text(screen, f"Health:", 22, 50, 10)
    draw_health_bar(screen, 110, 15, player.health)
    
    # Draw shield if active
    if player.shield_active:
        draw_shield(screen, player.rect.centerx, player.rect.centery, player.rect.width // 2 + 10)
    
    # Flip the display
    pygame.display.flip()

# Quit the game
pygame.quit()
