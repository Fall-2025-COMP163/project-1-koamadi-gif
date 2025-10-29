"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kobby Amadi
Date: 10/28/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns a tuple of (strength, magic, health)
    """
    if character_class.lower() == "warrior":
        strength = 10 + (level * 5)
        magic = 3 + (level * 2)
        health = 100 + (level * 10)
    elif character_class.lower() == "mage":
        strength = 4 + (level * 2)
        magic = 12 + (level * 6)
        health = 80 + (level * 8)
    elif character_class.lower() == "rogue":
        strength = 7 + (level * 4)
        magic = 6 + (level * 3)
        health = 70 + (level * 7)
    elif character_class.lower() == "cleric":
        strength = 6 + (level * 3)
        magic = 10 + (level * 5)
        health = 90 + (level * 9)
    else:
        # default fallback
        strength = 5 + (level * 3)
        magic = 5 + (level * 3)
        health = 80 + (level * 8)

    return (strength, magic, health)


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns: dictionary with keys:
    name, class, level, strength, magic, health, gold
    """
    level = 1
    strength, magic, health = calculate_stats(character_class, level)

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }

    return character


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
    Loads character from text file and returns a dictionary.
    Returns None if file is not found.
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
    Prints formatted character sheet.
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
    Increases character level and recalculates stats.
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    print(f"\n{character['name']} leveled up to level {character['level']}!")


# Optional testing block
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Testing functions...")

    # Example usage
    hero = create_character("Aria", "Mage")
    display_character(hero)
    save_character(hero, "hero.txt")

    loaded = load_character("hero.txt")
    if loaded:
        print("\nLoaded Character:")
        display_character(loaded)

    level_up(hero)
