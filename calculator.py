# calculator.py
import math
import time

def square_root(x):
    """Calculates the square root of a number."""
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return math.sqrt(x)

def factorial(x):
    """Calculates the factorial of a non-negative integer."""
    if not isinstance(x, int) or x < 0:
        return "Error: Factorial is only defined for non-negative integers."
    return math.factorial(x)

def natural_log(x):
    """Calculates the natural logarithm of a positive number."""
    if x <= 0:
        return "Error: Natural logarithm is only defined for positive numbers."
    return math.log(x)

def power(base, exponent):
    """Calculates the power of a number."""
    return math.pow(base, exponent)

def main_menu():
    """Displays the main menu and gets user choice."""
    print("\n--- Scientific Calculator ---")
    print("1. Square Root (√x)")
    print("2. Factorial (!x)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power Function (x^b)")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def run_calculator():
    """Main function to run the calculator loop."""
    while True:
        choice = main_menu()
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        try:
            if choice == '1':
                num = float(input("Enter a number to find the square root: "))
                print(f"Result: {square_root(num)}")
            elif choice == '2':
                num = int(input("Enter a non-negative integer to find the factorial: "))
                print(f"Result: {factorial(num)}")
            elif choice == '3':
                num = float(input("Enter a positive number to find the natural logarithm: "))
                print(f"Result: {natural_log(num)}")
            elif choice == '4':
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                print(f"Result: {power(base, exponent)}")
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        time.sleep(2)

if __name__ == "__main__":
    run_calculator()