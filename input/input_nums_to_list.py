# input to list

# one line code
print(list(map(lambda x: int(x) if x.isdigit() else x, input().split(' '))))

# is the same as
def input_to_list():
    num = input()
    num_list = num.split(' ')
    result=[]
    for x in num_list:
        if x.isdigit():
            x = int(x)
        result.append(x)
    print(result)

    