class Cookie:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight
    def show_info(self):
        print(f"La galleta tiene un precio de: {self.price}, y tiene un peso de {self.weight}")

class ChipCookie(Cookie):
    def __init__(self, cantidad_chispas):
        self.cantidad_chispas = cantidad_chispas
    def show_info(self):
        print(f"La galleta ahora tiene{self.cantidad_chispas} chispas")

class RellenoCookie(Cookie, ChipCookie):
    def __init__(self, sabor_relleno):
        self.sabor_relleno = sabor_relleno
    def describir_relleno(self):
        print(f"La galleta el precio de: {self.price} quetzales, y  peso de {self.weight} y \n"
              f"{self.cantidad_chispas} chispas, tiene un releno de {self.sabor_relleno}")