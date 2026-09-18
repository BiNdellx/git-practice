def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "cannot divided by zero"
    return a / b

print(add(10, 5))
print(sub(10, 5))
print(mul(10, 5))
print(div(10, 5))