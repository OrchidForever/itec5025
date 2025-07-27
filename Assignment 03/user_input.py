from adventures.adventure import Adventure

# Step 0: Get the genre the user wants to explore, Get the users desired type of setting, Get the users character name and description
# Step 1: Start branching path of genre story
class UserInput:
    step = 0
    emoji = "🎤"
    def __init__(self):
        self.user_input = ""

    def process_input(self, user_input: str):
        self.user_input = user_input
        if(self.step == 0):
            if(self.process_genre(self.user_input)):
                self.adventure = Adventure(self.genre)
                self.emoji = self.adventure.start()
                self.step = 1
                return True
            else:
                print("Please choose a valid genre from the list.")
                return False
        elif(self.step == 1):
            points = self.adventure.first_choice(self.user_input)
            if points == 0:
                print("Please make a valid choice.")
            else:
                self.points = points
                self.step = 2
            return True

        

    def is_exit_command(self):
        return self.user_input.lower() == 'stop'

    def process_genre(self, user_input: str):
        """Process the genre input from the user."""
        genres = ["alternative history", "fantasy", "science fiction", "mystery", "horror"]
        for genre in genres:
            if genre in user_input.lower():
                print(f"You have chosen the genre: {genre.title()}\n\n")
                self.genre = genre
                self.step = 1
                return True
        
        print("Please choose a valid genre from the list.")
        return False

    def process_choice_1(self, user_input: str):
        """Process the first choice input from the user."""
        print(f"You chose: {self.emoji} {user_input}")