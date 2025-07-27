## Basic adventure class
from genres.horror import start_horror, first_choice
from genres.mystery import start_mystery

class Adventure:
    """A simple class to represent an adventure."""
    ## ["alternative history", "fantasy", "science fiction", "mystery", "horror"]
    genre = ""
    characterName = ""
    characterDescription = ""
    emoji = "🎤"
    def __init__(self, genre):
        self.genre = genre

    def start(self):
        if self.genre == "alternative history":
            self.start_alternative_history()
            self.emoji = "✈️"
        elif self.genre == "fantasy":
            self.start_fantasy()
            self.emoji = "🧙‍♂️"
        elif self.genre == "science fiction":
            self.start_science_fiction()
            self.emoji = "🚀"
        elif self.genre == "mystery":
            self.characterName, self.characterDescription, self.emoji = start_mystery()
        elif self.genre == "horror":
            self.characterName, self.characterDescription, self.emoji = start_horror()
        else:
            print("Unknown genre. Adventure cannot be started.")
        return self.emoji

    def start_alternative_history(self):
        print("Starting an alternative history adventure...")
        print("I'm thinking of some fun scenarios in a different timeline after world war 1...")
        print("Imagine a steampunk type world where technology stalled after world war 1...")
        print("Planes are the most desired mode of transportation, and airships are the norm.")
        print("You are a pilot in this world, and you have a mission to deliver a secret package.")
        print("You will encounter various challenges and characters along the way.")
        # Implement the logic for alternative history adventure here
        # For example, ask for character name, description, etc.
        self.characterName = input("What's your pilot's name: ")
        self.characterDescription = input("Describe your pilot: ")
        print(f"Well {self.characterName}, let's get this plane in the air!")

    def start_fantasy(self):
        print("Starting a fantasy adventure...")
        print("Imagine a world filled with magic, mythical creatures, and epic quests.")
        print("You are a brave adventurer on a quest to save the kingdom from an ancient evil.")
        # Implement the logic for fantasy adventure here
        self.characterName = input("What's your character's name: ")
        self.characterDescription = input("Describe your character: ")
        print(f"Welcome {self.characterName}, your journey begins now!")

    def start_science_fiction(self):
        print("Starting a science fiction adventure...")
        print("Imagine a future where humanity has colonized other planets and advanced technology is the norm.")
        print("You are a space explorer on a mission to discover new worlds and civilizations.")
        # Implement the logic for science fiction adventure here
        self.characterName = input("What's your explorer's name: ")
        self.characterDescription = input("Describe your explorer: ")
        print(f"Greetings {self.characterName}, prepare for liftoff!")

    def first_choice(self, user_input: str):
        if self.genre == "alternative history":
            self.start_alternative_history()
        elif self.genre == "fantasy":
            self.start_fantasy()
        elif self.genre == "science fiction":
            self.start_science_fiction()
        elif self.genre == "mystery":
            self.characterName, self.characterDescription, self.emoji = start_mystery()
        elif self.genre == "horror":
            points = first_choice(user_input)
        else:
            print("Unknown genre. Cannot process first choice.")
            points = 0
        
        return points