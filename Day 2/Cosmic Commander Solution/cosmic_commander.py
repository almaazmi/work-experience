"""
Cosmic Commander - A space resource management game
Day 2 - Complete Solution
"""

import os
import json
import random
import time

# Game constants
SAVE_FILE = "game_save.json"

# Game variables
player = {
    "name": "",
    "day": 1,
    "crew": 5,
    "food": 100,
    "oxygen": 100,
    "fuel": 100,
    "credits": 1000,
    "ship_health": 100,
    "reputation": 50,
    "inventory": [],
    "missions_completed": [],
    "explored_planets": []
}

# Available resources
resources = {
    "minerals": {"price": 50, "weight": 2},
    "water": {"price": 30, "weight": 1},
    "alien_artifacts": {"price": 150, "weight": 1},
    "rare_metals": {"price": 100, "weight": 3},
    "crystal_shards": {"price": 80, "weight": 1},
    "bio_samples": {"price": 120, "weight": 2}
}

# Available planets
planets = {
    "Nexus Prime": {
        "distance": 1,
        "danger": 1,
        "resources": ["minerals", "water"],
        "description": "A temperate planet with abundant water and basic minerals."
    },
    "Cryosia": {
        "distance": 2,
        "danger": 2,
        "resources": ["water", "rare_metals"],
        "description": "An icy world with rare metals beneath its frozen surface."
    },
    "Vulcanis": {
        "distance": 3,
        "danger": 3,
        "resources": ["minerals", "crystal_shards"],
        "description": "A volcanic planet with valuable crystal formations in its cooling lava flows."
    },
    "Xenoria": {
        "distance": 4,
        "danger": 4,
        "resources": ["alien_artifacts", "bio_samples"],
        "description": "A mysterious planet with signs of ancient alien civilization and unique life forms."
    },
    "Asteros Belt": {
        "distance": 2,
        "danger": 3,
        "resources": ["minerals", "rare_metals"],
        "description": "A dense asteroid field rich in various metals and minerals."
    }
}

# Available missions
missions = [
    {
        "id": 1,
        "name": "Supply Run",
        "description": "Deliver essential supplies to a nearby outpost.",
        "planet": "Nexus Prime",
        "reward": 300,
        "reputation": 10,
        "requirements": {"fuel": 20, "food": 20},
        "difficulty": 1
    },
    {
        "id": 2,
        "name": "Mineral Survey",
        "description": "Conduct a geological survey on Cryosia.",
        "planet": "Cryosia",
        "reward": 500,
        "reputation": 15,
        "requirements": {"fuel": 40, "oxygen": 30},
        "difficulty": 2
    },
    {
        "id": 3,
        "name": "Artifact Recovery",
        "description": "Retrieve alien artifacts from ruins on Xenoria.",
        "planet": "Xenoria",
        "reward": 800,
        "reputation": 25,
        "requirements": {"fuel": 60, "oxygen": 50, "food": 40},
        "difficulty": 4
    },
    {
        "id": 4,
        "name": "Mining Operation",
        "description": "Extract rare metals from the Asteros Belt.",
        "planet": "Asteros Belt",
        "reward": 600,
        "reputation": 20,
        "requirements": {"fuel": 45, "oxygen": 40},
        "difficulty": 3
    },
    {
        "id": 5,
        "name": "Volcanic Research",
        "description": "Conduct research on Vulcanis's volcanic activity.",
        "planet": "Vulcanis",
        "reward": 700,
        "reputation": 20,
        "requirements": {"fuel": 50, "oxygen": 60},
        "difficulty": 3
    }
]

