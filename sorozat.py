import random

def masodik():
    lista=[]
    i=0
    print("II/A, B, C:")
    while (i <= 7):
        dobas:int = int(random.randint(0,1))
        lista.append(dobas)
        if dobas == 0:
            if i == 7:
                print("FEJ")
            else:
                print("FEJ", end="-")
        elif dobas == 1:
            if i == 7:
                print("ÍRÁS")
            else:
                print("ÍRÁS", end="-")
        i += 1
    return lista
    
def fejek_szama(lista):
    fejek:int=0
    for i in range(0,len(lista),1):
        if lista[i]==0:
            fejek+=1
    return fejek

def konzol_kiir(fejek):
    print("II/D, E:")
    print(f"A fejek száma: {fejek}.")

def file_kiir(fejek):
    fajlom = open("fejek.txt", "w", encoding="UTF-8")
    
    fajlom.write("II/F")
    fajlom.write(f"A fejek száma: {fejek}.")
    fajlom.close() 