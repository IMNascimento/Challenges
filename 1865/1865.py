teste = int(input())

for x in range(teste):
    palavra = input().split()
    palavra[1] = int(palavra[1])
    
    match palavra[0]:
        case 'Thor':
            print("Y")
        case _:
            print("N")