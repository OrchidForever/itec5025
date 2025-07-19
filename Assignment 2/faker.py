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

def print_greeting():
    print("Hello! I am a silly goose of a bot here to assist you with basic arithmetic and comparisons.")
    print("You can ask me questions like:")
    print("What is 5 + 6?")
    print("Is -1 equal to 10?")
    print("To end the chat session, simply type 'stop'")
    print("Let's get started!")

def print_exit():
    print("Thank you for chatting with me!")
    print("I hope I was able to assist you.")
    print("Goodbye!")

def print_error_processing():
    print("Yikes.")
    print("I didn't understand that request.")
    print("Can you try to rephrase it?")
    print("If you need help, you can type 'help' for examples of what I can do.")
    
def print_help():
    print("Here are some examples of how I can assist you:")
    print("1. What is 5 + 6?")
    print("2. Is -1 equal to 10?")
    print("3. To end the chat session, simply type 'stop'")
    print("Feel free to ask me any arithmetic or comparison questions!")

def process_arithmetic(input_str: str):
    words = input_str.lower().split()
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
        clean_word = word.strip('?.,;:')
        # print(f"Processing word: {clean_word}")
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
        return calculate(numbers[0], numbers[1], operation)
    return None

def process_or_operation(input_str: str):
    """Process OR operations like '5 > 3 or 2 < 1'"""
    # Split by 'or'
    parts = input_str.lower().split(' or ')
    
    if len(parts) == 2:
        # Process each part as a separate comparison
        result1 = process_arithmetic(parts[0].strip())
        result2 = process_arithmetic(parts[1].strip())
        
        # Implement OR logic
        final_result = result1 or result2
        print("Drumroll please...or not.")
        print(f"The result is: {final_result}")
        return True
    
    return False

def process_and_operation(input_str: str):
    """Process AND operations like '5 > 3 and 2 < 1'"""
    # Split by 'and'
    parts = input_str.lower().split(' and ')
    
    if len(parts) == 2:
        # Process each part as a separate comparison
        result1 = process_arithmetic(parts[0].strip())
        result2 = process_arithmetic(parts[1].strip())
        
        # Implement AND logic
        final_result = result1 and result2
        print("Aaaaand drumroll....")
        print(f"The result is: {final_result}")
        return True
    
    return False

def process_not_operation(input_str: str):
    """Process NOT operations like 'not 5 > 3'"""
    # Split by 'not'
    parts = input_str.lower().split('not')
    
    if len(parts) == 2:
        # Process the part after 'not'
        result = process_arithmetic(parts[1].strip())
        
        # Implement NOT logic
        final_result = not result
        print("No drumroll for this one...")
        print(f"The result is: {final_result}")
        return True
    
    return False

def process_logical(input_str: str):
    """Handle logical operations like AND, OR, NOT"""
    words = input_str.lower().split()
    
    # Look for logical operators
    if 'or' in words:
        return process_or_operation(input_str)
    elif 'and' in words:
        return process_and_operation(input_str)
    elif 'not' in words:
        return process_not_operation(input_str)
    
    # Fall back to arithmetic processing
    print("Drumroll please...")
    result = process_arithmetic(input_str)
    print(f"The result is: {result}")
    return result is not None

def main():
    try:   
        print_greeting()
        
        while True:
            user_input = input("Please enter your request: ")
            
            if user_input.lower() == 'stop':
                printExit()
                break
            
            # Process arithmetic operations
            if process_logical(user_input):
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