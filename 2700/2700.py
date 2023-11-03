convidados = int(input())
lista_convidados = []
doacao = 0
for x in range(convidados):
    b, f, d = map(int, input().split())
    lista_convidados.append([int(b),int(f), int(d)])
    
for i,pc in enumerate(lista_convidados):
    bonito = 0
    rico = 0
    for j, pj in enumerate(lista_convidados):
        if i != j: 
            if pc[0] == pc[1]:
                bonito += 3
                rico += 3
            if (pc[0] - pj[0]) > 2:
                bonito += 1
            if (pc[1] - pj[1]) > 2 :
                rico += 1
    
    if bonito >= 1 or rico >= 1:
        doacao += lista_convidados[int(i)][2]       
        
print(doacao)

#não concluido erro de time exception