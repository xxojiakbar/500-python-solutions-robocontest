#R059B Robo Password
n = input()

yigindi = 0

for son in n:
    yigindi += int(son)
    
if len(n) == 9 and n[0] != "0" and yigindi % 2 == 1:
    print("yes")
else:
    print("no")
