def fibonacci(max_num):
    number1 = 0
    number2 = 1
    for _ in range(max_num):
        yield number1
        number1, number2 = number2, number1 + number2

for num in fibonacci(6):
    print(num)
