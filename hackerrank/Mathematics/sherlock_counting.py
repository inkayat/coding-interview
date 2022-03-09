import math

def solve(n, k):
    if k>=n:
        return n-1
    # fst, snd, td = n-1, 2*n-4, 3*n-9
    # d = (snd-fst)-(td-snd)
    # eq = (n-1)*p - (p)*(p+1)
    try:
        d = math.sqrt(n**2-4*n*k)
    except:
        return n-1
    x1, x2 = (n-d)//2, (n+d)//2
    root = min(x1, x2)
    return int(min(root*2, n-1))

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = solve(n, k)
        print(result)
