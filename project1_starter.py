import os  # Import the OS module to work with file paths and check if files or directories exist

"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kobby Amadi
Date: 10/31/2025

AI Usage: Google Gemini help with file errors and logic in functions.
"""


def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns a tuple of (strength, magic, health)
    """
    if character_class.lower() == "gladiator":
        # Gladiators have high strength and health but low magic
        strength = 10 + (level * 5)
        magic = 3 + (level * 2)
        health = 100 + (level * 10)
    elif character_class.lower() == "mage":
        # Mages have low strength, high magic, and moderate health
        strength = 4 + (level * 2)
        magic = 12 + (level * 6)
        health = 80 + (level * 8)
    elif character_class.lower() == "ninja":
        # Ninjas are balanced but fast-growing in all stats
        strength = 7 + (level * 4)
        magic = 6 + (level * 3)
        health = 70 + (level * 7)
    elif character_class.lower() == "ranger":
        # Rangers have good balance, especially strong in health and magic
        strength = 6 + (level * 3)
        magic = 10 + (level * 5)
        health = 90 + (level * 9)
    else:
        # Default fallback if an unknown class is entered
        strength = 5 + (level * 3)
        magic = 5 + (level * 3)
        health = 80 + (level * 8)

    # Return the three calculated values as a tuple
    return (strength, magic, health)



def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns: dictionary with keys:
    name, class, level, strength, magic, health, gold
    """
    level = 1  # All new characters start at level 1

    # Calculate base stats based on the character class and starting level
    strength, magic, health = calculate_stats(character_class, level)

    # Store all character data in a dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100  # Every new character starts with 100 gold
    }

    return character  # Return the completed character dictionary



def save_character(character, filename):
    """
    Saves character to text file in specific format.
    Returns True if successful, False if an error occurred.
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # If character data or filename is missing, stop and return False
    if not character or not filename:
        return False

    # Get the directory part of the file path
    directory = os.path.dirname(filename)

    # If the directory doesn’t exist, return False to prevent file errors
    if directory and not os.path.exists(directory):
        return False  

    # Opens the file to creates or overwrites the file
    with open(filename, "w") as file:
        # Write each piece of character information in a formatted way
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")

    # If everything works return True
    return True



def load_character(filename):
    """
    Loads character from text file and returns a dictionary.
    Returns None if file is not found.
    """
    # Checks if the file exists before trying to open it
    if not os.path.exists(filename):
        print("File not found.")
        return None  # If the file doesn't exist it returns None

    # Opens the file and read all lines into a list
    with open(filename, "r") as file:
        lines = file.readlines()

    character = {}  # Temporary dictionary to hold loaded data

    # Process each line from the file to extract key-value pairs
    for line in lines:
        key, value = line.strip().split(": ")  # Split at ": " to separate the field name from its value
        character[key] = value  # Stored in the dictionary

    # Convert the loaded string values into proper data types (integers for numeric fields)
    return {
        "name": character["Character Name"],
        "class": character["Class"],
        "level": int(character["Level"]),
        "strength": int(character["Strength"]),
        "magic": int(character["Magic"]),
        "health": int(character["Health"]),
        "gold": int(character["Gold"])
    }



def display_character(character):
    """
    Prints formatted character sheet.
    """
    # Prints the character sheet
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")



def level_up(character):
    """
    Increases character level and recalculates stats.
    """
    # Increase the level by 1
    character["level"] += 1

    # Recalculate the character’s stats for the new level
    strength, magic, health = calculate_stats(character["class"], character["level"])

    # Update the character’s stats with the new values
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    # Print a message confirming the level up
    print(f"\n{character['name']} leveled up to level {character['level']}!")



if __name__ == "__main__":
    # This section only runs when the script is fully executed
    print("=== CHARACTER CREATOR ===")
    print("Testing functions...")

    # Creates an example character named Aria, who is a Mage
    hero = create_character("Aria", "Mage")

    # Display the character’s current stats
    display_character(hero)

    # Save the character’s data to a text file named "hero.txt"
    save_character(hero, "hero.txt")

    # Load the saved character from the file
    loaded = load_character("hero.txt")

    # If the load is complete, it prints the loaded character's stats from display_character function.
    if loaded:
        print("\nLoaded Character:")
        display_character(loaded)

    # Levels up the hero and show new stats
    level_up(hero)
