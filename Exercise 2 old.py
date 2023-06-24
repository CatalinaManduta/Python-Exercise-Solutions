from typing import Union


# 1 Making Choices
# 1.1 Define a function sign(n) that returns the sign of the number n.
def sign(n:int) -> int:
    """
    This function returns the sign of the number n or prints a message if the inserted value is not an integer.

    Args:
        n (int): The value to be checked.

    Returns:
        int: 1 if number is positive;
             0 if number is 0;
             -1 if number is negative.

    Raises:
        ValueError: If the argument is not an integer.
    """
    if n > 0:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return -1
    else:
        raise ValueError('Please enter an integer.')


# 1.2 Define a function to_meters(length,unit) that converts length given in unit to meters.
def to_meters(length:int, unit:str) -> float:
    """
    Converts length given in unit to meters.

    Args:
        length (int): Length to be converted.
        unit (str): The unit of the length to be converted.

    Returns:
        float: The length converted to meters.

    Raises:
        ValueError: If the unit is not one of the predefined units.
    """
    if unit == 'inch' or 'in':
        return length * 0.0254
    elif unit == 'hand'or 'h':
        return length * 0.1016
    elif unit == 'foot' or 'ft':
        return length * 0.3048
    elif unit == 'yard' or 'yd':
        return length * 0.9144
    else:
        raise ValueError("Invalid input")
# print(to_meters(30, "in"))


# 1.3 Write a function print_conversion_table(length) that prints a table with the conversion to meters of length if
# this value is taken in inches, hands, foots, or yards.
def print_conversion_table(length: Union[int, float]) -> None:
    """
        Prints a conversion table of the given length in different units to meters.

        Args:
            length (Union[int, float]): The length to be converted.

        Returns:
            None
        """
    print(length, "in = ", length * 0.0254, "m\n",
    length, "h = ", length * 0.1016, "m\n",
    length, "ft = ", length * 0.3048, "m\n",
    length, "yd = ", length * 0.9144, "m")
# print_conversion_table(30)


# 1.4 Write a program to compute the perimeter and area of a square. The program starts by asking
# the user to input the side of the square (assume it is a floating point number). If the input is
# positive, then it prints the perimeter and the area.

def inp() -> None:
    """
       Asks the user to input the side length of a square (a positive number).
       If the input is positive, it computes and prints the perimeter and the area of the square.

       Args:
           None

       Returns:
           None

       Raises:
           ValueError: If the input is not a positive number.
       """
    side = int(input("Enter the side of the square (a positive number):"))
    if side > 0:
        print("The perimeter of a square of side", side, "is", side*4)
        print("The area of a square of side", side, "is", side*side)
    else:
        raise ValueError("Input should be positive!!!!")
# inp() # because we do not want to run it every time

# 1.5 Write a program to compute the area of circles, rectangles, squares, and triangles. The program
# starts by asking the user to select a shape and, depending on the selection, to input the necessary
# lengths. Then, it prints the area and terminates.
def options() -> None:
    """
       Asks the user to select a shape from a provided list (circle, rectangle, square, or triangle).
       Depending on the user's selection, it then requests the necessary dimensions, calculates,
       and prints the area of the chosen shape.

       Args:
           None

       Returns:
           None

       Raises:
           ValueError: If the shape selection is not within the range of 1-4. It asks the user to try again.
       """
    shape = int(input("Select one of the following shapes by entering the corresponding number: \n1 circle\n2 rectangle\n3 square \n4 triangle"))
    if shape == 1:
        diameter = int(input("Please insert the circle's diameter:"))
        radius = int(input("Please insert the circle's radius:"))
        return print(" The circle circumferince is:", diameter * radius * 3.14)
    elif shape == 2:
        width = int(input("Enter the width of the rectangle:"))
        height = int(input("Enter the height of the rectangle:"))
        return print("The area is", width*height)
    elif shape == 3:
        side = int(input("Enter the side of the rectangle:"))
        return print("The area is", side*side)
    elif shape == 4:
        base = int(input("Enter the base of the triangle:"))
        height = int(input("Enter the height of the triangle:"))
        return print("The area is:", base* height/2)
    else:
        print(" The values must be between 1 and 4. Please try again!!!")
        return options()
