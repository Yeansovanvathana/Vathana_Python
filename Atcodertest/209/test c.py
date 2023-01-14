# Python3 implementation of the approach
from math import sqrt

MAX = 10**9 + 7
prime = [True] * (MAX + 1);

def SieveOfEratosthenes():
    prime[1] = False;
    for p in range(2, int(sqrt(MAX)) + 1):
        if (prime[p] == True):
            for i in range(p * 2, MAX + 1, p):
                prime[i] = False;
def solve(n):
    count = 0;
    i = 3;
    while count < n:
        if (prime[i]):
            print(i, end=" ");
            count += 1;
        i += 1
if __name__ == "__main__":
    SieveOfEratosthenes();
    n = 6;
    solve(n);
