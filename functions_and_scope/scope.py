x = 30  # Global variable

def print_x():
    x = 25  # Local variable
    print(f"Local x: {x}")

print_x()
print(f"Global x: {x}")


count = 1

def increment():
    global count
    count += 2
    print(f"Count: {count}")

increment()
increment()
print(f"Final count: {count}")

def outer():
    x = "outside"

    def inner():
        nonlocal x
        x = "inside"
        print(f"inside x: {x}")

    inner()
    print(f"outsidde x: {x}")

outer()


