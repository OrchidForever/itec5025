from texts.greeting import print_greentings
from user_input import UserInput
from texts.exit import print_exit
    
def main():
    try:   
        print_greentings()
        user = UserInput()
        while True:
            user_input = input(f"{user.emoji}: ")

            if user_input.lower() == 'stop':
                print_exit()
                break
            # Process user input
            if user.process_input(user_input):
                continue
            
            # If no processing was done, print an error message
            print_error_processing()
    except KeyboardInterrupt:
        print("\n\nOh! Looks like you pressed Ctrl+C. Instead of stop. Rude.")
        print("Goodbye! 🦆")
    except EOFError:
        print("\n\nInput stream ended.")
        printExit()

if __name__ == "__main__":
    main()