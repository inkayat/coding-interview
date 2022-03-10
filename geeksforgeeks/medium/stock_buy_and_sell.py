#https://practice.geeksforgeeks.org/problems/stock-buy-and-sell2615/1/#


def stockBuySell(price, n): 
    found, x, y = True, 0, 0
    while x < n-1 and price[x+1]<=price[x]:
        x+=1
    y = x+1
    while y < n:
        if y==n-1:
            if price[y]>price[x]:
                found = False
                print("("+str(x)+" "+str(y)+")", end=" ")
        elif price[y]>price[y+1]:
            found = False
            print("("+str(x)+" "+str(y)+")", end=" ")
            x = y+1
            while x < n-1 and price[x+1]<=price[x]:
                x+=1
            y = x
        y+=1
    if found==True:
        print("No Profit", end="")
    print()
        
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        price=list(map(int, input().split()))
        stockBuySell(price, n)
