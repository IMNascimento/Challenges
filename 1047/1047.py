d= input()
z = d.split()
hi = int(z[0])
mi = int(z[1])
hf = int(z[2])
mf = int(z[3])

if(hi == mi == hf == mf):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif(hi > hf):
    calci=(hi*60)+mi
    calcf=((hf+24)*60)+mf 
    result =calci - calcf 
    time = abs(result)//60
    minutos =  abs(result) % 60
    print(f"O JOGO DUROU {abs(time)} HORA(S) E {abs(minutos)} MINUTO(S)")
elif(hi == hf  and mf < mi):
    calci=(hi*60)+mi
    calcf=((hf+24)*60)+mf 
    result =calci - calcf 
    time = abs(result)//60
    minutos =  abs(result) % 60
    print(f"O JOGO DUROU {abs(time)} HORA(S) E {abs(minutos)} MINUTO(S)")
else:
    calci=(hi*60)+mi
    calcf=(hf*60)+mf 
    result =calci - calcf 
    time = abs(result)//60
    minutos = abs(result) % 60
    print(f"O JOGO DUROU {abs(time)} HORA(S) E {abs(minutos)} MINUTO(S)")