#R058E VAQT

vaqt = input().split(":")
h = int(vaqt[0])
m = int(vaqt[1])
t = int(input())
jami = h * 60 + m + t
h = (jami // 60) % 24
m = jami % 60 
print(f"{h:02d}:{m:02d}")


