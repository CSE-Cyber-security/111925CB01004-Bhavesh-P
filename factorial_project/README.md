# Factorial Program

A simple Python project that calculates the factorial of a number, with unit tests and sample output.

## Folder Structure

```
factorial_project/
├── factorial.py        # Main program (iterative + recursive versions)
├── test_factorial.py   # Unit test cases
├── output.txt          # Sample program output and test results
└── README.md           # This file
```

## Requirements

- Python 3.7 or higher (no external libraries needed)

## How to Run

Run the program:

```bash
python factorial.py
```

Example:

```
Enter a non-negative integer: 5
5! = 120
```

## How to Run the Tests

```bash
python test_factorial.py
```

## Test Cases Covered

| Test                        | Input      | Expected            |
|-----------------------------|------------|---------------------|
| Zero                        | 0          | 1                   |
| One                         | 1          | 1                   |
| Small numbers               | 5, 6       | 120, 720            |
| Large number                | 20         | 2432902008176640000 |
| Negative input              | -3         | ValueError          |
| Non-integer input           | 3.5        | TypeError           |
| Recursive == iterative      | 0 to 14    | Same results        |
| Recursive negative input    | -1         | ValueError          |

## How It Works

- `factorial(n)` multiplies numbers from 2 up to `n` using a loop.
- `factorial_recursive(n)` calls itself with `n - 1` until it reaches 1.
- Both reject negative numbers and non-integers.
