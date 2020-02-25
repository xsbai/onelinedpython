# input matrix to 2D array

# variable
rows = 3

# one line code
#print([list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(rows)])

# is the same as
def input_matrix_to_2D_array():
    result = []
    for n in range(rows):
        row=[]
        lines = input()
        lines_list = lines.split()
        for x in lines_list:
            if x.isdigit():
                x = int(x)
            row.append(x)
        result.append(row)
    print(result)