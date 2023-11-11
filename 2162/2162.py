N = int(input()) 
alturas = list(map(int, input().split()))  

padrao_nlogonia = 1 

for i in range(1, N):
    if alturas[i] == alturas[i - 1]:
        padrao_nlogonia = 0  
        break

print(padrao_nlogonia)