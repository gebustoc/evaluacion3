import os


mascotas = []

def intInp(mstr):
    v = 0
    try:
        v = int(input(mstr))
    except Exception as e:
        v = -1    
    return v

def getConfirmedValue(message,isint=False ):
    while True:
        v = None
        if isint:
            v = intInp(message)
        else:
            v = input(message)

        # invalid :( boowomp.wav
        if v == -1 or v == None:
            print("valor invalido ")
            continue
        else:
            conf = input("estas seguro?, s/n ")
            if conf.lower() == "s": return v
            



def addPET():
    species = ""
    name = ""
    weight = 0
    initialcost = 0
    total = 0
    tax = 0
    struct = []

    while True:
        species = getConfirmedValue("que especie es? ")
        name = getConfirmedValue("cual es su nombre? ")
        weight = getConfirmedValue("cuanto kgs pesa? ",True)
        initialcost = getConfirmedValue("cuanto es la consulta inicial? ",True)
        tax = round(initialcost * .05)
        total = round(initialcost+tax)
        struct = [species,name,weight,initialcost,tax,total]
        print_datastruct(struct)

        if input("esta correcta la informacion? s/n ").lower() == "s":
            break
    
    mascotas.append(struct)

def print_datastruct(data,printtocon=True):
    m = f"especie:{data[0]}, nombre:{data[1]}, peso:{data[2]}kg, consulta inicial:${data[3]},impuesto:${data[4]}, total:${data[5]}"
    if printtocon:print(m)
    return m

def print_all():
    for PETprogre in mascotas:print_datastruct(PETprogre)
    input("presiona enter para salir")

def save_text():
    while True:
        path = input("como se va a llamar el archivo? ")+".txt"

        if (os.path.exists(path) and os.path.isfile(path)):
            if input("el archivo ya existe, sobreescribir? s/n ").lower()!="s":
                continue
        filter = None

        if input("quiere poner un filtro? s/n ").lower() == "s":
            filter = input("elija una especie exclusiva para guardar: ")


        with open(path,"a") as f:
            # clear file
            f.truncate(0)
            for advancedPET in mascotas:
                if advancedPET[0] == filter or filter == None:
                    f.write(f"{print_datastruct(advancedPET,False)},\n")


        input("listo, presiona enter para salir")
        break

def main():
    while True:
        os.system("cls")
        print(
        """1):Registrar Mascota
2):Listar Mascotas
3):Imprimir ficha
4):Salir

        """
        )
        v = intInp("elije una opcion ")
        match v:
            case -1:print("opcion invalida");input("presione enter para continuar")
            case 1:
                addPET()
            case 2:
                print_all()
            case 3:
                save_text()
            case 4:
                input("presiona enter para salir ")



if __name__ == "__main__":main()