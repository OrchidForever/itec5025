# Assignment 5

## Author
Brenna Auker

With help with Github Copilot

## Class
ITEC 5025

## Project Structure

```
Assignment 05/
├── adventures/
│   └── adventure.py          # Main adventure class with async methods and translation 
├── data/
├   ├── stories.py            # Main JSON data for the various stories.
├── genres/
│   ├── __init__.py
│   ├── horror.py             # Horror storyline (mostly developed with choices)
│   └── mystery.py            # Mystery storyline (basic implementation)
├── texts/
│   ├── greeting.py           # Welcome messages
│   ├── exit.py               # Farewell messages
│   ├── print_error.py        # Error handling messages
│   └── translate.py          # Translation functionality using Google Translate API
├── terminal_outputs/         # Sample outputs and screenshots
├── data_set.py               # User input processing and game state
└── README.md
├── user_input.py             # Main file the processes what the user inputed. 
```

## How to Run

1. Navigate to the project directory:
   ```bash
   cd "Assignment 05"
   ```

2. Run the main application:
   ```bash
   python data_set.py
   ```

## How to Play

Currently, the **horror** genre is the most developed storyline.

1. **Choose a Genre**: Select from the available adventure types
2. **Create Your Character**: Enter your character's name and description
3. **Make Choices**: Follow the prompts and make decisions
4. **Exit Anytime**: Type 'stop' to end your adventure

## Current Development Status

- 🔧 **Horror**: Basic developed storyline with multiple choices and outcomes
- 🚧 **Mystery**: Basic character creation implemented
- 🚧 **Alternative History**: Character creation and basic setup
- 🚧 **Fantasy**: Character creation and basic setup  
- 🚧 **Science Fiction**: Character creation and basic setup

## Bugs

- Translations are not always right. May need to add spaces to ensure the translation comes out better. Or more words? But then it messes up how I am looking for choices. Might to rethink my keywords to make it work better overall.
- MAN there is no space between my input and the printed text. Looks bad man.
- When the sub choice is made, and it's incorrect, it will bounce you back to the first choice. Need to fix that.
- ~~Exiting now causes issues (ctrl + c). Has to do with async/await~~ Fixed by wrapping my call to main in try catch.
- ~~Refactor the choices to more readable functions. They getting long~~ Using a dataset solved this problem.