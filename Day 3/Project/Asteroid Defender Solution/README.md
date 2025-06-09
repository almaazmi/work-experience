# Asteroid Defender Solution

This is a complete, functional implementation of the Asteroid Defender graphical game described in the Day 3 project, using PyGame.

## Features

- Full graphical arcade-style shooter game
- Object-oriented design with sprite classes
- Collision detection
- Rotating asteroids with different sizes
- Player ship with health system
- Laser weapons system
- Scoring system
- Power-ups (shield, health, rapid fire)
- Explosions and visual effects
- Game state management (start screen, game over screen)

## How to Play

1. Run the game using Python: `python asteroid_defender.py`
2. Use the LEFT and RIGHT arrow keys to move your ship
3. Press SPACE to shoot lasers at the asteroids
4. Avoid collisions with asteroids
5. Collect power-ups for advantages:
   - Blue: Shield (temporary invulnerability)
   - Green: Health (restores ship health)
   - Yellow: Rapid Fire (increases firing rate)
6. Try to achieve the highest score possible!

## Game Mechanics

- Smaller asteroids are worth fewer points but are faster
- Larger asteroids are worth more points but take multiple hits to destroy
- Asteroids have a chance to drop power-ups when destroyed
- Health decreases when hit by asteroids (unless shield is active)
- Game difficulty increases as your score rises
- Game ends when your health reaches zero

## Code Structure

The game uses a comprehensive structure typical of PyGame projects:
- Sprite classes for game objects (Player, Asteroid, Laser, Explosion, PowerUp)
- Main game loop handling input, updates, and rendering
- Collision detection between game objects
- Asset management for images
- Text rendering for UI elements
- Game state management

This solution demonstrates the application of advanced Python concepts including object-oriented programming, graphical rendering with PyGame, event handling, and game development patterns.
