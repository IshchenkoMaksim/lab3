import math

x1 = int(input('Enter coordinates, first x1, then y1: '))
y1 = int(input())
x2 = int(input('Enter coordinates, first x2, then y2: '))
y2 = int(input())

x = math.pow(x2 - x1, 2)
y = math.pow(y2 - y1, 2)
dist = math.sqrt(x + y)

print('Distance is equal to:', dist)