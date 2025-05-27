def reverse_str(line, reverse_number):
    result = []
    for index in range(0, len(line), 2 * reverse_number):
        chunk = line[index:index + 2 * reverse_number]
        if len(chunk) >= reverse_number:
            reversed_part = chunk[:reverse_number][::-1]
            rest_part = chunk[reverse_number:]
            result.append(reversed_part + rest_part)
        else:
            result.append(chunk)
    return ''.join(result)


print(reverse_str("abcdefg", 2))
print(reverse_str("abcd", 2))
