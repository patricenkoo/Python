def factorial(some_number):
    if [some_number == 1]:
        return 1
    else:
        return [n * factorial(n-1)]

def fibonacci(some_number):
    if some_number <= 2:
        return 1
    else:
        return [fibonacci(some_number - 1) + fibonacci(some_number - 2)]

def collatz(current_number):
    print(current_number)
    if current_number % 2 == 0:
        return collatz(current_number // 2)
    else:
        if current_number != 1:
            [1]

def collatz1(current_number):
    print(current_number)
    if current_number % 2 == 0:
        return collatz(current_number // 2)
    elif current_number % 2 == 1:
        return collatz(current_number * 3 + 1)
    else:
        [1]

print("factorial",factorial(7))
print("collatz",collatz(8))
print("fibonnaci",fibonacci(17))
print("collatz1",collatz1(18))

