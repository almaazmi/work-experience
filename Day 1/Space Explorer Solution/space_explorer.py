"""
Space Explorer - A text-based space adventure game
Day 1 - Complete Solution
"""

# Game variables
player_name = ""
oxygen = 100
fuel = 50
ship_health = 100
game_over = False
current_location = "Ship"

# Game locations
locations = {
    "Ship": {
        "description": "You are aboard your spaceship. The control panel is blinking with various indicators.",
        "options": ["Check oxygen levels", "Check fuel levels", "Check ship status", "Look outside", "Exit airlock"]
    },
    "Surface": {
        "description": "You are on the surface of an unknown planet. The landscape is rocky and alien.",
        "options": ["Explore further", "Collect samples", "Check oxygen levels", "Return to ship"]
    },
    "Cave": {
        "description": "You've found a mysterious cave. It's dark inside, but you can see strange glowing crystals.",
        "options": ["Examine crystals", "Go deeper", "Collect samples", "Return to surface"]
    }
}

# Game items that can be collected
items = []

def display_stats():
    """Display the player's current stats"""
    print("\n=== STATS ===")
    print(f"Oxygen: {oxygen}%")
    print(f"Fuel: {fuel} units")
    print(f"Ship Health: {ship_health}%")
    print(f"Items: {', '.join(items) if items else 'None'}")
    print("=============\n")

def intro():
    """Display the game introduction"""
    global player_name
    print("\n" + "=" * 60)
    print("SPACE EXPLORER: A COSMIC ADVENTURE")
    print("=" * 60)
    print("\nYou are a space explorer on a mission to discover new planets.")
    print("Your ship has landed on a mysterious planet, and it's up to you to explore it.")
    print("Be careful - you need to manage your resources to survive!")
    
    player_name = input("\nWhat is your name, explorer? ")
    print(f"\nWelcome, Captain {player_name}! Your adventure begins now...\n")

def get_user_choice(options):
    """Get and validate user choice from a list of options"""
    while True:
        print("\nWhat would you like to do?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        try:
            choice = int(input("\nEnter your choice (number): "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def ship_actions():
    """Handle actions when the player is on the ship"""
    global oxygen, fuel, ship_health, current_location
    
    print(locations["Ship"]["description"])
    choice = get_user_choice(locations["Ship"]["options"])
    
    if choice == 1:  # Check oxygen levels
        print(f"\nOxygen levels are at {oxygen}%.")
        if oxygen < 30:
            print("Warning: Oxygen levels are low!")
        elif oxygen < 10:
            print("CRITICAL: Oxygen levels dangerously low!")
    
    elif choice == 2:  # Check fuel levels
        print(f"\nFuel reserves are at {fuel} units.")
        if fuel < 20:
            print("Warning: Fuel reserves are low!")
        elif fuel < 5:
            print("CRITICAL: Almost out of fuel!")
    
    elif choice == 3:  # Check ship status
        print(f"\nShip health is at {ship_health}%.")
        if ship_health < 50:
            print("Warning: Ship has sustained damage!")
        elif ship_health < 20:
            print("CRITICAL: Ship integrity compromised!")
    
    elif choice == 4:  # Look outside
        print("\nThrough the viewport, you see a desolate landscape.")
        print("The ground is rocky, and strange formations dot the horizon.")
        print("The atmosphere seems thin, but breathable with your suit.")
    
    elif choice == 5:  # Exit airlock
        print("\nYou suit up and exit through the airlock...")
        current_location = "Surface"

def surface_actions():
    """Handle actions when the player is on the planet surface"""
    global oxygen, current_location, items
    
    print(locations["Surface"]["description"])
    choice = get_user_choice(locations["Surface"]["options"])
    
    if choice == 1:  # Explore further
        print("\nYou venture further across the rocky terrain.")
        oxygen -= 5
        print("You discover a cave entrance hidden among some rock formations.")
        if input("\nWould you like to enter the cave? (y/n): ").lower() == 'y':
            current_location = "Cave"
        
    elif choice == 2:  # Collect samples
        print("\nYou collect rock and soil samples from the surface.")
        if "Surface Samples" not in items:
            items.append("Surface Samples")
            print("Added Surface Samples to your inventory.")
        else:
            print("You already have surface samples in your inventory.")
        oxygen -= 5
    
    elif choice == 3:  # Check oxygen levels
        print(f"\nYour suit's oxygen level is at {oxygen}%.")
        if oxygen < 30:
            print("Warning: Oxygen levels are getting low. Consider returning to the ship.")
    
    elif choice == 4:  # Return to ship
        print("\nYou return to your ship and cycle through the airlock.")
        current_location = "Ship"

def cave_actions():
    """Handle actions when the player is in the cave"""
    global oxygen, current_location, items
    
    print(locations["Cave"]["description"])
    choice = get_user_choice(locations["Cave"]["options"])
    
    if choice == 1:  # Examine crystals
        print("\nYou examine the glowing crystals closely.")
        print("They emit a soft blue light and seem to pulse with energy.")
        oxygen -= 5
        
    elif choice == 2:  # Go deeper
        print("\nYou venture deeper into the cave system.")
        print("The passage narrows and the crystals grow more numerous.")
        if "Energy Crystal" not in items:
            print("\nYou find a large, particularly bright crystal!")
            if input("Would you like to take it? (y/n): ").lower() == 'y':
                items.append("Energy Crystal")
                print("Added Energy Crystal to your inventory.")
                print("The crystal seems to be interfering with your suit systems...")
                oxygen -= 15
        else:
            print("There's nothing else of interest deeper in the cave.")
        oxygen -= 10
    
    elif choice == 3:  # Collect samples
        print("\nYou carefully extract some of the smaller crystals.")
        if "Crystal Samples" not in items:
            items.append("Crystal Samples")
            print("Added Crystal Samples to your inventory.")
        else:
            print("You already have crystal samples in your inventory.")
        oxygen -= 5
    
    elif choice == 4:  # Return to surface
        print("\nYou make your way back to the planet's surface.")
        current_location = "Surface"

def check_game_state():
    """Check if the game should end based on player status"""
    global game_over
    
    # Reduce oxygen over time
    if current_location != "Ship":
        global oxygen
        oxygen -= 2
    
    # Check if game over conditions are met
    if oxygen <= 0:
        print("\n*** CRITICAL OXYGEN FAILURE ***")
        print("Your oxygen supply has been depleted. You collapse on the alien surface.")
        game_over = True
        return
    
    if "Energy Crystal" in items and "Surface Samples" in items and "Crystal Samples" in items:
        print("\n*** MISSION SUCCESSFUL ***")
        print("You've collected all the important samples from this planet!")
        print(f"Congratulations, Captain {player_name}! You can now return to Earth with your discoveries.")
        game_over = True
        return

def main():
    """Main game loop"""
    intro()
    
    while not game_over:
        display_stats()
        
        if current_location == "Ship":
            ship_actions()
        elif current_location == "Surface":
            surface_actions()
        elif current_location == "Cave":
            cave_actions()
        
        check_game_state()
    
    print("\nGame Over")
    print(f"Final Stats: Oxygen: {oxygen}%, Fuel: {fuel}, Ship Health: {ship_health}%")
    print(f"Items collected: {', '.join(items) if items else 'None'}")

if __name__ == "__main__":
    main()
