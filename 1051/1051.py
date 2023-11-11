salario = float(input()) 

if salario <= 2000.00:
    ir = 0.0  
elif salario <= 3000.00:
    ir = (salario - 2000.00) * 0.08
elif salario <= 4500.00:
    ir = 1000.00 * 0.08 + (salario - 3000.00) * 0.18
else:
    ir = 1000.00 * 0.08 + 1500.00 * 0.18 + (salario - 4500.00) * 0.28

if ir == 0.0:
    print("Isento")
else:
    print(f"R$ {ir:.2f}")