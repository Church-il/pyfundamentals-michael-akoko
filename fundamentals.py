# Python Fundamentals Assessment

# Task 1: Function to add two numbers
def add_numbers(num1: float, num2: float) -> float:
    """
    Add two numbers and return the result.
    
    Args:
        num1 (float): The first number to add.
        num2 (float): The second number to add.
    
    Returns:
        float: The sum of num1 and num2.
    """
    return num1 + num2

# Task 2: Function to check if a number is even
def is_even(number: int) -> bool:
    """
    Check if a number is even.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

# Task 3: Function to reverse a string
def reverse_string(text: str) -> str:
    """
    Reverse the given string.
    
    Args:
        text (str): The string to reverse.
    
    Returns:
        str: The reversed string.
    """
    return text[::-1]  # Efficient string slicing for reversal

# Task 4: Function to count vowels in a string
def count_vowels(text: str) -> int:
    """
    Count the number of vowels in the given string.
    Ignores case sensitivity.
    
    Args:
        text (str): The string to count vowels in.
    
    Returns:
        int: The number of vowels in the string.
    """
    vowels = set('aeiou')  # Using a set for efficient lookup
    return sum(1 for char in text.lower() if char in vowels)

# Task 5: Function to calculate factorial
def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n.
    
    Args:
        n (int): The number to calculate factorial for.
    
    Returns:
        int: The factorial of n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Task 6: Decorator function
def decorator_func(func):
    """
    A decorator that prints "Decorator Applied" before calling the original function.
    
    Args:
        func (callable): The function to be decorated.
    
    Returns:
        callable: The wrapped function.
    """
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    """
    Apply the decorator_func to the given function.
    
    Args:
        func (callable): The function to apply the decorator to.
    
    Returns:
        callable: The decorated function.
    """
    return decorator_func(func)

# Task 7: Function to sort list of tuples by age
def sort_by_age(people: list) -> list:
    """
    Sort a list of tuples (name, age) by age in ascending order.
    
    Args:
        people (list): A list of tuples, each containing a name (str) and an age (int).
    
    Returns:
        list: The sorted list of tuples.
    """
    return sorted(people, key=lambda x: x[1])

# Task 8: Function to merge dictionaries
def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merge two dictionaries, summing values for common keys.
    
    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.
    
    Returns:
        dict: A new dictionary with merged key-value pairs.
    """
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

# Task 9: Car class
class Car:
    """
    A class representing a car with make, model, and year attributes.
    """

    def __init__(self, make: str, model: str, year: int):
        """
        Initialize a Car instance.
        
        Args:
            make (str): The make of the car.
            model (str): The model of the car.
            year (int): The year of manufacture of the car.
        """
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self) -> None:
        """
        Display information about the car.
        """
        print(f"{self.year} {self.make} {self.model}")

# Example usage and testing from task 1 to 9
if __name__ == "__main__":
    print(add_numbers(5, 3))  # 8
    print(is_even(4))  # True
    print(reverse_string("hello"))  # "olleh"
    print(count_vowels("Hello World"))  # 3
    print(calculate_factorial(5))  # 120
    
    @apply_decorator
    def greet(name):
        return f"Hello, {name}!"
    print(greet("Alice")) # "Decorator Applied" and then "Hello, Alice!"
    
    people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
    print(sort_by_age(people))  # [('Charlie', 20), ('Alice', 25), ('Bob', 30)]
    
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    print(merge_dicts(dict1, dict2))  # {'a': 1, 'b': 5, 'c': 4}
    
    car = Car("Toyota", "Corolla", 2022)
    car.display_info()  # "2022 Toyota Corolla"