#R078A HTTS

n = input("N sonini kiriting: ")

if len(n) % 2 != 0 and all(int(i)%2!=0 for i in n):
    print("YES")
else:
    print("NO")
