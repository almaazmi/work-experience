"""
Asteroid Defender - Turtle Graphics Version
Day 3 Starter Code

This template provides the basic structure for a graphical asteroid shooter game
using Python's Turtle module. You'll need to implement the game mechanics.
"""

import turtle
import random
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Asteroid Defender")
screen.tracer(0)  # Turn off automatic animation

# Register shapes
# TODO: Add code to register custom shapes from image files
# For now, we'll use built-in turtle shapes
screen.register_shape("triangle")
screen.register_shape("circle")

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

# Create the player's ship
ship = turtle.Turtle()
ship.shape("triangle")
ship.color("white")
ship.penup()
ship.speed(0)
ship.setposition(0, 0)
ship.setheading(90)

# Create score display
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(-380, 250)
score_display.write(f"Score: {game_state['score']} | Lives: {game_state['lives']} | Level: {game_state['level']}", 
                    font=("Arial", 14, "normal"))

# Functions for game mechanics

def create_asteroid(size="large"):
    """Create a new asteroid"""
    asteroid = turtle.Turtle()
    asteroid.shape("circle")
    asteroid.color("gray")
    asteroid.penup()
    asteroid.speed(0)
    
    # Set size
    if size == "large":
        asteroid.shapesize(3)
        speed = 1
        worth = 10
    elif size == "medium":
        asteroid.shapesize(2)
        speed = 1.5
        worth = 20
    else:  # small
        asteroid.shapesize(1)
        speed = 2
        worth = 30
    
    # Set position (off screen)
    x = random.randint(-380, 380)
    y = random.choice([-300, 300])  # Either top or bottom
    asteroid.setposition(x, y)
    
    # Set random heading
    angle = random.randint(0, 360)
    asteroid.setheading(angle)
    
    # Add to asteroids list
    game_state["asteroids"].append({
        "turtle": asteroid,
        "size": size,
        "speed": speed,
        "worth": worth
    })

def fire_bullet():
    """Fire a bullet from the ship"""
    # Limit firing rate
    current_time = time.time()
    if current_time - game_state["last_shot_time"] < 0.5:
        return  # Too soon to fire again
    
    game_state["last_shot_time"] = current_time
    
    # Create bullet
    bullet = turtle.Turtle()
    bullet.shape("circle")
    bullet.color("yellow")
    bullet.penup()
    bullet.speed(0)
    bullet.shapesize(0.3)
    bullet.setposition(ship.xcor(), ship.ycor())
    bullet.setheading(ship.heading())
    bullet.speed = 10
    
    # Add to bullets list
    game_state["bullets"].append(bullet)

def move_ship_left():
    """Move the ship left"""
    x = ship.xcor() - 10
    if x < -380:
        x = -380
    ship.setx(x)

def move_ship_right():
    """Move the ship right"""
    x = ship.xcor() + 10
    if x > 380:
        x = 380
    ship.setx(x)

def move_ship_up():
    """Move the ship up"""
    y = ship.ycor() + 10
    if y > 280:
        y = 280
    ship.sety(y)

def move_ship_down():
    """Move the ship down"""
    y = ship.ycor() - 10
    if y < -280:
        y = -280
    ship.sety(y)

def is_collision(obj1, obj2):
    """Check if two objects have collided"""
    distance = math.sqrt((obj1.xcor() - obj2.xcor())**2 + (obj1.ycor() - obj2.ycor())**2)
    return distance < 20  # Adjust collision threshold as needed

def update_game():
    """Update game state for one frame"""
    # TODO: Implement the logic to:
    # 1. Move all asteroids according to their heading and speed
    # 2. Move all bullets in their direction
    # 3. Check for collisions between bullets and asteroids
    # 4. Check for collisions between ship and asteroids
    # 5. Remove objects that go off screen
    # 6. Update the score display
    pass

def spawn_new_asteroids():
    """Spawn new asteroids based on level"""
    # TODO: Implement asteroid spawning logic
    # The higher the level, the more asteroids should spawn
    pass

def check_level_completion():
    """Check if all asteroids are destroyed to advance to next level"""
    # TODO: Implement level completion logic
    pass

def draw_game_over():
    """Display game over screen"""
    game_over_text = turtle.Turtle()
    game_over_text.hideturtle()
    game_over_text.penup()
    game_over_text.color("red")
    game_over_text.goto(0, 0)
    game_over_text.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
    
    score_text = turtle.Turtle()
    score_text.hideturtle()
    score_text.penup()
    score_text.color("white")
    score_text.goto(0, -50)
    score_text.write(f"Final Score: {game_state['score']}", align="center", font=("Arial", 24, "normal"))
    
    restart_text = turtle.Turtle()
    restart_text.hideturtle()
    restart_text.penup()
    restart_text.color("white")
    restart_text.goto(0, -100)
    restart_text.write("Press 'R' to restart or 'Q' to quit", align="center", font=("Arial", 18, "normal"))

# Set up keyboard bindings
screen.listen()
screen.onkeypress(move_ship_left, "Left")
screen.onkeypress(move_ship_right, "Right")
screen.onkeypress(move_ship_up, "Up")
screen.onkeypress(move_ship_down, "Down")
screen.onkeypress(fire_bullet, "space")

# Create initial asteroids
for _ in range(5):
    create_asteroid()

# Main game loop
def game_loop():
    """Main game loop"""
    while not game_state["game_over"]:
        update_game()
        check_level_completion()
        screen.update()  # Update the screen
        time.sleep(0.05)  # Small delay to control game speed
    
    draw_game_over()
    screen.update()

# Start the game
if __name__ == "__main__":
    game_loop()
    screen.mainloop()  # Keep the window open after game over
