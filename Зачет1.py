line = input().upper().split()
new_line = ''
for word in line:
    if word[0].isalpha():
        new_line += word[0]
print(new_line)
