# Cosmic Commander Solution

This is a complete, functional implementation of the Cosmic Commander space resource management game described in the Day 2 project.

## Features

- Resource management game with multiple systems to balance
- Save/load functionality using JSON files
- Crew management system
- Planet exploration with risk/reward mechanics
- Mission system with requirements and rewards
- Trading system for buying and selling resources
- Random events that affect gameplay
- Multiple win and loss conditions

## How to Play

1. Run the game using Python: `python cosmic_commander.py`
2. Enter your commander name when prompted
3. Navigate through the menus to manage your spaceship and crew
4. Explore planets to gather resources
5. Complete missions to earn credits and reputation
6. Trade resources for credits to buy supplies
7. Manage your ship's maintenance
8. Try to complete all missions or reach 100 reputation to win

## Game Systems

- **Resource Management**: Balance oxygen, food, fuel, and credits
- **Exploration**: Visit planets to discover resources and complete missions
- **Missions**: Accept and complete missions for rewards
- **Trading**: Buy and sell resources and supplies
- **Ship Maintenance**: Repair your ship to prevent failure
- **Crew Management**: Hire crew members and monitor morale
- **Random Events**: Deal with unexpected situations during exploration

## Game Mechanics

- Each day consumes resources based on crew size
- Exploring planets requires fuel and carries risks
- Completing missions requires specific resources but provides rewards
- Ship health decreases over time and must be maintained
- Random events can help or hinder your progress

## Code Structure

The game uses a more complex structure than Day 1:
- JSON-based save/load system
- Function-based menu system
- Dictionaries for storing game data
- Random event generation
- Multiple interconnected systems

This solution demonstrates the application of intermediate Python concepts including functions, collections (lists, dictionaries), file handling for save/load functionality, and more complex program structure.
