# Python Fundamentals Assessment - Michael Akoko

This repository contains the implementation of various fundamental Python concepts, including functions, decorators, data structures, and object-oriented programming. The code is designed to demonstrate an understanding of basic programming principles in Python.


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage Instructions](#usage-instructions)
- [Code Structure](#code-structure)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)


## Overview

The main goal of this project is to implement essential Python functionalities and demonstrate best coding practices. The assessment consists of functions for mathematical operations, string manipulation, and more, as well as a simple `Car` class showcasing object-oriented programming.


## Features

- **Mathematical Functions**: 
  - `add_numbers`: Returns the sum of two numbers.
  - `is_even`: Checks if a number is even.
  - `calculate_factorial`: Computes the factorial of a non-negative integer.

- **String Manipulation**:
  - `reverse_string`: Reverses a given string.
  - `count_vowels`: Counts the vowels in a string, ignoring case sensitivity.

- **Decorator**:
  - `apply_decorator`: Applies a simple decorator to demonstrate the decorator concept in Python.

- **Data Structures**:
  - `sort_by_age`: Sorts a list of tuples by age in ascending order.
  - `merge_dicts`: Merges two dictionaries, summing values for common keys.

- **Object-Oriented Programming**:
  - `Car` class: Represents a car with attributes like make, model, and year, and includes a method to display its information.


## Requirements

- Python 3.7+
- pipenv (for dependency management)


## Setup Instructions

To set up this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/pyfundamentals-michael-akoko.git
   cd pyfundamentals-michael-akoko
   ```

2. **Set Up Virtual Environment**:
   ```bash
   pipenv install
   ```

3. **Activate the Virtual Environment**:
   ```bash
   pipenv shell
   ```


## Usage Instructions

1. **Run the Main Script**:
   ```bash
   python fundamentals.py
   ```
   This will execute all the implemented functions and demonstrate the `Car` class functionality.

2. **Using Individual Functions**:
   You can import and use individual functions in your Python scripts or interactive shell:
   ```python
   from fundamentals import add_numbers, reverse_string, Car
   
   result = add_numbers(5, 3)
   reversed_text = reverse_string("Hello")
   my_car = Car("Toyota", "Corolla", 2022)
   my_car.display_info()
   ```


## Code Structure

- `fundamentals.py`: Contains all implemented functions and the `Car` class.
- `README.md`: This file, containing project documentation.


## Testing

The `fundamentals.py` file includes basic test cases for each function and the `Car` class. To run these tests:

```bash
python fundamentals.py
```

For more comprehensive testing, consider adding unit tests using Python's `unittest` or `pytest` framework.


## Contributing

Contributions to improve the code or documentation are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.