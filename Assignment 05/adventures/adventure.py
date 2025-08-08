## Basic adventure class
from typing import Any
import asyncio


from genres.horror import start_horror, choice_horror, end_horror_story
from genres.mystery import start_mystery
from texts.translate import translate_text, translate_text_print

class Adventure:
    """A simple class to represent an adventure."""
    ## ["alternative history", "fantasy", "science fiction", "mystery", "horror"]
    genre: str = ""
    character_name: str = ""
    character_description: str = ""
    emoji: str = "🎤"

    def __init__(self, genre: str):
        self.genre = genre

    async def start(self, language: str) -> str:
        """Start the adventure based on the genre."""
        if self.genre == "alternative history":
            await self.start_alternative_history(language)
            self.emoji = "✈️"
        elif self.genre == "fantasy":
            await self.start_fantasy(language)
            self.emoji = "🧙‍♂️"
        elif self.genre == "science fiction":
            await self.start_science_fiction(language)
            self.emoji = "🚀"
        elif self.genre == "mystery":
            self.characterName, self.characterDescription, self.emoji = await start_mystery()
        elif self.genre == "horror":
            self.emoji = await start_horror(language)
        else:
            _ = await translate_text_print("Unknown genre. Adventure cannot be started.", language)

        return self.emoji
    
    async def start_alternative_history(self, language: str):
        text = "Starting an alternative history adventure...\n\n"
        text += "I'm thinking of some fun scenarios in a different timeline after world war 1...\n"
        text += "Imagine a steampunk type world where technology stalled after world war 1...\n"
        text += "Planes are the most desired mode of transportation, and airships are the norm.\n"
        text += "You are a pilot in this world, and you have a mission to deliver a secret package.\n"
        text += "You will encounter various challenges and characters along the way.\n"
        text += "You will encounter various challenges and characters along the way.\n"
        _ = await translate_text_print(text, language)
        # Implement the logic for alternative history adventure here
        # For example, ask for character name, description, etc.
        character_name_text = await translate_text("What's your pilot's name: ", language)
        character_description_text = await translate_text("Describe your pilot: ", language)
        self.characterName = input(character_name_text)
        self.characterDescription = input(character_description_text)
        final_text = f"Well {self.characterName}, let's get this plane in the air!"
        _ = await translate_text_print(final_text, language)

    async def start_fantasy(self, language: str):
        text = "Starting a fantasy adventure...\n"
        text += "Imagine a world filled with magic, mythical creatures, and epic quests.\n"
        text += "You are a brave adventurer on a quest to save the kingdom from an ancient evil.\n"
        _ = await translate_text_print(text, language)
        # Implement the logic for fantasy adventure here
        character_name_text = await translate_text("What's your character's name: ", language)
        character_description_text = await translate_text("Describe your character: ", language)
        self.characterName = input(character_name_text)
        self.characterDescription = input(character_description_text)
        final_text = f"Welcome {self.characterName}, your journey begins now!"
        _ = await translate_text_print(final_text, language)

    async def start_science_fiction(self, language: str):
        text = "Starting a science fiction adventure...\n"
        text += "Imagine a future where humanity has colonized other planets and advanced technology is the norm.\n"
        text += "You are a space explorer on a mission to discover new worlds and civilizations.\n"
        _ = await translate_text_print(text, language)
        # Implement the logic for science fiction adventure here
        character_name_text = await translate_text("What's your explorer's name: ", language)
        character_description_text = await translate_text("Describe your explorer: ", language)
        self.characterName = input(character_name_text)
        self.characterDescription = input(character_description_text)
        final_text = f"Greetings {self.characterName}, prepare for liftoff!"
        _ = await translate_text_print(final_text, language)

    async def first_choice(self, user_input: str, language: str, step = 1) -> int:
        points = 0
        if self.genre == "alternative history":
            await self.start_alternative_history(language)
        elif self.genre == "fantasy":
            await self.start_fantasy(language)
        elif self.genre == "science fiction":
            await self.start_science_fiction(language)
        elif self.genre == "mystery":
            self.characterName, self.characterDescription, self.emoji = await start_mystery()
        elif self.genre == "horror":
            points = await choice_horror(user_input, language, step)
        else:
            error_text = "Unknown genre. Cannot process first choice."
            _ = await translate_text_print(error_text, language)
        
        return points

    async def second_choice(self, user_input: str, language: str, step = 2) -> int:
        points = 0
        if self.genre == "alternative history":
            points = await self.process_alternative_history_choice(user_input, language)
        elif self.genre == "fantasy":
            points = await self.process_fantasy_choice(user_input, language)
        elif self.genre == "science fiction":
            points = await self.process_science_fiction_choice(user_input, language)
        elif self.genre == "mystery":
            points = await self.process_mystery_choice(user_input, language)
        elif self.genre == "horror":
            points = await choice_horror(user_input, language, step)
        else:
            error_text = "Unknown genre. Cannot process second choice."
            _ = await translate_text_print(error_text, language)

        return points

    async def end_story(self, language: str, points: int) -> str:
       if self.genre == "horror":
           return await end_horror_story(language, points)