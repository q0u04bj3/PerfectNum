import sys

def is_perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

for i in range(1,len(sys.argv)):
    print is_perfect (int(sys.argv[i]))