# options()

# 2. Recursion
# 2.1. Define a function print_down_triangle(n) that prints a downside “right triangle” with base
# and height n and made of asterisks.
def print_down_triangle(n:int) -> None:
    """
        Prints a "downward" right triangle made of asterisks with a base and height of `n`.

        Args:
            n (int): The base and height of the right triangle.

        Returns:
            None
    """
    for i in range(n, 0, -1):
        print("*" * i)
#print_down_triangle(10)

def down_triangle(n):
    """
            Prints a "downward" right triangle made of asterisks with a base and height of `n`.

            Args:
                n (int): The base and height of the right triangle.

            Returns:
                None
    """
    start = n
    while start > 0:
        print("*" * start)
        start = start - 1
#down_triangle(5)


# 2.2 Define a function print_up_triangle(n) that prints an upside “right triangle”.
def up_triangle(n):
    """
        Prints an "upward" right triangle made of asterisks with a base and height of `n`.

        Args:
            n (int): The base and height of the right triangle.

        Returns:
            None
    """
    start = n
    star = 1
    while star <= n:
        print("*" * (start - (start-star)))
        star += 1
# up_triangle(5)


# 2.3. Write a function print_iso_triangle(n) that prints an upside isosceles triangle made of asterisks.
def print_iso_triangle(n: int) -> None:
    """
    Prints an upward isosceles triangle made of asterisks with a base of `n`.

    Args:
        n (int): The base of the isosceles triangle.

    Returns:
        None
    """
    if (n % 2) == 0:
        print("The value should be an odd number, please try a different number")
    else:
        start = n
        asterix = 1
        space = n - asterix
        while asterix <= n:
            spa = int(space / 2)
            print(" " * spa, "*" * (start - (start - asterix)), " " * spa)
            asterix += 2
            space = n - asterix
# print_iso_triangle(5)



# 2.4 Define a function factorial(n) that returns n!, the factorial of n (n! = 1 · 2 · . . . · n).
def factorial(n: int) -> int:
    """
    Computes the factorial of `n` (n!).

    Args:
        n (int): The value for which the factorial will be computed.

    Returns:
        int: The factorial of `n`.

    Raises:
        ValueError: If an error occurs during computation.
    """
    new = n+1
    ran = range(1, new, 1)
    d = 1
    if n <= 1:
        return 1
    elif n >= 1:
        for i in ran:
            c = i
            d = d*c
        return d
    else:
        raise ValueError("Something went wrong, try again.")
# factorial(5)

# 2.5 Define a function double_factorial(n) that returns n!! (n!! = 1 · 3 · 5 · . . . · n if n is odd and
# n!! = 2 · 4 · 6 · . . . · n if n is even).
def double_factorial(n:int) -> int:
    """
        Computes the double factorial of `n` (n!!), where n!! equals the product of 1, 3, 5, ..., n if n is odd,
        and equals the product of 2, 4, 6, ..., n if n is even.

        Args:
            n (int): The value for which the double factorial will be computed.

        Returns:
            int: The double factorial of `n`.

        Raises:
            ValueError: If an error occurs during computation.
        """
    if n <= 1:
        return 1
    elif n >= 1:
        new = n + 1
        if (n % 2) == 0:
            ran = range(2, new, 2)
            d = 1
            for i in ran:
                c = i
                d = d * c
            print("It is an even number")
            return d
        else:
            ran = range(1, new, 2)
            d = 1
            for i in ran:
                c = i
                d = d * c
            print("It is an odd number", d)
            return d

    else:
        raise ValueError("Invalid argument")
# double_factorial(9)

# 2.6 Define a function gcd(m,n) that returns the greatest common divisor of m and n using Euclides’ algorithm:
def gcd(m: int, n: int) -> int:
    """
        Computes the greatest common divisor of `m` and `n` using Euclid's algorithm.

        Args:
            m (int): First input number.
            n (int): Second input number.

        Returns:
            int: The greatest common divisor of `m` and `n`.
        """
    while n != 0:
        remainder = m % n
        m = n
        n = remainder
    print("Greatest common divisor of m and n using Euclides' algorithm is:", m)
    return m
gcd(23, 10)

