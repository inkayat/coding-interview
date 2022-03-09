import math
from functools import reduce


allPrimes = [];
mod = 1000007

def sieve(n): 
 
    prime = [True] * (n + 1); 
 
    p = 2;
    while(p * p <= n):
        if (prime[p] == True):
            i = p * 2;
            while(i <= n): 
                prime[i] = False;
                i += p;
        p += 1; 
    for p in range(2, n + 1): 
        if (prime[p]): 
            allPrimes.append(p);


def _sum(N,  p):
    return  sum([N//(p**i)%mod for i in range(1, int(math.log(N, p))+1)])


def solve(n):
    sieve(n)
    res = list(map(lambda x: (1+2*_sum(n, x))%mod, allPrimes))
    res = reduce(lambda x, y: (x*y)%mod, res, 1)
    ans = res
    return (int(ans))%mod


if __name__ == '__main__':
    n = int(input())

    result = solve(n)

    print(result)
