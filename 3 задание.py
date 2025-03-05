line = input()
check_repeat = 0
new_line = ''
for letter in range(len(line) - 1):
    if line[letter + 1] == line[letter]:
        check_repeat += 1
    else:
        check_repeat += 1
        new_line = new_line + line[letter] + str(check_repeat)
        check_repeat = 0
if line[-1] == line[len(line) - 2]:
        check_repeat += 1
        new_line = new_line + line[-1] + str(check_repeat)
else:
    check_repeat += 1
    new_line = new_line + line[-1] + str(check_repeat)
    check_repeat = 0
print(new_line)
