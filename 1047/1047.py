d= input()
z = d.split()
minutos = (int(z[0])*60+int(z[1]))-(int(z[2])*60+int(z[3]))
hours = abs(minutos)//60
calc = hours * 60
result = calc - abs(minutos)
if(z[0] == z[1] == z[2] == z[3]):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print(f"O JOGO DUROU {hours} HORA(S) E {abs(result)} MINUTO(S)")