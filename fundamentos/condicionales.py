

def ejemplo_if_elif():

    lista = [1,2,3]

    condicion = len(lista) == 1
    if(len(lista) == 2) :
        print("Entre al if\n")

    elif len(lista) == 1:
        print("Entre al elif\n")
    
    else:
        print("Entre al else\n")



    # if len(lista) == 0:
    #     print("Lista vacia")
    # elif len(lista) == 1:
    #     print("Lista con un elemento")
    # else:
    #     print("Else lista no esta cubierta por los casos")

    i = 0
    #i <= 10 -> [0, 10]
    #i < 10 -> [0, 10)
    #i >= 10 -> [10, infinito)
    #i > 10 -> (10, infinito)
    # i == 10
    while i >= 10 or len(lista) == 3:#not False = True

        print(i)
        
        if i  % 2 == 0:
            print("par\n")
        else:
            print("impar\n")
        
        if i == 9:
            print("Lucky number!\n")
            break
        
        i += 1


    return

if __name__ == "__main__":

    ejemplo_if_elif()