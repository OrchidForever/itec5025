from adventures.adventure import Adventure
from texts.translate import translate_text, translate_text_print

class UserInput:
    step: int = 0
    emoji: str = "🎤"
    language: str = "en"
    genre: str = ""
    points: int = 0
    adventure: None | Adventure = None

    def __init__(self):
        self.user_input = ""

    async def process_input(self, user_input: str) -> bool:
        """Process the user input based on the current step."""
        self.user_input = user_input
        if(self.step == 0):
            if(await self.process_genre(self.user_input)):
                self.adventure = Adventure(self.genre)
                self.emoji = await self.adventure.start(self.language)
                self.step = 1
                return True
            else:
                error_text = f"Invalid genre: {self.user_input}. Please choose a valid genre from the list."
                _ = await translate_text_print(error_text, self.language)
                return False
        elif(self.step == 1 and self.adventure):
            points = await self.adventure.first_choice(self.user_input, self.language)
            if points == 0:
                error_text = f"Invalid choice: {self.user_input}. Please make a valid choice."
                _ = await translate_text_print(error_text, self.language)
            else:
                self.points += points
                self.step = 2
        elif(self.step == 2 and self.adventure):
            points = await self.adventure.second_choice(self.user_input, self.language)
            if points == 0:
                error_text = f"Invalid choice: {self.user_input}. Please make a valid choice."
                _ = await translate_text_print(error_text, self.language)
            else:
                self.points += points
                self.step = 3
        
        return True

    async def process_genre(self, user_input: str):
        """Process the genre input from the user."""
        genres = ["alternative history", "fantasy", "science fiction", "mystery", "horror"]
        translated_genres = []
        for genre in genres:
            genre_text = await translate_text(genre, self.language)
            translated_genres.append(genre_text)
        for i, genre in enumerate(translated_genres):
            if genre in user_input.lower():
                text = f"You have chosen the genre: {genres[i]}\n\n"
                _ = await translate_text_print(text, self.language)
                self.genre = genres[i]
                self.step = 1
                return True

        _ = await translate_text_print("Invalid genre. Please choose from the list. ", self.language)
        return False

    async def process_choice_1(self, user_input: str):
        """Process the first choice input from the user."""
        text = "You chose: {self.emoji} {user_input}"
        _ = await translate_text_print(text, self.language)

    async def set_language(self, language: str):
        """Set the language for the user."""
        self.language = language
        _ = await translate_text_print(f"Language has been set to code: {self.language}", self.language)