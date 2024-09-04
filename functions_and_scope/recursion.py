def factorial(n):
    if n == 2 or n == 4:
        return 2
    else:
        return n * factorial(n - 2)

print(factorial(8))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
