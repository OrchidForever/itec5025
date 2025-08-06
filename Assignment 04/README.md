# Assignment 4

## Author
Brenna Auker

With help with Github Copilot

## Class
ITEC 5025

## Project Structure

```
Assignment 04/
├── adventures/
│   └── adventure.py          # Main adventure class with async methods and translation support
├── genres/
│   ├── __init__.py
│   ├── horror.py             # Horror storyline (fully developed with choices)
│   └── mystery.py            # Mystery storyline (basic implementation)
├── texts/
│   ├── greeting.py           # Welcome messages
│   ├── exit.py               # Farewell messages
│   ├── print_error.py        # Error handling messages
│   └── translate.py          # Translation functionality using Google Translate API
├── terminal_outputs/         # Sample outputs and screenshots
├── user_input.py             # User input processing and game state
├── i_can_translate.py        # Main application entry point with translation support
└── README.md
```

## How to Run

1. Navigate to the project directory:
   ```bash
   cd "Assignment 04"
   ```

2. Run the main application:
   ```bash
   python i_can_translate.py
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

## NEW Bugs

- ~~Emoji is unhappy. it always says none.~~ Fixed when doing code review with Github Copilot
- Translations are not always right. May need to add spaces to ensure the translation comes out better.
- MAN there is no space between my input and the printed text. Looks bad man.
- Exiting now causes issues (ctrl + c). Has to do with async/await
- Refactor the choices to more readable functions. They getting long