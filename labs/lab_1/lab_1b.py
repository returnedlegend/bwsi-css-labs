"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

# global variable declaration
num2: float = 0.0  # will be assigned in `main` and can be accessed by other functions if needed

def request_sanitized_number(prompt: str) -> float:
    """
    Function to request a number from the user and ensure that it is a valid float.

    Args:
        prompt (str): The message to display when asking for input.
    Returns:
        float: The sanitized number input by the user.\
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def request_sanitized_operation(prompt: str) -> str:
    """
    Function to request an operation from the user and ensure that it is valid.

    Args:
        prompt (str): The message to display when asking for input.

    Returns:
        str: The sanitized operation input by the user.
    """
    valid_operations = ["add", "subtract", "multiply", "divide"]
    while True:
        operation = input(prompt).strip().lower()
        if operation in valid_operations:
            return operation
        else:
            print("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
def sanitized_division(num1: float, num2_arg: float) -> float:
    """
    Function to perform division while handling division by zero.

    This version updates the module-level `num2` whenever the denominator
    is re-requested, ensuring the global reflects any correction so that the
    final print statement in `main()` shows the current value.

    Args:
        num1 (float): The numerator.
        num2_arg (float): The initial denominator value (typically passed
            from `simple_calculator`).

    Returns:
        float: The result of the division.
    """
    # write-through to the global variable so callers see updates
    global num2
    num2 = num2_arg

    while True:
        try:
            if num2 != 0:
                return num1 / num2
            else:
                raise ValueError("Cannot divide by zero.")
        except ValueError as undefined:
            print(f"Error: {undefined}")
            num2 = request_sanitized_number("Enter a non-zero denominator: ")

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        # use sanitized division helper which also updates the global `num2`
        return sanitized_division(num1, num2)
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def main():
    
    # declare that we intend to modify the module‑level `num2`
    global num2

    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = request_sanitized_number("Enter the first number: ")
    # assign to the global variable instead of a local one
    num2 = request_sanitized_number("Enter the second number: ")
    operation = request_sanitized_operation("Enter the operation (add, subtract, multiply, divide): ")

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()