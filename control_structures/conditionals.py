number = 10 
if number > 0:
    print("the number is positive.")
else: 
    print("the number is non-positive.")

number = 0 
if number > 0:
    print("The number id positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

score = 85
if score >= 90:
    grate = "A"
elif score >= 80:
    grate = "B"
elif score >= 70:
    grate = "c"
elif score >= 60:
    grate = "D"
else:
    grate = "F"
print(f"your grade is: {grate}")

number = 7
result = "even" if number % 2 == 0 else "odd"
print(f"the number is {result}.")

num1 = 10
num2 = 5
operator = "+"
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
else:
    result = "Error: Invalid operator"
print(f"Result: {result}")




