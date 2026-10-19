
L = int(input())
R = int(input())
N = int(input())

kichik = 0
katta = 0

for son in range(L, R + 1):
    yigindi = sum(map(int, str(son)))

    if yigindi == N:
        if kichik == 0:
            kichik = son
        katta = son

print(kichik)
print(katta)
