def getRow(rowIndex):
    row = [1]
    for _ in range(1, rowIndex + 1):
        new_row = [1]
        for index in range(1, len(row)):
            new_row.append(row[index - 1] + row[index])
        new_row.append(1)
        row = new_row
    return row


print(getRow(3))
print(getRow(0))
print(getRow(1))
