import sys

def is_perfect(n):
    return sum([i for i in range(1,n+1) if n%i == 0]) == 2*n

for i in range(1,len(sys.argv)):
    print is_perfect (int(sys.argv[i]))
