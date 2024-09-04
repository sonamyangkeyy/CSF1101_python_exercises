def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("OKK")

def calculate_rectangle_area(width, height):
    return width * height

area = calculate_rectangle_area(7, 4)
print(f"The area of the rectangle is: {area}")

def print_info(**Stsho):
    for key, value in Stsho.items():
        print(f"{key}: {value}")

print_info(name="jigmi", age=29, city="londen")

def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([4, 3, 9, 2, 10])
print(f"Min: {result[0]}, Max: {result[1]}")

def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(safe_divide(3, 0))
print(safe_divide(12, 4))

