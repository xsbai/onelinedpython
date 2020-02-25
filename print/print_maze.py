# print maze

# one line code
print(''.join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))

# is the same as
def print_maze():
    import random
    maze = []
    for x in range(24):
        for y in range(50):
            i = random.choice('\u2571\u2572')
            print(i,end='')
