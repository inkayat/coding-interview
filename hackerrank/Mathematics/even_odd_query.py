# https://www.hackerrank.com/challenges/even-odd-query/problem

def find(x, y, A):
    if x<=y:
        return (A[x-1]%2==0 and x==y) or (A[x-1]%2==0 and A[x]!=0) or A[x-1] == 0
    return False

def solve(A, queries):
    for x, y in queries:
        yield find(x, y , A)

if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(arr, queries)
    for res in result:
        if res:
            print("Even")
        else:
            print("Odd")
