def cripto(key, text):
    alpha = {}
    bet = ["A", "B", "C", "D", "E", "F",\
        "G", "H", "I", "J", "K", "L",\
            "M", "N", "O", "P", "Q", "R",\
                "S","T", "U", "V", "W", "X", "Y", "Z"]

    for i in range(26):
        alpha[bet[i]] = bet[i:] + bet[:i]
         
    mensagem = ""
    z = len(key)
    y = 0  
    for i in text:
        if i == " ":
            mensagem += " "
            continue
        else:
            mensagem += alpha[key[y].upper()][bet.index(i.upper())]
        if y == (z-1):
            y = 0
        else:
            y+= 1
    print(mensagem.lower())

cipher = input()
length = int(input())
for i in range(length):
    cripto(cipher, input())
    
# acusou erro de 10 % 
#erro   
#dzzfxvhrlo td qbxrhgocmu hicuittkmg vo qoxz lq tasd ti oqmh auseftwdta guaqprmc...
#dzzfxvhrlo td qbxrhgocmu hicuittkmg vo qoxz lq tasd ti oqmh auseftwdta guaqprmc...

#esperado
#dzzfxvhrlo iv empregarei diogqflcoc va cwjr ds essa ec pxis vudpzudzev gflkqyin...
#dzzfxvhrlo iv empregarei diogqflcoc va cwjr ds essa ec pxis vudpzudzev gflkqyin...

#erro
#dymgswuot srmakcsato sm kbxwcuchdwl
#jem iqzcyx aupog

#esperado
#olimpiada qeemlzytkr dq informatica
#uri online yhhah