"""
A program to sum the first 50 fibonacci sequence.
"""

def fibonacci(n):
    sequence = [1, 1]
    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)
    return sequence

generated_sequece = (fibonacci(50))
fibonacci_sum = sum(fibonacci(50))
print(f"The first 50 fibonacci sequence is {generated_sequece}")
print(f"The sum of the first 50 fibonacci sequence is {fibonacci_sum}")


