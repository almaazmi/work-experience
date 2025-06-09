# Space Explorer Solution

This is a complete, functional implementation of the Space Explorer text-based adventure game described in the Day 1 project.

## Features

- Text-based adventure game with multiple locations to explore
- Resource management (oxygen, fuel, ship health)
- Item collection system
- Game state tracking
- Multiple endings based on player actions
- User-friendly interface with clear options

## How to Play

1. Run the game using Python: `python space_explorer.py`
2. Enter your name when prompted
3. Make choices by typing the corresponding number
4. Explore the planet, collect samples, and manage your resources
5. Try to collect all the important samples before your oxygen runs out

## Game Locations

- **Ship**: Your home base where you can check your resources
- **Surface**: The alien planet's surface where you can collect samples
- **Cave**: A mysterious cave with valuable crystals

## Game Mechanics

- Oxygen decreases over time when exploring outside the ship
- Making certain choices will consume additional oxygen
- Collecting all three types of samples (Surface Samples, Crystal Samples, and Energy Crystal) will complete the mission
- Running out of oxygen results in game over

## Code Structure

The game uses a simple but effective structure:
- Location-based action functions
- Game state tracking variables
- A main game loop
- Helper functions for displaying information

This solution demonstrates the application of fundamental Python concepts including variables, data types, conditional statements, loops, and basic functions.
