def elso():
    print("I/A:")
    jnev:str=str(input("Játékos neve: "))
    szerepkor:str=str(input("szerepkör: "))
    
    
    v:str="varázsló"
    h:str="harcos"
    print("I/B:")
    if szerepkor==v:
        print(f"Üdvözlunk {jnev},2 életed van!")
    elif(szerepkor==h):
        print(f"Üdvözlünk {jnev}, 10 életed van!")
    else:
        print(f"Üdvözlünk {jnev}, 8 életed van!")