# Random events that can occur
random_events = [
    {
        "name": "Solar Flare",
        "description": "A sudden solar flare damages your ship's systems.",
        "effect": {"ship_health": -10, "oxygen": -5},
        "severity": "moderate"
    },
    {
        "name": "Meteor Shower",
        "description": "Your ship navigates through a dense meteor shower.",
        "effect": {"ship_health": -15, "fuel": -10},
        "severity": "severe"
    },
    {
        "name": "Space Pirates",
        "description": "Space pirates attempt to raid your ship.",
        "effect": {"credits": -200, "ship_health": -5},
        "severity": "severe"
    },
    {
        "name": "Cosmic Radiation",
        "description": "Unusual radiation levels affect your crew's health.",
        "effect": {"crew": -1, "oxygen": -10},
        "severity": "severe"
    },
    {
        "name": "Supply Cache",
        "description": "You discover an abandoned supply cache floating in space.",
        "effect": {"food": 20, "oxygen": 15, "fuel": 15},
        "severity": "positive"
    },
    {
        "name": "System Malfunction",
        "description": "A system malfunction causes resource leakage.",
        "effect": {"oxygen": -10, "fuel": -5},
        "severity": "moderate"
    },
    {
        "name": "Friendly Trader",
        "description": "A friendly trader offers you discounted supplies.",
        "effect": {"credits": 150, "food": 10},
        "severity": "positive"
    },
    {
        "name": "Crew Dispute",
        "description": "A dispute among crew members affects morale.",
        "effect": {"reputation": -5},
        "severity": "minor"
    }
]

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def save_game():
    """Save the current game state to a file"""
    with open(SAVE_FILE, 'w') as f:
        json.dump(player, f)
    print("\nGame saved successfully!")

def load_game():
    """Load a saved game from file"""
    global player
    try:
        with open(SAVE_FILE, 'r') as f:
            player = json.load(f)
        print("\nGame loaded successfully!")
        return True
    except FileNotFoundError:
        print("\nNo saved game found.")
        return False

def display_header():
    """Display the game header"""
    clear_screen()
    print("=" * 60)
    print(f"COSMIC COMMANDER - Day {player['day']}")
    print("=" * 60)
    print(f"Captain: {player['name']} | Reputation: {player['reputation']}")
    print("-" * 60)

def display_status():
    """Display the current status of the player"""
    print("\n=== SHIP STATUS ===")
    print(f"Crew: {player['crew']} | Ship Health: {player['ship_health']}%")
    print(f"Food: {player['food']} units | Oxygen: {player['oxygen']} units | Fuel: {player['fuel']} units")
    print(f"Credits: {player['credits']}")
    
    if player['inventory']:
        print("\n=== INVENTORY ===")
        for item in player['inventory']:
            print(f"- {item}")
    
    if player['explored_planets']:
        print("\n=== EXPLORED PLANETS ===")
        for planet in player['explored_planets']:
            print(f"- {planet}")
    
    if player['missions_completed']:
        print("\n=== COMPLETED MISSIONS ===")
        for mission in player['missions_completed']:
            print(f"- {mission}")
    
    print("\n" + "-" * 60)

def intro():
    """Display the game introduction"""
    clear_screen()
    print("=" * 60)
    print("COSMIC COMMANDER: A SPACE RESOURCE MANAGEMENT ADVENTURE")
    print("=" * 60)
    print("\nThe year is 2157. Humanity has expanded throughout the solar system")
    print("and is now venturing into nearby star systems.")
    print("\nAs the commander of the spaceship 'Odyssey', your mission is to")
    print("explore new planets, gather valuable resources, and ensure the")
    print("survival of your crew while maintaining your ship.")
    print("\nEvery decision matters. Will you prioritize exploration, profit,")
    print("or the safety of your crew?")
    
    global player
    player["name"] = input("\nWhat is your name, Commander? ")
    print(f"\nWelcome aboard, Commander {player['name']}! Your journey begins now...\n")
    input("Press Enter to continue...")

def main_menu():
    """Display the main menu and get player choice"""
    display_header()
    display_status()
    
    print("\n=== MAIN MENU ===")
    print("1. Explore a Planet")
    print("2. Trade Resources")
    print("3. Ship Maintenance")
    print("4. Manage Crew")
    print("5. View Missions")
    print("6. End Day")
    print("7. Save Game")
    print("8. Exit Game")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-8): "))
            if 1 <= choice <= 8:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
        except ValueError:
            print("Please enter a number.")

