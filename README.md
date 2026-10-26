# 111925CB01004-Bhavesh-P

# Simple Calculator in C

A command-line calculator written in C that performs basic arithmetic on two numbers.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Handles decimal numbers (uses `double`)
- Error handling for division by zero and invalid operators

## Requirements

- A C compiler such as GCC

## Compile

```bash
gcc calculator.c -o calculator
```

## Run

```bash
./calculator
```

On Windows:

```bash
calculator.exe
```

## Usage

The program asks for an operator first, then two numbers.

```
Enter an operator (+, -, *, /): +
Enter two numbers: 12 8
12.00 + 8.00 = 20.00
```

```
Enter an operator (+, -, *, /): /
Enter two numbers: 10 0
Error: Division by zero is not allowed.
```

```
Enter an operator (+, -, *, /): %
Enter two numbers: 5 2
Error: Invalid operator.
```

## How It Works

1. Reads the operator character with `scanf`.
2. Reads the two operands as `double` values.
3. Uses a `switch` statement to pick the operation and print the result.
4. Checks that the divisor is not zero before dividing.

## File Structure

```
.
├── calculator.c
└── README.md
```

## License

Free to use and modify for learning purposes.
