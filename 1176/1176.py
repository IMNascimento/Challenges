fibonacci = [0,1]

for i in range(2,62):
    calc = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(calc)
    
teste = int(input())

for j in range(1, teste+1):
    n = int(input())
    print(f"Fib({n}) = {fibonacci[n]}")