def explore_planet():
    """Handle planet exploration"""
    display_header()
    print("\n=== EXPLORE A PLANET ===")
    
    print("\nAvailable planets:")
    available_planets = list(planets.keys())
    for i, planet_name in enumerate(available_planets, 1):
        planet = planets[planet_name]
        print(f"{i}. {planet_name} - Distance: {planet['distance']} AU, Danger: {planet['danger']}/5")
        print(f"   Description: {planet['description']}")
        print(f"   Resources: {', '.join(planet['resources'])}")
    
    print(f"{len(available_planets) + 1}. Return to Main Menu")
    
    while True:
        try:
            choice = int(input("\nSelect a planet to explore (or return): "))
            if 1 <= choice <= len(available_planets):
                selected_planet = available_planets[choice - 1]
                explore_selected_planet(selected_planet)
                return
            elif choice == len(available_planets) + 1:
                return
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def explore_selected_planet(planet_name):
    """Handle exploration of a selected planet"""
    planet = planets[planet_name]
    
    # Calculate fuel cost based on distance
    fuel_cost = planet["distance"] * 10
    
    # Check if player has enough fuel
    if player["fuel"] < fuel_cost:
        print(f"\nNot enough fuel to reach {planet_name}. Required: {fuel_cost} units.")
        input("\nPress Enter to continue...")
        return
    
    # Ask for confirmation
    print(f"\nExploring {planet_name} will consume {fuel_cost} units of fuel.")
    confirm = input("Do you want to proceed? (y/n): ").lower()
    if confirm != 'y':
        return
    
    # Deduct fuel cost
    player["fuel"] -= fuel_cost
    
    print(f"\nTraveling to {planet_name}...")
    time.sleep(1)
    print("Entering orbit...")
    time.sleep(1)
    print("Scanning surface...")
    time.sleep(1)
    
    # Check for random event
    if random.random() < 0.3:  # 30% chance of random event
        trigger_random_event()
    
    # Exploration success based on planet danger and ship health
    success_chance = 100 - (planet["danger"] * 10) + (player["ship_health"] // 10)
    success_chance = max(10, min(90, success_chance))  # Clamp between 10% and 90%
    
    if random.randint(1, 100) <= success_chance:
        # Successful exploration
        print(f"\nExploration of {planet_name} successful!")
        
        # Add planet to explored list if it's not already there
        if planet_name not in player["explored_planets"]:
            player["explored_planets"].append(planet_name)
        
        # Gather resources
        resources_found = []
        for resource_name in planet["resources"]:
            if random.random() < 0.7:  # 70% chance to find each resource
                resources_found.append(resource_name)
                if resource_name not in player["inventory"]:
                    player["inventory"].append(resource_name)
        
        if resources_found:
            print(f"Resources gathered: {', '.join(resources_found)}")
        else:
            print("No resources were gathered during this expedition.")
        
        # Gain reputation
        reputation_gain = planet["danger"] * 2
        player["reputation"] += reputation_gain
        print(f"Reputation increased by {reputation_gain} points.")
    else:
        # Failed exploration
        print(f"\nExploration of {planet_name} encountered difficulties!")
        
        # Lose resources
        oxygen_loss = planet["danger"] * 5
        food_loss = planet["danger"] * 3
        ship_damage = planet["danger"] * 5
        
        player["oxygen"] = max(0, player["oxygen"] - oxygen_loss)
        player["food"] = max(0, player["food"] - food_loss)
        player["ship_health"] = max(0, player["ship_health"] - ship_damage)
        
        print(f"Oxygen decreased by {oxygen_loss} units.")
        print(f"Food decreased by {food_loss} units.")
        print(f"Ship sustained {ship_damage}% damage.")
        
        # Crew injury chance
        if player["ship_health"] < 50 and random.random() < 0.3:
            player["crew"] -= 1
            print("A crew member was injured during the expedition.")
    
    input("\nPress Enter to continue...")

def trigger_random_event():
    """Trigger a random event during exploration"""
    event = random.choice(random_events)
    
    print("\n" + "!" * 60)
    print(f"ALERT: {event['name']}")
    print(event['description'])
    
    # Apply event effects
    for resource, change in event['effect'].items():
        if resource in player:
            player[resource] += change
            player[resource] = max(0, player[resource])  # Ensure value doesn't go below zero
            
            if change > 0:
                print(f"{resource.replace('_', ' ').title()} increased by {change}.")
            else:
                print(f"{resource.replace('_', ' ').title()} decreased by {abs(change)}.")
    
    print("!" * 60)
    time.sleep(2)

def trade_resources():
    """Handle resource trading"""
    display_header()
    print("\n=== TRADING POST ===")
    
    print("\nYour Inventory:")
    if not player["inventory"]:
        print("You have no resources to trade.")
    else:
        for i, resource in enumerate(player["inventory"], 1):
            price = resources[resource]["price"]
            print(f"{i}. {resource} - Value: {price} credits")
    
    print("\nTrading Options:")
    print("1. Sell Resources")
    print("2. Buy Supplies")
    print("3. Return to Main Menu")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if choice == 1:
                sell_resources()
                return
            elif choice == 2:
                buy_supplies()
                return
            elif choice == 3:
                return
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def sell_resources():
    """Handle selling resources"""
    if not player["inventory"]:
        print("\nYou have no resources to sell.")
        input("\nPress Enter to continue...")
        return
    
    print("\n=== SELL RESOURCES ===")
    print("Your Inventory:")
    for i, resource in enumerate(player["inventory"], 1):
        price = resources[resource]["price"]
        print(f"{i}. {resource} - Value: {price} credits")
    
    print(f"{len(player['inventory']) + 1}. Return to Trading Post")
    
    while True:
        try:
            choice = int(input("\nSelect a resource to sell (or return): "))
            if 1 <= choice <= len(player["inventory"]):
                selected_resource = player["inventory"][choice - 1]
                
                # Get selling price
                price = resources[selected_resource]["price"]
                
                # Ask for confirmation
                confirm = input(f"\nSell {selected_resource} for {price} credits? (y/n): ").lower()
                if confirm == 'y':
                    # Remove resource and add credits
                    player["inventory"].remove(selected_resource)
                    player["credits"] += price
                    print(f"\nSold {selected_resource} for {price} credits.")
                
                # Return to trading menu
                trade_resources()
                return
            elif choice == len(player["inventory"]) + 1:
                trade_resources()
                return
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def buy_supplies():
    """Handle buying supplies"""
    display_header()
    print("\n=== BUY SUPPLIES ===")
    print(f"Available Credits: {player['credits']}")
    
    supplies = {
        1: {"name": "Food", "price": 10, "amount": 10},
        2: {"name": "Oxygen", "price": 15, "amount": 10},
        3: {"name": "Fuel", "price": 20, "amount": 10},
        4: {"name": "Ship Repair Kit", "price": 50, "amount": 10}
    }
    
    print("\nAvailable Supplies:")
    for i, supply in supplies.items():
        print(f"{i}. {supply['name']} - {supply['amount']} units for {supply['price']} credits")
    
    print("5. Return to Trading Post")
    
    while True:
        try:
            choice = int(input("\nSelect supplies to buy (or return): "))
            if 1 <= choice <= 4:
                selected_supply = supplies[choice]
                
                # Check if player has enough credits
                if player["credits"] < selected_supply["price"]:
                    print("\nNot enough credits.")
                else:
                    # Apply purchase
                    player["credits"] -= selected_supply["price"]
                    
                    if choice == 1:
                        player["food"] += selected_supply["amount"]
                        print(f"\nPurchased {selected_supply['amount']} units of food.")
                    elif choice == 2:
                        player["oxygen"] += selected_supply["amount"]
                        print(f"\nPurchased {selected_supply['amount']} units of oxygen.")
                    elif choice == 3:
                        player["fuel"] += selected_supply["amount"]
                        print(f"\nPurchased {selected_supply['amount']} units of fuel.")
                    elif choice == 4:
                        repair_amount = min(selected_supply["amount"], 100 - player["ship_health"])
                        player["ship_health"] += repair_amount
                        print(f"\nRepaired ship by {repair_amount}%.")
                
                # Continue shopping
                buy_supplies()
                return
            elif choice == 5:
                trade_resources()
                return
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def ship_maintenance():
    """Handle ship maintenance"""
    display_header()
    print("\n=== SHIP MAINTENANCE ===")
    print(f"Current Ship Health: {player['ship_health']}%")
    
    if player["ship_health"] >= 100:
        print("\nYour ship is in perfect condition!")
        input("\nPress Enter to continue...")
        return
    
    repair_cost = (100 - player["ship_health"]) * 5
    print(f"\nFull repair will cost {repair_cost} credits.")
    
    if player["credits"] < repair_cost:
        print(f"You don't have enough credits for a full repair (need {repair_cost}).")
        max_repair = player["credits"] // 5
        if max_repair > 0:
            print(f"You can repair up to {max_repair}% with your current credits.")
            
            repair_amount = input(f"\nHow much do you want to repair (0-{max_repair})? ")
            try:
                repair_amount = int(repair_amount)
                if 0 <= repair_amount <= max_repair:
                    cost = repair_amount * 5
                    player["credits"] -= cost
                    player["ship_health"] += repair_amount
                    print(f"\nRepaired ship by {repair_amount}%. New health: {player['ship_health']}%")
                else:
                    print("Invalid amount.")
            except ValueError:
                print("Please enter a number.")
    else:
        confirm = input("Do you want to fully repair your ship? (y/n): ").lower()
        if confirm == 'y':
            player["credits"] -= repair_cost
            player["ship_health"] = 100
            print("\nShip fully repaired!")
    
    input("\nPress Enter to continue...")

def manage_crew():
    """Handle crew management"""
    display_header()
    print("\n=== CREW MANAGEMENT ===")
    print(f"Current Crew: {player['crew']}")
    print(f"Food: {player['food']} units")
    
    print("\nOptions:")
    print("1. Hire New Crew Members")
    print("2. Check Crew Morale")
    print("3. Return to Main Menu")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if choice == 1:
                hire_crew()
                return
            elif choice == 2:
                check_morale()
                return
            elif choice == 3:
                return
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def hire_crew():
    """Handle hiring new crew members"""
    max_crew = 10
    
    if player["crew"] >= max_crew:
        print(f"\nYour ship is already at maximum crew capacity ({max_crew}).")
        input("\nPress Enter to continue...")
        return
    
    crew_cost = 200
    print(f"\nHiring a new crew member costs {crew_cost} credits.")
    print(f"You can hire up to {max_crew - player['crew']} more crew members.")
    
    if player["credits"] < crew_cost:
        print("\nYou don't have enough credits to hire new crew members.")
        input("\nPress Enter to continue...")
        return
    
    max_hire = min(player["credits"] // crew_cost, max_crew - player["crew"])
    hire_amount = input(f"\nHow many crew members do you want to hire (0-{max_hire})? ")
    
    try:
        hire_amount = int(hire_amount)
        if 0 <= hire_amount <= max_hire:
            total_cost = hire_amount * crew_cost
            player["credits"] -= total_cost
            player["crew"] += hire_amount
            print(f"\nHired {hire_amount} new crew members for {total_cost} credits.")
            print(f"New crew total: {player['crew']}")
        else:
            print("Invalid amount.")
    except ValueError:
        print("Please enter a number.")
    
    input("\nPress Enter to continue...")

def check_morale():
    """Check crew morale based on ship conditions and resources"""
    factors = []
    morale_score = 0
    
    # Ship health factor
    if player["ship_health"] >= 80:
        factors.append("Ship is in good condition (+10)")
        morale_score += 10
    elif player["ship_health"] >= 50:
        factors.append("Ship needs some repairs (+0)")
    else:
        factors.append("Ship is in poor condition (-10)")
        morale_score -= 10
    
    # Food factor
    food_per_crew = player["food"] / max(1, player["crew"])
    if food_per_crew >= 30:
        factors.append("Food supplies are plentiful (+10)")
        morale_score += 10
    elif food_per_crew >= 15:
        factors.append("Food supplies are adequate (+5)")
        morale_score += 5
    else:
        factors.append("Food supplies are low (-5)")
        morale_score -= 5
    
    # Oxygen factor
    if player["oxygen"] >= 80:
        factors.append("Oxygen levels are high (+10)")
        morale_score += 10
    elif player["oxygen"] >= 50:
        factors.append("Oxygen levels are adequate (+5)")
        morale_score += 5
    else:
        factors.append("Oxygen levels are concerning (-10)")
        morale_score -= 10
    
    # Reputation factor
    if player["reputation"] >= 70:
        factors.append("Crew is proud of our mission (+10)")
        morale_score += 10
    elif player["reputation"] >= 40:
        factors.append("Mission progress is acceptable (+0)")
    else:
        factors.append("Crew is questioning our mission (-10)")
        morale_score -= 10
    
    # Display morale report
    print("\n=== CREW MORALE REPORT ===")
    for factor in factors:
        print(f"- {factor}")
    
    morale_rating = ""
    if morale_score >= 25:
        morale_rating = "EXCELLENT"
    elif morale_score >= 10:
        morale_rating = "GOOD"
    elif morale_score >= 0:
        morale_rating = "ADEQUATE"
    elif morale_score >= -15:
        morale_rating = "POOR"
    else:
        morale_rating = "CRITICAL"
    
    print(f"\nOverall Morale: {morale_rating} (Score: {morale_score})")
    
    if morale_score < -15:
        print("\nWARNING: Low morale may lead to crew departures if not addressed!")
    
    input("\nPress Enter to continue...")

def view_missions():
    """View and accept available missions"""
    display_header()
    print("\n=== AVAILABLE MISSIONS ===")
    
    # Filter out completed missions
    available_missions = [m for m in missions if m["name"] not in player["missions_completed"]]
    
    if not available_missions:
        print("No missions available at this time.")
        input("\nPress Enter to continue...")
        return
    
    for i, mission in enumerate(available_missions, 1):
        print(f"{i}. {mission['name']} (Difficulty: {mission['difficulty']}/5)")
        print(f"   Location: {mission['planet']}")
        print(f"   Description: {mission['description']}")
        print(f"   Reward: {mission['reward']} credits, +{mission['reputation']} reputation")
        print(f"   Requirements: ", end="")
        req_strings = []
        for resource, amount in mission["requirements"].items():
            req_strings.append(f"{amount} {resource}")
        print(", ".join(req_strings))
        print()
    
    print(f"{len(available_missions) + 1}. Return to Main Menu")
    
    while True:
        try:
            choice = int(input("\nSelect a mission to accept (or return): "))
            if 1 <= choice <= len(available_missions):
                accept_mission(available_missions[choice - 1])
                return
            elif choice == len(available_missions) + 1:
                return
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def accept_mission(mission):
    """Accept and complete a selected mission"""
    print(f"\nMission: {mission['name']}")
    
    # Check if planet has been explored
    if mission["planet"] not in player["explored_planets"]:
        print(f"\nYou need to explore {mission['planet']} before accepting this mission.")
        input("\nPress Enter to continue...")
        return
    
    # Check requirements
    can_complete = True
    for resource, amount in mission["requirements"].items():
        if player[resource] < amount:
            print(f"Not enough {resource}: have {player[resource]}, need {amount}")
            can_complete = False
    
    if not can_complete:
        print("\nYou don't meet the mission requirements.")
        input("\nPress Enter to continue...")
        return
    
    # Confirm mission acceptance
    confirm = input(f"\nAccept mission '{mission['name']}'? This will consume required resources. (y/n): ").lower()
    if confirm != 'y':
        return
    
    # Consume required resources
    for resource, amount in mission["requirements"].items():
        player[resource] -= amount
    
    # Mission success based on difficulty
    success_chance = 100 - (mission["difficulty"] * 10) + (player["reputation"] // 5)
    success_chance = max(20, min(90, success_chance))  # Clamp between 20% and 90%
    
    if random.randint(1, 100) <= success_chance:
        # Mission success
        print(f"\nMission '{mission['name']}' completed successfully!")
        player["credits"] += mission["reward"]
        player["reputation"] += mission["reputation"]
        player["missions_completed"].append(mission["name"])
        
        print(f"Received {mission['reward']} credits.")
        print(f"Reputation increased by {mission['reputation']} points.")
    else:
        # Mission failure
        print(f"\nMission '{mission['name']}' failed!")
        
        # Some compensation
        compensation = mission["reward"] // 4
        player["credits"] += compensation
        player["reputation"] -= mission["reputation"] // 2
        
        print(f"Received {compensation} credits as compensation.")
        print(f"Reputation decreased by {mission['reputation'] // 2} points.")
    
    input("\nPress Enter to continue...")

def end_day():
    """Process the end of a day"""
    display_header()
    print("\n=== END OF DAY ===")
    
    # Calculate food consumption
    food_consumed = player["crew"] * 2
    player["food"] = max(0, player["food"] - food_consumed)
    print(f"Crew consumed {food_consumed} units of food.")
    
    # Calculate oxygen consumption
    oxygen_consumed = player["crew"] * 3
    player["oxygen"] = max(0, player["oxygen"] - oxygen_consumed)
    print(f"Crew consumed {oxygen_consumed} units of oxygen.")
    
    # Ship health natural decay
    if random.random() < 0.3:  # 30% chance of system wear
        decay = random.randint(1, 3)
        player["ship_health"] = max(0, player["ship_health"] - decay)
        print(f"Ship systems experienced wear and tear: -{decay}% health.")
    
    # Check for crew departure due to low morale or resources
    if (player["food"] < player["crew"] * 5 or player["oxygen"] < player["crew"] * 5) and random.random() < 0.3:
        departures = random.randint(1, max(1, player["crew"] // 3))
        departures = min(departures, player["crew"] - 1)  # Ensure at least one crew member remains
        if departures > 0:
            player["crew"] -= departures
            print(f"\nALERT: {departures} crew member(s) have left due to resource shortages!")
    
    # Advance day
    player["day"] += 1
    
    print(f"\nDay {player['day']} begins...")
    
    # Check game over conditions
    if check_game_over():
        return True
    
    input("\nPress Enter to continue...")
    return False

def check_game_over():
    """Check if game over conditions are met"""
    game_over = False
    
    if player["crew"] <= 0:
        print("\n*** GAME OVER ***")
        print("You have lost all your crew members.")
        game_over = True
    
    elif player["ship_health"] <= 0:
        print("\n*** GAME OVER ***")
        print("Your ship has been critically damaged and can no longer function.")
        game_over = True
    
    elif player["oxygen"] <= 0:
        print("\n*** GAME OVER ***")
        print("Your ship has run out of oxygen, causing the crew to suffocate.")
        game_over = True
    
    elif player["food"] <= 0 and player["credits"] < 10:
        print("\n*** GAME OVER ***")
        print("Your crew has starved with no food and no means to buy more.")
        game_over = True
    
    # Victory condition: complete all missions
    elif len(player["missions_completed"]) >= len(missions):
        print("\n*** VICTORY ***")
        print("Congratulations! You have completed all available missions.")
        print(f"Final score: {player['credits']} credits, {player['reputation']} reputation")
        print(f"Days survived: {player['day']}")
        game_over = True
    
    # Alternative victory: reach high reputation
    elif player["reputation"] >= 100:
        print("\n*** VICTORY ***")
        print("Your exceptional leadership has brought you galactic recognition!")
        print(f"Final score: {player['credits']} credits, {player['reputation']} reputation")
        print(f"Days survived: {player['day']}")
        game_over = True
    
    if game_over:
        print("\nThank you for playing COSMIC COMMANDER!")
        input("\nPress Enter to exit...")
    
    return game_over

def main():
    """Main game function"""
    # Check for saved game
    if not load_game():
        intro()
    
    game_ended = False
    while not game_ended:
        choice = main_menu()
        
        if choice == 1:
            explore_planet()
        elif choice == 2:
            trade_resources()
        elif choice == 3:
            ship_maintenance()
        elif choice == 4:
            manage_crew()
        elif choice == 5:
            view_missions()
        elif choice == 6:
            game_ended = end_day()
        elif choice == 7:
            save_game()
            input("\nPress Enter to continue...")
        elif choice == 8:
            confirm = input("Are you sure you want to exit? Unsaved progress will be lost. (y/n): ").lower()
            if confirm == 'y':
                print("\nThank you for playing COSMIC COMMANDER!")
                break

if __name__ == "__main__":
    main()
