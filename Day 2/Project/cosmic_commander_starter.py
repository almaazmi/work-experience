"""
Cosmic Commander: Resource Management
Day 2 Starter Code

This template provides the basic structure for a space resource management game.
You'll need to implement functions, use collections, and add file handling.
"""

import random
import json
import os

# Game state
game_state = {
    "station_name": "",
    "day": 1,
    "resources": {
        "oxygen": 100,
        "food": 100,
        "water": 100,
        "energy": 100,
        "materials": 50
    },
    "crew": 5,
    "morale": 80,
    "missions_completed": 0,
    "events_survived": 0
}

# File to save game data
SAVE_FILE = "cosmic_commander_save.json"

# Functions for game mechanics

def initialize_game():
    """Set up a new game with player input"""
    print("=" * 60)
    print("COSMIC COMMANDER: RESOURCE MANAGEMENT")
    print("=" * 60)
    print("\nYou are in charge of a space station orbiting a distant planet.")
    print("Your mission is to manage resources, keep your crew alive,")
    print("and complete missions to ensure humanity's survival in space.")
    
    # TODO: Ask for the station name and set it in the game state
    
    print(f"\nWelcome aboard {game_state['station_name']}!")
    print("Your adventure begins now...\n")

def save_game():
    """Save the current game state to a file"""
    # TODO: Implement the save game functionality using file operations
    # Use the json module to convert the game_state dictionary to JSON
    # Write the JSON data to the SAVE_FILE
    pass

def load_game():
    """Load a saved game from a file"""
    global game_state
    # TODO: Implement the load game functionality
    # Check if the save file exists
    # If it does, read the file and parse the JSON data
    # Update the game_state with the loaded data
    pass

def display_status():
    """Show the current status of the space station"""
    # TODO: Display the current game state nicely formatted
    # Show station name, day, resources, crew count, and morale
    pass

def process_daily_consumption():
    """Calculate daily resource consumption based on crew size"""
    # TODO: Implement daily resource consumption
    # Reduce resources based on crew size
    # If any resource runs out, reduce crew and morale
    pass

def generate_random_event():
    """Generate a random event that affects resources"""
    # List of possible events
    events = [
        {"name": "Meteor Shower", "description": "A meteor shower has damaged some of your solar panels.", "effect": {"energy": -15}},
        {"name": "Supply Ship", "description": "A supply ship has docked with extra resources!", "effect": {"food": 20, "materials": 15}},
        {"name": "Oxygen Leak", "description": "There's an oxygen leak in sector 3!", "effect": {"oxygen": -20}},
        {"name": "Water Recycler Improved", "description": "Engineers improved the water recycling system.", "effect": {"water": 10}},
        {"name": "Crew Conflict", "description": "A conflict has broken out among crew members.", "effect": {"morale": -15}},
        {"name": "Scientific Discovery", "description": "Scientists made a discovery that boosted morale.", "effect": {"morale": 20}}
    ]
    
    # TODO: Select a random event from the list
    # Apply its effects to the game_state
    # Return the event for display purposes
    pass

def mission_menu():
    """Display available missions and let the player choose one"""
    missions = [
        {"name": "Repair Satellite", "difficulty": "Easy", "rewards": {"materials": 10, "energy": 5}},
        {"name": "Explore Nearby Moon", "difficulty": "Medium", "rewards": {"materials": 20, "water": 15}},
        {"name": "Rescue Stranded Astronaut", "difficulty": "Hard", "rewards": {"crew": 1, "morale": 10}}
    ]
    
    # TODO: Display the available missions
    # Let the player choose a mission
    # Calculate success based on current resources and difficulty
    # Apply rewards if successful
    pass

# Main game loop
def game_loop():
    global game_state
    
    # Check if a saved game exists
    if os.path.exists(SAVE_FILE):
        choice = input("A saved game was found. Would you like to load it? (y/n): ")
        if choice.lower() == 'y':
            load_game()
        else:
            initialize_game()
    else:
        initialize_game()
    
    while True:
        display_status()
        
        print("\nWhat would you like to do today?")
        print("1. Launch a mission")
        print("2. Manage resources")
        print("3. Save game")
        print("4. Quit")
        
        choice = input("> ")
        
        if choice == "1":
            mission_menu()
        elif choice == "2":
            # TODO: Implement resource management menu
            pass
        elif choice == "3":
            save_game()
            print("Game saved successfully!")
        elif choice == "4":
            save_choice = input("Would you like to save before quitting? (y/n): ")
            if save_choice.lower() == 'y':
                save_game()
                print("Game saved successfully!")
            print("Thank you for playing Cosmic Commander!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        # Process end of day
        event = generate_random_event()
        print(f"\nEND OF DAY {game_state['day']} EVENT: {event['name']}")
        print(event['description'])
        
        process_daily_consumption()
        game_state['day'] += 1
        
        # Check if game over
        if game_state['crew'] <= 0:
            print("\nAll crew members have perished. Game over!")
            break
        
        input("\nPress Enter to continue to the next day...")

# Start the game
if __name__ == "__main__":
    game_loop()
