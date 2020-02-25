# input lines to list

# variable
rows = 3

# one line code
print(list(map(lambda x: int(x) if x.isdigit() else x,[input() for _ in range(rows)])))

# is the same as
def input_lines_to_list():
    result = []
    for n in range(rows):
        x = input()
        if x.isdigit():
            x = int(x)
        result.append(x)
    print(result)
