"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kobby Amadi
Date: 10/28/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    if character_class == "Gladiator":
        strength = 10
        magic = 3 
        health = 120 
    elif character_class == "Mage":
        strength = 4 
        magic = 12 
        health = 80 
    elif character_class == "Ninja":
        strength = 7 
        magic = 6 
        health = 90 
    elif character_class == "Ranger":
        strength = 6 
        magic = 10 
        health = 100 
    else:
        # Default stats for unknown class
        strength = 5 
        magic = 5
        health = 100 

    return (strength, magic, health)


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    """
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100

    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }


def save_character(character, filename):
    """
    Saves character to text file in specific format
    """
    try:
        with open(filename, "w") as file:
            file.write(f"Character Name: {character['name']}\n")
            file.write(f"Class: {character['class']}\n")
            file.write(f"Level: {character['level']}\n")
            file.write(f"Strength: {character['strength']}\n")
            file.write(f"Magic: {character['magic']}\n")
            file.write(f"Health: {character['health']}\n")
            file.write(f"Gold: {character['gold']}\n")
        return True
    except:
        return False


def load_character(filename):
    
    """
    Loads character from text file
    """
    with open(filename, "r") as file:
        lines = file.readlines()

        character = {}
        for line in lines:
            key, value = line.strip().split(": ")
            character[key] = value

        return {
            "name": character["Character Name"],
            "class": character["Class"],
            "level": int(character["Level"]),
            "strength": int(character["Strength"]),
            "magic": int(character["Magic"]),
            "health": int(character["Health"]),
            "gold": int(character["Gold"])
        }
    except FileNotFoundError:
        print("File not found.")
        return None


def display_character(character):
    """
    Prints formatted character sheet
    """
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
    Increases character level and recalculates stats
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    print(f"\n{character['name']} leveled up to level {character['level']}!")


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
