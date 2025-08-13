class Cookie:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight
    def show_info(self):
        print(f"La galleta tiene un precio de: {self.price}, y tiene un peso de {self.weight}")
cookies = []
class ChipCookie(Cookie):
    def __init__(self, cantidad_chispas):
        self.cantidad_chispas = cantidad_chispas
    def show_info(self):
        print(f"La galleta con el precio de: {self.price} quetzaltes y peso de {self.weight}\n"
              f" ahora tiene{self.cantidad_chispas} chispas")

class RellenoCookie(Cookie, ChipCookie):
    def __init__(self, sabor_relleno):
        self.sabor_relleno = sabor_relleno
    def describir_relleno(self):
        print(f"La galleta el precio de: {self.price} quetzales, y  peso de {self.weight} y \n"
              f"{self.cantidad_chispas} chispas, tiene un releno de {self.sabor_relleno}")

def hi():
    print("-"*10 + "BIENVENIDO AL REGISTRO DE GALLETAS" + "-"*10)

def options():
    try:
        print("1.Registrar galleta básica. \n"
              "2. Registrar galleta con chispas \n"
              "3. Registrar galleta rellena\n"
              "4. Lista de galletas\n"
              "5. Buscar galleta por nombre\n"
              "6. Eliminar galleta por nombre\n"
              "7. Salir del programa")
        option = int(input("Ingrese la opcion que desea:"))
        match option:
            case "1":
                print()

    except ValueError:
        print("Ingrese un dato valido")
    except TypeError:
        print("Ingrese un numero")
    except Exception as e:
        print("Un error inesperado ha ocurrido", e)

