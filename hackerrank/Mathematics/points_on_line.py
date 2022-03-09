# https://www.hackerrank.com/challenges/points-on-a-line/problem

def is_points_on_line(points_x, points_y):
    return len(set(points_x)) == 1 or len(set(points_y)) == 1


if __name__ == "__main__":
    points_x, points_y = [], []
    for i in range(int(input())):
        xy = list(map(int, input().split()))
        points_x.append(xy[0])
        points_y.append(xy[1])
    if is_points_on_line(points_x, points_y):
        print("YES")
    else:
        print("NO")


