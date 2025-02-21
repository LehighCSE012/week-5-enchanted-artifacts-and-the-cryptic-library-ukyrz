import random

def display_player_status(player_stats):
    """Displays the player's current stats."""
    print(f"Health: {player_stats['health']}, Attack: {player_stats['attack']}")

def discover_artifact(player_stats, artifacts, artifact_name):
    """Handles discovering and using artifacts."""
    if artifact_name in artifacts:
        artifact = artifacts.pop(artifact_name)  # Remove artifact once found
        print(f"You found {artifact_name}: {artifact['description']}")
        
        if artifact['effect'] == "increases health":
            player_stats['health'] += artifact['power']
        elif artifact['effect'] == "enhances attack":
            player_stats['attack'] += artifact['power']
        
        print(f"Effect: {artifact['effect']} (+{artifact['power']})")
    else:
        print("You found nothing of interest.")
    return player_stats, artifacts

def find_clue(clues, new_clue):
    """Handles finding unique clues."""
    if new_clue in clues:
        print("You already know this clue.")
    else:
        clues.add(new_clue)
        print(f"You discovered a new clue: {new_clue}")
    return clues

def enter_dungeon(player_stats, inventory, dungeon_rooms, clues, artifacts):
    """Handles exloration"""
    if not isinstance(dungeon_rooms, list) or not all(isinstance(room, tuple) and len(room) == 4 for room in dungeon_rooms):
        raise TypeError("dungeon_rooms must be a list of 4-element tuples")
    
    for room in dungeon_rooms:
        room_name, item, challenge_type, challenge_outcome = room
        print(f"You have entered {room_name}.")
        
        if item:
            print(f"You found a {item}!")
            inventory.append(item)
        
        if challenge_type == "puzzle":
            if not isinstance(challenge_outcome, tuple) or len(challenge_outcome) != 3:
                raise TypeError("Puzzle challenges must have a 3-element outcome tuple")
            success, fail, penalty = challenge_outcome
            print("You encountered a puzzle!")
            if "key" in inventory:  # Example condition
                print(success)
            else:
                print(fail)
                player_stats["health"] -= penalty
        
        elif challenge_type == "trap":
            if not isinstance(challenge_outcome, tuple) or len(challenge_outcome) != 3:
                raise TypeError("Trap challenges must have a 3-element outcome tuple")
            success, fail, penalty = challenge_outcome
            print("You triggered a trap!")
            if player_stats["health"] > penalty:
                print(success)
                player_stats["health"] -= penalty
            else:
                print(fail)
                player_stats["health"] = 0
        
        elif challenge_type == "library":
            print("You found an ancient library with cryptic texts.")
            clues.add("ancient text fragment")
        
        elif challenge_type == "none":
            print("This room is empty.")
        else:
            print(f"Unknown challenge type: {challenge_type}. Skipping room.")
    
    print("Dungeon exploration complete.")

def main():
    """Main game loop."""
    dungeon_rooms = [
        {"description": "Dusty library", "item": "key", "challenge_type": "puzzle"},
        {"description": "Narrow passage, creaky floor", "item": "torch", "challenge_type": "trap"},
        {"description": "Grand hall, shimmering pool", "item": "healing potion", "challenge_type": "none"},
        {"description": "Small room, locked chest", "item": "treasure", "challenge_type": "puzzle"},
        {"description": "Cryptic Library", "item": None, "challenge_type": "library"}
    ]

    player_stats = {'health': 100, 'attack': 5}
    inventory = []
    clues = set()
    artifacts = {
        "amulet_of_vitality": {"description": "A glowing amulet that enhances your life force.", "power": 15, "effect": "increases health"},
        "ring_of_strength": {"description": "A powerful ring that boosts your attack damage.", "power": 10, "effect": "enhances attack"},
        "staff_of_wisdom": {"description": "A staff imbued with ancient wisdom.", "power": 5, "effect": "solves puzzles"}
    }
    
    display_player_status(player_stats)
    
    if random.random() < 0.3 and artifacts:
        artifact_name = random.choice(list(artifacts.keys()))
        player_stats, artifacts = discover_artifact(player_stats, artifacts, artifact_name)
        display_player_status(player_stats)
    
    player_stats, inventory, clues = enter_dungeon(player_stats, inventory, dungeon_rooms, clues)
    print("\n--- Game End ---")
    display_player_status(player_stats)
    print(f"Final Inventory: {inventory}")
    print("Clues:")
    for clue in clues:
        print(f"- {clue}")

if __name__ == "__main__":
    main()
