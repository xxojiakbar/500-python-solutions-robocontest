x, y = map(int, input().split())

kun = 0
holati = 0

while holati < 100:
    kun += 1
    holati -= y
    holati += x 
    
    if holati >= 100:
        break
    
    holati -= y 
    holati -= y 
    
    if holati < 0:
        holati = 0
print(kun)
    