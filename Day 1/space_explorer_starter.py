"""
Space Explorer: The Text Adventure
Day 1 Starter Code

This template provides the basic structure for a text-based space adventure game.
You'll need to complete the functions and add game logic using Python fundamentals.
"""

# Game variables
player_name = ""
player_oxygen = 100  # Starting oxygen level
player_health = 100  # Starting health
player_inventory = []  # Empty inventory to start
current_location = "Sleeping Quarters"  # Starting location

# Map of the spaceship - connects locations to possible destinations
ship_map = {
    "Sleeping Quarters": ["Corridor", "Bathroom"],
    "Corridor": ["Sleeping Quarters", "Bridge", "Engine Room", "Airlock"],
    "Bridge": ["Corridor"],
    "Engine Room": ["Corridor", "Maintenance Bay"],
    "Maintenance Bay": ["Engine Room"],
    "Airlock": ["Corridor", "Outside Ship"],
    "Bathroom": ["Sleeping Quarters"],
    "Outside Ship": ["Airlock"]
}

# Items available in each location
location_items = {
    "Sleeping Quarters": ["spacesuit", "notebook"],
    "Corridor": ["flashlight"],
    "Bridge": ["access card", "star map"],
    "Engine Room": ["toolkit", "fuel cell"],
    "Maintenance Bay": ["oxygen tank", "repair manual"],
    "Airlock": ["tether rope"],
    "Bathroom": ["medkit"],
    "Outside Ship": ["space rock"]
}

# Introduction
def introduction():
    print("=" * 60)
    print("SPACE EXPLORER: THE TEXT ADVENTURE")
    print("=" * 60)
    print("\nYou wake up on a spaceship to the sound of alarms.")
    print("The ship has been damaged and systems are failing.")
    print("You need to explore the ship, collect useful items,")
    print("and solve the crisis before your oxygen runs out!")
    
    global player_name
    player_name = input("\nWhat is your name, astronaut? ")
    print(f"\nGood luck, {player_name}! Your adventure begins now...\n")

# Show the current status of the player
def show_status():
    # TODO: Write code to display the player's current status
    # This should include name, health, oxygen level, inventory, and current location
    pass

# Show available commands
def show_commands():
    print("\nAvailable commands:")
    print("  look - Look around your current location")
    print("  go [direction] - Move to a new location")
    print("  take [item] - Add an item to your inventory")
    print("  inventory - Show your inventory")
    print("  status - Show your current status")
    print("  help - Show available commands")
    print("  quit - End the game")

# Look around the current location
def look_around():
    # TODO: Write code to describe the current location and list items available
    pass

# Move to a new location
def go_to(destination):
    # TODO: Write code to allow the player to move between locations
    # Remember to check if the destination is valid from the current location
    # Don't forget to reduce oxygen slightly when moving
    pass

# Take an item
def take_item(item):
    # TODO: Write code to allow the player to take an item
    # Check if the item is in the current location
    # Add it to inventory and remove it from the location
    pass

# Check oxygen level and update game state
def check_oxygen():
    # TODO: Write code to check oxygen level and take appropriate action
    # If oxygen gets too low, warn the player
    # If oxygen reaches zero, end the game
    pass

# Main game loop
def game_loop():
    global player_oxygen, current_location
    
    introduction()
    show_commands()
    
    while True:
        check_oxygen()  # Check oxygen level before each turn
        
        # Reduce oxygen slightly each turn
        player_oxygen -= 1
        
        # Get player command
        command = input(f"\n[{current_location}] What would you like to do? ").lower()
        
        # TODO: Add code to process the player's commands
        # This should include handling all the different commands
        # (look, go, take, inventory, status, help, quit)
        
        # Example of command processing (you need to complete this):
        if command == "quit":
            print("\nThank you for playing Space Explorer!")
            break
        elif command == "help":
            show_commands()
        # Add more elif statements for other commands
        else:
            print("I don't understand that command. Type 'help' for a list of commands.")

# Start the game
if __name__ == "__main__":
    game_loop()
