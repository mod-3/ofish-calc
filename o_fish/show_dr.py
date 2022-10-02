import math

max = 100
min = 50
current = 100
points = 0
remaining = 1382000
days = 0

while current >= min:
    days = math.ceil(remaining/(current*1000))
    print(current)
    print(" - ")
    print(days)
    current = current-5