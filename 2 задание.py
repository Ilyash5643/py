biology_command = int(input())
programming_command = int(input())
up_to = biology_command * programming_command + 1
for i in range(max(biology_command, programming_command), up_to):
    if i % biology_command == 0 and i % programming_command == 0:
        print(i)
        break
