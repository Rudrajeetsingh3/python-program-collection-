"""Beginner-friendly Python program collection."""


def factorial(number):
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def fibonacci(count):
    """Return the first `count` Fibonacci numbers."""
    if count < 0:
        raise ValueError("Count cannot be negative.")
    sequence = []
    first, second = 0, 1
    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second
    return sequence


def pairs_to_dictionary(pairs):
    """Convert key-value pairs such as [('name', 'Vidhi')] to a dictionary."""
    return dict(pairs)


if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("First 8 Fibonacci numbers:", fibonacci(8))
    print("Pairs converted to dictionary:",
          pairs_to_dictionary([("name", "Vidhi"), ("course", "CSE")]))
