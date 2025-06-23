def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        choice = input("Enter choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Please enter 1, 2, 3, or 4.")

def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2, '+'
    elif operation == '2':
        return num1 - num2, '-'
    elif operation == '3':
        return num1 * num2, '*'
    elif operation == '4':
        if num2 == 0:
            return None, '/'
        return num1 / num2, '/'

def main():
    print("=== SIMPLE CALCULATOR ===")
    
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