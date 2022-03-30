def is_index_valid(index, string):
    if 0 <= index < len(string):
        return True
    return False


initial_string = input()

data = input()

while data != "Travel":
    command, val1, val2 = data.split(":")

    if command == "Add Stop":
        index = int(val1)
        if is_index_valid(index, initial_string):
            initial_string = initial_string[:index] + val2 + initial_string[index:]

    elif command == "Remove Stop":
        index_start = int(val1)
        index_finish = int(val2)
        if is_index_valid(index_start, initial_string) and is_index_valid(index_finish, initial_string):
            initial_string = initial_string[:index_start] + initial_string[index_finish+1:]

    elif command =="Switch":
        if val1 in initial_string:
            initial_string = initial_string.replace(val1, val2)

    print(initial_string)

    data = input()

print(f"Ready for world tour! Planned stops: {initial_string}")