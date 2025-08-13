class Cookie:
    def __init__(self,name,price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    def show_info(self):
        print(f"La galleta tiene un precio de: {self.price}, y tiene un peso de {self.weight}")
class ChipCookie(Cookie):
    def __init__(self, chips_amount):
        super().__init__(name, price, weight)
        self.chips_amount = chips_amount
        try:
            if chips_amount <= 0 :
                print("La cantidad de chispas debe ser un numero mayor a 0")
        except ValueError:
            print("Ingrese un valor valido")
        except TypeError:
            print("Ingrese un tipo de valor valido")
        except Exception as e:
            print("Un error inesperado ha ocurrido")
    def show_info(self):
        print(f"La galleta con el precio de: {self.price} quetzaltes y peso de {self.weight}\n"
              f" ahora tiene{self.chips_amount} chispas")

class Relleno:
    def __init__(self, sabor_relleno):
        self.sabor_relleno = sabor_relleno
    def describir_relleno(self):
        relleno = input("Describa que relleno lleva la galleta: ")

class FilledCookie(Cookie, Relleno):
    def __init__(self, filled_flavor):
        super().__init__(name, price, weight)
        self.filled_flavor = filled_flavor

def describir_relleno(self):
        print(f"La galleta el precio de: {self.price} quetzales, y  peso de {self.weight} y \n"
              f"{self.chips_amount} chispas, tiene un releno de {self.filled_flavor}")

class data_filled:
    def __init__(self):self.cookies = []
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

