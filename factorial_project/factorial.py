"""Factorial program: computes n! iteratively and recursively."""


def factorial(n: int) -> int:
    """Return n! using iteration. Raises ValueError for negative input."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Return n! using recursion."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    try:
        n = int(input("Enter a non-negative integer: "))
        print(f"{n}! = {factorial(n)}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
