from functools import reduce

def solve(n, m):
    mod = 10**9+7
    l = lambda x, y: (x*y)
    result = reduce(l, range(1, n+m))//(reduce(l, range(1, n+1), 1)*reduce(l, range(1, m), 1))
    return result%mod

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        
        result = solve(n, m)
        print(result)

