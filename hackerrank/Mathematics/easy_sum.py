# https://www.hackerrank.com/challenges/easy-sum/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def easy_sum(a, b):
    n = a//b
    k = a%b
    return ((b*(b-1)*n)+(k*(k+1)))//2


if __name__ == "__main__": 
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        print(easy_sum(a, b))


