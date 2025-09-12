import math

# Quadratic Equation Solver


def solve_quadratic(a, b, c):
    """Solves ax^2 + bx + c = 0 for real roots."""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return ()

if __name__ == "__main__":
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    roots = solve_quadratic(a, b, c)
    if roots:
        print("Roots:", roots)
    else:
        print("No real roots.")