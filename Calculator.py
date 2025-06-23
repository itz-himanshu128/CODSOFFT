def get_number(num):
    while True:
        try:
            return float(input(num))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    print("\nChoose operation:")
    print(" Addition (+)")
    print(" Subtraction (-)")
    print(" Multiplication (*)")
    print(" Division (/)")
    
    while True:
        choice = input("Enter choice ( +, -, *, / ): ")
        if choice in ['+', '-', '*', '/']:
            return choice
        else:
            print("Please enter  +, -, *, / ")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2, '+'
    elif operation == '-':
        return num1 - num2, '-'
    elif operation == '*':
        return num1 * num2, '*'
    elif operation == '/':
        if num2 == 0:
            return None, '/'
        return num1 / num2, '/'

def main():
    print("=== CALCULATOR ===")
    
    while True:
        # Get user input
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operation = get_operation()
        
        # Perform calculation
        result, symbol = calculate(num1, num2, operation)
        
        # Display result
        if result is None:
            print("Error: Cannot divide by zero!")
        else:
            print(f"\nResult: {num1} {symbol} {num2} = {result}")
        
        # Ask to continue
        if input("\nDo another calculation? (y/n): ").lower() != 'y':
            print("Thanks for using the calculator!")
            break
        print()

# Run the calculator
main()