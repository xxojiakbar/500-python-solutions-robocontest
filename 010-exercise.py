# R047C Omadli chipta

n = input()
if len(n) == 6:
    a, b, c, d, e, f = map(int, n)
    if a + b + c == d + e + f:
        print("Yes")
    else:
        print("No")
else:
    print("No")
    