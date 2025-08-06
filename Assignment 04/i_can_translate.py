from texts.greeting import print_greetings
from user_input import UserInput
from texts.exit import print_exit
from texts.print_error import print_error
from texts.translate import translate_text_print

async def main():
    try:
        print(print_greetings())
        user: UserInput = UserInput()
        while True:
            user_input: str = input(f"{user.emoji}: ")

            if user_input.lower() == 'stop':
                print_exit()
                break
            if 'language' in user_input.lower():
                language: str = input("Enter the destination language code (e.g., 'es' for Spanish): ")
                try:
                    await user.set_language(language)
                except Exception as e:
                    print("Not a valid language code.")
                
                await translate_text_print(print_greetings(), language)
                continue
            elif await user.process_input(user_input):
                continue
            
            # If no processing was done, print an error message
            print_error()
    except KeyboardInterrupt:
        print("\n\nOh! Looks like you pressed Ctrl+C. Instead of stop. Rude.")
        print("Goodbye! 🦆")
    except EOFError:
        print("\n\nInput stream ended.")
        print_exit()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())