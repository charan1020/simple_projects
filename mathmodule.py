import math
from math import sqrt, factorial
def calculate_square_root(number):
    return sqrt(number) 
def calculate_factorial(number):
    return factorial(number)
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
def power(base, exponent):
    return base ** exponent
def logarithm(number, base=10):
    return math.log(number, base)
def sine(angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    return math.sin(angle_in_radians)
def cosine(angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    return math.cos(angle_in_radians)
def tangent(angle_in_degrees):

    angle_in_radians = math.radians(angle_in_degrees)
    return math.tan(angle_in_radians)
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
print("LCM of 12 and 15 is:", lcm(12, 15))
print("Square root of 16 is:", calculate_square_root(16))
print("Factorial of 5 is:", calculate_factorial(5))
print("Is 7 prime?:", is_prime(7))
print("GCD of 54 and 24 is:", gcd(54, 24))
print("2 raised to the power 3 is:", power(2, 3))
print("Logarithm of 1000 base 10 is:", logarithm(1000))
print("Sine of 30 degrees is:", sine(30))
print("Cosine of 60 degrees is:", cosine(60))
print("Tangent of 45 degrees is:", tangent(45))
print("Factorial of 6 using recursion is:", factorial_recursive(6))

