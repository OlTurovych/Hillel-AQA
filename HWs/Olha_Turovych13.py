import math
import re
from typing import Tuple


def open_file() -> str:
    """
    This function opens a file and reads its content

    outcome: str
    """
    with open("seventh_lesson/file1.txt", "r") as f:
        equation = f.read()
    return equation


def find_values(equation: str) -> Tuple:
    """
    This function searches for a, b, c coefficients in the equation using regex

    param: str
    outcome: tuple
    """
    pattern = r"(?P<a>\d*)x\^2\s*[-+]?\s*(?P<b>\d*)x\s*[-+]?\s*(?P<c>\d*)"
    match = re.match(pattern, equation)
    if match:
        a = int(match.group("a")) if match.group("a") else 1
        b = int(match.group("b")) if match.group("b") else 1
        c = int(match.group("c")) if match.group("c") else 0
        return a, b, c
    else:
        raise ValueError("Invalid equation format: ax^2 + bx + c = 0")


def discriminant_calculate(a: float, b: float, c: float) -> float:
    """
    Calculates the discriminant of a quadratic equation.
    Returns a float representing the discriminant.
    """
    return b**2 - 4 * a * c


def calculate_roots(a: float, b: float, c: float, d: float) -> Tuple[float, float]:
    """
    Calculates the roots of a quadratic equation given the coefficients and discriminant.
    Returns a tuple of two floats representing the roots (root1, root2).
    Raises a ValueError if the discriminant is negative.
    """
    if d >= 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return root1, root2
    else:
        raise ValueError("The discriminant is negative!")


def write_results(root1: float, root2: float) -> None:
    """
    This function writes the roots of the quadratic equation

    params: float
    """
    with open(
        "/Users/olhaturovych/Documents/Python automation/AQA /python_class2205/seventh_lessonfile2.txt",
        "w",
    ) as f:
        f.write(f"x1 = {root1}\n")
        f.write(f"x2 = {root2}\n")


def main():
    equation = open_file()
    a, b, c = find_values(equation)
    discriminant = discriminant_calculate(a, b, c)
    root1, root2 = calculate_roots(a, b, c, discriminant)
    write_results(root1, root2)


if __name__ == "__main__":
    main()
