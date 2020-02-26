# print multiplication formula

# one line code
print('\n'.join([' '.join(["%2s x%2s = %2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))

# is the same as
def print_multiplication_formula():
    for i in range(1,10):
        for j in range(1,i+1):
            formula = "%2s x%2s = %2s " % (j,i,i*j)
            print(formula,end='')
        print()
