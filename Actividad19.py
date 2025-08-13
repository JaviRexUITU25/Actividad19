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
    def __init__(self):
        self.cookies = []

    def addedCookie(self):
        while True:
            name2 = input("Ingrese el nombre de la galleta: ")
            if name2 == " ": break
            print("Nombre vacio, debe agregar una galleta primero.")
        while True:
            price2 = int(input("Ingrese el precio de la galleta: "))
            if price2 <=0: break
            print("El precio debe ser mayor a 0")
        while True:
            peso2 = int(input("Ingrese el peso de la galleta"))
            if peso2 <=0: break
            print("El precio de la galleta debe ser mayor a 0 ")
            return name2, price2,peso2

    def add_cookie(self):
        try:
            print("-"*10 + "AÑADIR GALLETA" + "-"*10)
            name, price, weight = self.addedCookie()
            self.cookies.append(Cookie(name, price, weight))
        except ValueError:
            print("Ingrese un valor valido")
        except TypeError:
            print("Ingrese un tipo de valor valido")
        except Exception as e:
            print("Un error inesperado ha ocurrido, intenta de nuevo\n"
                  "Error: ",e)
    def add_chips_cookie(self):
        print("-"*10 + "AGREGAR CHISPAS A LA GALLETA"+ "-"*10)
        name, price, weight = self.addedCookie()
        try:
            while True:
                chips = int(input("Ingresa la cantidad de chispas a agregar: "))
                if chips <=0:
                    print("La cantidad de chispas debe ser mayor a 0")
                else:
                    break
                self.cookies.append(ChipCookie(name, price, weight, chips))
                print(f"Se han agregado {chips} chispas a la galleta {name}")
        except Exception as e:
            print("Un error inesperado ha ocurrido!\n"
                  "Error: ", e)
    def filled_cookie(self):
        print("-"*10 + "AGREGAR RELLENO A LA GALLETA" + "-"*10)
        name, price, weight = self.addedCookie()
        while True:
            filled = input("Ingrese que relleno desea agregar a la galleta: ")
            if filled != " ": break
            else:
                print("Relleno vacio, ingresalo de nuevo.")
        self.cookies.append(Relleno(name))

    def cookie_list(self):
        if self.cookies:
            print("-"*10+ "LISTA DE GALLETAS"+ "-"*10)
            for num, x in enumerate(self.cookies, 1):
                print(f"{num} ", end="")
                x.show_info()
        else:
            print("Ninguna galleta ha sido agregada, agrega una primero.")

    def find_cookie(self):
        if self.cookies:
            print("-"*10 + "ENCONTRAR GALLETA POR NOMBRE"+ "-"*10)
            found = input("Ingrese el nombre de la galleta que busca: ").lower()
            for i in self.cookies:
                if i.found.lower() == found:
                    i.show_info()
                    print(f"La galleta encontrada es: {i}")
                    break
                else:
                    print("No se ha encontrado esa galleta, intente de nuevo.")

    def deleted_cookie(self):
        if self.cookies:
            print("-"*10 + "ELIMINAR GALLETA POR NOMBRE"+ "-"*10)
            deleted = input("Ingrese el nombre de la galleta que desea eliminar:  ").lower()
            for y in self.cookies:
                if y.deleted.lower() == deleted:
                    y.show_info()
                    print("Galleta eliminada")
                    break
                else:
                    print("Galleta no encontrada, intente de nuevo. ")



def hi():
    print("-"*20 + "BIENVENIDO AL REGISTRO DE GALLETAS" + "-"*20)
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
                data_filled.add_cookie()
            case 2:
                data_filled.add_chips_cookie()
            case 3:
                data_filled.filled_cookie()
            case 4:
                data_filled.cookie_list()
            case 5:
                data_filled.find_cookie()
            case 6:
                data_filled.deleted_cookie()
            case 7:
                print("Saliendo...")
            case _:
                print("Ingrese una opcion valida.")
                break
    except ValueError:
        print("Ingrese un valor valido")
    except TypeError:
        print("Ingrese un tipo de valor valido")
    except Exception as e:
        print("Un error inesperado ha ocurrido\n"
              "error: ", e)