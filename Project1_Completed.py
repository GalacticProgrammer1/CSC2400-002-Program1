# File: Project1.py
# Author: Jackie Campbell
# Date: September 8, 2023
# Description: This script defines two functions for calculating the greatest common divisor (GCD) of two numbers.

def extended_gcd(a, b):
    """
    Compute the GCD of two integers using the extended Euclidean algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        tuple: A tuple containing three values: the GCD of a and b, and integers x and y
        such that ax + by = GCD(a, b).
    """
    if a == 0:
        return (b, 0, 1)
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return (gcd, x, y)

# Example usage:
a = 48
b = 18
gcd, x, y = extended_gcd(a, b)
print(f"GCD({a}, {b}) = {gcd}")
print(f"x = {x}, y = {y}")

def consecutive_integer_gcd(m, n):
    """
    Compute the GCD of two integers using consecutive integer checking.

    Args:
        m (int): The first integer.
        n (int): The second integer.

    Returns:
        int: The GCD of m and n.
    """
    if m == 0 or n == 0:
        return abs(m) + abs(n)  # GCD of 0 and any number is the other number
    min_val = min(abs(m), abs(n))
    gcd = 1  # Initialize the GCD to 1
    for i in range(2, min_val + 1):
        if m % i == 0 and n % i == 0:
            gcd = i
    return gcd

# Example usage:
m = 48
n = 18
result = consecutive_integer_gcd(m, n)
print(f"GCD({m}, {n}) = {result}")
