class Cookie:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    def show_info(self):
        print(f"La galleta {self.name} tiene un precio de: {self.price}, y tiene un peso de {self.weight}")

class Relleno:
    def __init__(self, sabor_relleno):
        self.sabor_relleno = sabor_relleno
    def describir_relleno(self):
        print(f"El relleno que lleva la galleta es: {self.sabor_relleno}")

class ChipCookie(Cookie):
    def __init__(self, name, price, weight, chips_amount):
        super().__init__(name, price, weight)
        self.chips_amount = chips_amount

class FilledCookie(Cookie, Relleno):
    def __init__(self, name, price, weight, filled_flavor):
        super().__init__(name, price, weight)
        self.filled_flavor = filled_flavor
    def show_info(self):
        print(f"La galleta {self.name} tiene un precio de: {self.price} quetzales, y tiene un peso de {self.weight} lb")
        print(f"la galleta tiene un relleno de: {self.filled_flavor}")

class data_filled:
    def __init__(self):self.cookies = []
    def addedCookie(self):
        while True:
            name2 = input("Ingrese el nombre de la galleta: ")
            if name2 == " ": break
                print("Nombre vacio, debe agregar una galleta primero.")
        while True:
            price2 = int(input("Ingrese el precio de la galleta: "))
            if price2 <0: break
            print("El precio debe ser mayor a 0")
        while True:
            peso2 = int(input("Ingrese el peso de la galleta"))
            if peso2 <0: break
            print("El precio de la galleta debe ser mayor a 0 ")

    def add_cookie(self):
        try:
            name, price, weight = self.
            _new = Cookie(name, price, weight)
            cookies.append(_new)
            print(f"Galleta {name} ha sido agregada correctamente!")
            if not name:
                print("El nombre esta vacio")
            elif price < 0:
                print("El precio debe ser mayor a 0")
            elif weight < 0:
                print("El peso debe ser mayor a 0")

        except Exception as e:
            print("Un error inesperado ha ocurrido!\n"
                  "Error: ", e)

def hi():
    print("-"*10 + "BIENVENIDO AL REGISTRO DE GALLETAS" + "-"*10)

cookies = []
while True:
    try:
        hi()
        print("1.Registrar galleta básica. \n"
              "2. Registrar galleta con chispas \n"
              "3. Registrar galleta rellena\n"
              "4. Lista de galletas\n"
              "5. Buscar galleta por nombre\n"
              "6. Eliminar galleta por nombre\n"
              "7. Salir del programa")
        option = int(input("Ingrese la opcion que desea:"))
        match option:
            case 1:
                try:
                    name = input("Ingrese el nombre de la galleta: ")
                    price = int(input("Ingrese el precio de la galleta(en quetzales): "))
                    weight = int(input("Ingrese el peso de la galleta(en libras): "))
                    new = Cookie(name, price, weight)
                    cookies.append(new)
                    print(f"Galleta {name} ha sido agregada correctamente!")
                    if not name:
                        print("El nombre esta vacio")
                    elif price < 0:
                        print("El precio debe ser mayor a 0")
                    elif weight < 0:
                        print("El peso debe ser mayor a 0")
                except ValueError:
                    print("Ingrese un valor valido")
                except TypeError:
                    print("Ingrese un tipo de valor valido")
                except Exception as e:
                    print("Un error inesperado ha ocurrido")
            case 2:
                print("-"*10 + "INGRESAR GALLETA CON CHISPAS" + "-"*10)
                cantidad_chispas = int(input("Ingrese cantidad de chispas: "))
                if not cookies:
                    print("Ninguna galleta ha sido registrada, ingrese una primero.")
                else:
                    for x in cookies:
                        print(f"Se ha agregadov{cantidad_chispas} chipas a la galleta {name}")
            case 3:
                print("-"*10 + "REGISTRAR GALLETA RELLENA" + "-"*10)
                print("1. Chocolate\n"
                      "2. Crema\n"
                      "3. Caramelo")
                rellena = input("Ingrese el relleno que desea: ")
                match rellena:
                    case 1:
                        print(f"La galleta {name} ha sido rellena con chocolate")
                    case 2:
                        print(f"La galleta {name} ha sido rellena cin crema")
                    case 3:
                        print(f"La galleta {name} ha sido rellena con caramelo")
            case 4:
                print("-"*10 + "LISTA DE GALLETAS" + "-"*10)
                for x, galletas in enumerate():

                break
    except ValueError:
        print("Ingrese un valor valido")
    except TypeError:
        print("Ingrese un tipo de valor valido")