# 2.7 Define a function lcm(m,n) that returns the least common multiple of m and n.
def lcm(m:int, n:int) -> int:
    """
       Returns the least common multiple (LCM) of the two numbers m and n.

       This function uses the formula LCM(m, n) = (m * n) / GCD(m, n) where GCD is the greatest common divisor,
       which is calculated by the gcd() function.

       Args:
           m (int): The first number.
           n (int): The second number.

       Returns:
           int: The least common multiple of m and n.

       Raises:
           ValueError: If either of m or n is not a positive integer.
       """
    if m > 0 and n > 0:
        product = m * n
        gcd_1 = gcd(m, n)
        return product / gcd_1
    else:
        raise ValueError("Both numbers should be positive integers.")


# 2.8 Define a function sum_between(m,n) that returns the sum of all integer numbers greater than m and smaller than n.
def sum_between(m: int, n: int) -> None:
    """
    Calculates the sum of all integer numbers greater than m and smaller than n.

    Args:
        m (int): The starting number of the range. (exclusive)
        n (int): The ending number of the range. (inclusive)

    Returns:
        None: It prints the result instead of returning it.

    Raises:
        ValueError: If m is not smaller than n.
    """
    if m < n:
        variable = range(m, n+1, 1)
        total_1 = 0
        for i in variable:
            total_1 += i
        return print("The sum between", m, "and", n , "is", total_1)
    else:
        print("m should be smaller than n")
#sum_between(1, 6)


# 2.9 Define a function sum_even_between(m,n) that returns the sum of all integer even numbers greater than m and
# smaller than n.
def sum_even_between(m:int, n:int) -> None:
    """
    Calculates the sum of all integer even numbers greater than m and smaller than n.

    Args:
        m (int): The starting number of the range. (exclusive)
        n (int): The ending number of the range. (inclusive)

    Returns:
        None: It prints the result instead of returning it.

    Raises:
        ValueError: If m is not smaller than n.
    """
    if m < n:
        variable = range(m, n + 1, 1)
        total_1 = 0
        for i in variable:
            if i % 2 == 0:
                total_1 += i
        return print("The sum between", m, "and", n, "is", total_1)
    else:
        print("m should be smaller than n")
# sum_even_between(1,6)


# 2.10 Define a function sum_odds_between(m,n) that returns the sum of all integer odd numbers greater than m and smaller than n.
def sum_odd_between(m: int, n: int) -> None:
    """
    Calculates the sum of all integer odd numbers greater than m and smaller than n.

    Args:
        m (int): The starting number of the range. (exclusive)
        n (int): The ending number of the range. (inclusive)

    Returns:
        None: It prints the result instead of returning it.

    Raises:
        ValueError: If m is not smaller than n.
    """
    if m < n:
        variable = range(m, n + 1, 1)
        total_1 = 0
        for i in variable:
            if i % 2 != 0:
                total_1 += i
        return print("The sum between", m, "and", n, "is", total_1)
    else:
        print("M should be smaller than n")
# sum_odd_between(1, 6)

# 2.11 Define a function is_prime(n) that given a positive integer n returns True if n is prime and False otherwise.
def is_prime(n:int) -> None:
    """
    Checks if a positive integer n is prime.

    Args:
        n (int): The number to check.

    Returns:
        None: It prints whether the number is prime or not.

    Raises:
        ValueError: If n is not a positive integer.
    """
    data = range(3, n+1, 2)
    if n == 1:
        print(n, "is prime!")
    else:
        for i in data:
            if n % i == 0 and i != n:
                return print(n, "is not a prime number!")
            elif n % i == 0 and i == n:
                return print(n, "is a prime number!")
# is_prime(23)


# 2.12. Define a function input_positive(message) returns a positive integer by asking the user for input (displaying
# message) until a positive integer is provided or a malformed input causes an error.
def input_positive() -> None:
    """
    Prompts the user to input a positive integer until a positive integer is provided.

    Returns:
        None: It prints the entered positive integer.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    inp =  int(input("Please insert an positive integer here:"))
    if inp > 0:
        print("You entered the value:", inp)
    else:
        print(" Please enter a positive integer. Try again!")
        return(input_positive())
# input_positive()
















