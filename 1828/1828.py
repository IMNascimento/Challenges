T = int(input())  # Lê o número de casos de teste

for caso in range(1, T + 1):
    escolhas = input().split()  # Lê as escolhas de Sheldon e Raj
    sheldon, raj = escolhas

    if sheldon == raj:
        resultado = "De novo!"
    elif (
        (sheldon == "pedra" and (raj == "lagarto" or raj == "tesoura")) or
        (sheldon == "papel" and (raj == "pedra" or raj == "Spock")) or
        (sheldon == "tesoura" and (raj == "papel" or raj == "lagarto")) or
        (sheldon == "lagarto" and (raj == "Spock" or raj == "papel")) or
        (sheldon == "Spock" and (raj == "tesoura" or raj == "pedra"))
    ):
        resultado = "Bazinga!"
    else:
        resultado = "Raj trapaceou!"

    print(f"Caso #{caso}: {resultado}")