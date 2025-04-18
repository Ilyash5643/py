number = input()
check = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '0': 0
}
for digit in number:
    check[digit] += 1
print(check)
