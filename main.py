
from calculator import modulo, max, min, power, abs_val, sqrt, is_odd, is_even, is_positive, is_negative

def main():
    """Main interactive loop for the calculator."""
    print("=== Advanced Calculator ===")
    print("Available operations: modulo, max, min, pow, abs, sqrt, is_odd, is_even, is_positive, is_negative")
    print("Type 'exit' to quit.\n")

    while True:
        operation = input("Enter operation: ").strip().lower()
        if operation == "exit":
            print("Goodbye!")
            break

        if operation not in ["modulo", "max", "min", "pow", "abs", "sqrt", "is_odd", "is_even", "is_positive", "is_negative"]:
            print("Invalid operation. Try again.\n")
            continue

        try:
            if operation in ["modulo", "pow", "max", "min"]:

                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if operation == "modulo":
                    result = modulo(a, b)
                elif operation == "pow":
                    result = power(a, b)
                elif operation == "max":
                    result = max(a, b)
                elif operation == "min":
                    result = min(a, b)

            if operation in ["abs", "sqrt", "is_positive", "is_negative"]:
                
                a = float(input("Enter number: "))

                if operation == "abs":
                    result = abs_val(a)
                elif operation == "sqrt":
                    result = sqrt(a)
                elif operation == "is_positive":
                    result = is_positive(a)
                elif operation == "is_negative":
                    result = is_negative(a)
                
            
            if operation in ["is_even", "is_odd"]:
                
                a = int(input("Enter number: "))

                if operation == "is_even":
                    result = is_even(a)
                elif operation == "is_odd":
                    result = is_odd(a)

            print(f"Result: {result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()