# print love

# one line code
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

# is the same as
def print_love():
    for y in range(30, -30, -1):
        for x in range(-30, 30):
            if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 :
                lovestr = 'Love'[(x-y) % len('Love')] 
                print(lovestr,end='')
            else:
                print(' ',end='')
        print()
