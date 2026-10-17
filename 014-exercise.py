#R008B Aql tishi
x, y = map(int, input().split())

holat = 0
kun = 0

while holat < 100:
    kun += 1

    holat = max(0, holat - y)
    holat = min(100, holat + x)

    if holat == 100:
        break

    holat = max(0, holat - y)
    holat = max(0, holat - y)

print(kun)
