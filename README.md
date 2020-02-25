# one line in python

Programming problems achieved in one line

# Input
## 1. Input to list
```python
print(list(map(lambda x: int(x) if x.isdigit() else x, input().split(' '))))
```

## 2. Input lines to list
```python
# rows = 10
print(list(map(lambda x: int(x) if x.isdigit() else x,[input() for _ in range(rows)])))
```

## 3. Input matrix to 2D array
```python
# rows = 10
print([list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(rows)])
```

# Print
## 1. Print multiplication formula
```python
print('\n'.join([' '.join(["%2s x%2s = %2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
```

## 2. Print maze
```python
print(''.join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))
```

## 3. Print love
```python
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
```

## 4. Print Mandelbrot
```python
print('\n'.join([''.join(['*'if abs((lambda a: lambda z, c, n: a(a, z, c, n))(lambda s, z, c, n: z if n == 0 else s(s, z*z+c, c, n-1))(0, 0.02*x+0.05j*y, 40)) < 2 else ' ' for x in range(-80, 20)]) for y in range(-20, 20)]))
```

## 5. Print Infinite character animation
```python
while 1: import random; print(random.choice('^_^'), end='')
```

# Operation
## 1. Array flatten
```python
# array = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
flatten = lambda x: [y for l in x for y in flatten(l)] if isinstance(x, list) else [x]
# print(flatten(array))
```

## 2. list to array
```python 
# x,y = [1,2,3,4,5,6,7,8,9],3
array = lambda x,y: [x[i:i+y] for i in range(0, len(x), y)]
# print(array(x,y))
```

## 3. Rotate 2D array
```python
# array = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print([[i, j, k] for i, j, k in zip(*array)])
```

# Calculate
## 1. Calculate the prime number between 1-n
```python
# n = 100
print(' '.join([str(item) for item in filter(lambda x: all(map(lambda p: x % p != 0, range(2, x))), range(2, n+1))]))
```

## 2. Calculate fibonacci series in Top n 
```python
# n = 10
print([x[0] for x in [(a[i][0], a.append([a[i][1], a[i][0]+a[i][1]])) for a in ([[1, 1]], ) for i in range(30)]])
```

## 3. Calculate Pascal triangle in line n
```python
# n = 10
[print(" ".join(map(str, x))) for x in [[[1]]+[[item.append([1] + [item[i][j]+item[i][j+1] for j in range(len(item[-1])-1)] + [1]), item][-1][-1] for item in [ [[1]] ] for i in range(n-1)]][0]]
```

## 4. Calculate FizzBuzz between 1-n
```python
# n = 100
[print("fizz"[x % 3 * 4:]+"buzz"[x % 5 * 4:] or x) for x in range(1, n+1)]
```

# Algorithm
## 1. Quick sort
```python
# arr = [1,4,3,7,8,2,5,9]
qsort = lambda arr: len(arr) > 1 and qsort(list(filter(lambda x: x <= arr[0], arr[1:]))) + arr[0:1] + qsort(list(filter(lambda x: x > arr[0], arr[1:]))) or arr
# print(qsort(arr))
```

## 2. Eight queens
```python
[__import__('sys').stdout.write('\n'.join('.' * i + 'Q' + '.' * (8-i-1) for i in vec) + "\n========\n") for vec in __import__('itertools').permutations(range(8)) if 8 == len(set(vec[i]+i for i in range(8))) == len(set(vec[i]-i for i in range(8)))]
```

## 3. Word count
```python
# from collections import Counter
# string = "Hi! Mi fans? Are you ok?"
[print("{} : {}".format(k, v)) for k, v in Counter(string.split(" ")).items()]
```


```python

```