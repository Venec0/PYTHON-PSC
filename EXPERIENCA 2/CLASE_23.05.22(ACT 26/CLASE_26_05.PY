while True:
    id=input("INGRESE CÓDIGO: ")
    if len(id)==4:
        if id[0:1].isalpha():
            if id[1:4].isnumeric():
                break
            else:
                print("NO ES NUMÉRICO.")
        else:
            print("NO ES UNA LETRA.")
    else:
        print("LARGO NO VÁLIDO.")