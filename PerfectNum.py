import sys

def is_perfect(n):
    return sum([i for i in range(1,n) if n%i == 0]) == n

for i in range(1,len(sys.argv)):
    print is_perfect (int(sys.argv[i]))
