#M022A Simmetrik nuqta

t = int(input())

for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())

    x = 2 * x2 - x1
    y = 2 * y2 - y1

    print(x, y)