''' present the user with a a meaningful greeting
    take in user input
    process that input by storing it into variables, performing type casts, and checking the input for specific commands
    based on the input perform at least one of each of the following types of operations
        arithmetic
        comparison
        boolean comparison
    document your test cases

   Failed [('5 = 5', True), ('5 > 3', True), ('3 < 5', True), ('5 >= 5', True), ('3 <= 5', True), ('5 != 3', True)]
'''
from utils import calculate

def printGreeting():
    print("Hello! I am a silly goose of a bot here to assist you with basic arithmetic and comparisons.")
    print("You can ask me questions like:")
    print("What is 5 + 6?")
    print("Is -1 equal to 10?")
    print("To end the chat session, simply type 'stop'")
    print("Let's get started!")

def printExit():
    print("Thank you for chatting with me!")
    print("I hope I was able to assist you.")
    print("Goodbye!")

def printErrorProcessing():
    print("Yikes.")
    print("I didn't understand that request.")
    print("Can you try to rephrase it?")
    print("If you need help, you can type 'help' for examples of what I can do.")
    
def printHelp():
    print("Here are some examples of how I can assist you:")
    print("1. What is 5 + 6?")
    print("2. Is -1 equal to 10?")
    print("3. To end the chat session, simply type 'stop'")
    print("Feel free to ask me any arithmetic or comparison questions!")

def processArithmetic(input: str):
    words = input.lower().split()
    # Look for operation keywords
    operations = {
        'plus': '+', 'add': '+', 'added': '+', 'sum': '+', '+': '+',
        'minus': '-', 'subtract': '-', 'subtracted': '-', 'difference': '-', '-': '-',
        'times': '*', 'multiply': '*', 'multiplied': '*', 'product': '*', '*': '*',
        'divided': '/', 'divide': '/', 'division': '/', '/': '/',
        'equal': '=', 'equals': '=', '=': '=', '==': '=',
        'greater': '>', 'less': '<', 'greater than': '>', 'less than': '<', '<': '<', '>': '>',
        'greater than or equal to': '>=', '>=': '>=',
        'less than or equal to': '<=', '<=': '<=',
        'not equal': '!=', '!=': '!=',
    }
    operation_symbols = ['+', '-', '*', '/', '=', '>', '<', '>=', '<=', '!=']
    
    numbers = []
    operation = None
    
    for word in words:
        # Try to convert word to number
        # print(f"Processing word: {word}")
        clean_word = word.strip('?!.,;:')
        print(f"Cleaned word: {clean_word}")
        for op_symbol in operation_symbols:
            # If we found an operation symbol, we can extract numbers
            if op_symbol in clean_word:
                parts = clean_word.split(op_symbol)
                if len(parts) == 2:
                    try:
                        num1 = float(parts[0])
                        num2 = float(parts[1])
                        numbers.extend([num1, num2])
                        operation = op_symbol
                        break
                    except ValueError:
                            continue
        if operation is None or len(numbers) < 2:
            try:
                num = float(clean_word)
                numbers.append(num)
            except ValueError:
                # Check if it's an operation keyword
                if clean_word in operations:
                    operation = operations[clean_word]
        

    # Process if we found numbers and an operation
    if len(numbers) >= 2 and operation:
        print(f"Numbers found: {numbers}, Operation: {operation}")
        result = calculate(numbers[0], numbers[1], operation)
        print("Drumroll please...")
        print(f"The result is: {result}")
        return True
    
    print (numbers, operation)
    return False

def main():
    try:   
        printGreeting()
        
        while True:
            user_input = input("Please enter your request: ")
            
            if user_input.lower() == 'stop':
                printExit()
                break
            
            # Process arithmetic operations
            if processArithmetic(user_input):
                continue
            
            # If no processing was done, print an error message
            printErrorProcessing()
    except KeyboardInterrupt:
        print("\n\nOh! Looks like you pressed Ctrl+C. Instead of stop. Rude.")
        print("Goodbye! 🦆")
    except EOFError:
        print("\n\nInput stream ended.")
        printExit()

if __name__ == "__main__":
    main()