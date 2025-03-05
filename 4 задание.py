string = input()
substring = input()
flag = 0
for elem in string:
    if elem == substring:
        flag += 1
print(flag)
