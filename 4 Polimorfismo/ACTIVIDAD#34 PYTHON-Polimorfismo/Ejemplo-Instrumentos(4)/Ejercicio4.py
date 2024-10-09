# Clase Guitarra
class Guitarra:
    def __init__(self, marca, color,material):
        self.marca = marca
        self.color = color
        self.material = material
       
    def mostrar_info(self):
        print("----GUITARRA----")
        print(f"{self.marca} {self.color}")
        print(f"Material: {self.material}")

    def tocar(self):
        print("tocar guitarra")
        print(f"....................................")


# Clase Piano
class Piano:
    def __init__(self, marca, color,material):
        self.marca = marca
        self.color = color
        self.material = material
        

    def mostrar_info(self):
        print(" ----PIANO----")
        print(f"{self.marca} {self.color}")
        print(f"Material: {self.material}")

    def tocar(self):
        print("tocar piano")
        print(f"....................................")

# Clase Trompeta
class Trompeta:
    def __init__(self, marca, color,material):
        self.marca = marca
        self.color = color
        self.material = material 
        

    def mostrar_info(self):
        print("----TROMPETA----")
        print(f"{self.marca} {self.color}")
        print(f"Material: {self.material}")

    def tocar(self):
        print("tocar trompeta")
        print(f"....................................")

# Instancias de cada clase
objeto_guitarra = Guitarra("Fender", "amarillo", "abeto")
objeto_piano = Piano("Steinway & Sons ", "Negro", "Madera")
objeto_trompeta = Trompeta("Yamaha", "Dorado", "Laton")

# Llamado al método mostrar_info para cada objeto
objeto_guitarra.mostrar_info()
objeto_guitarra.tocar()
objeto_piano.mostrar_info()
objeto_piano.tocar()
objeto_trompeta.mostrar_info()
objeto_trompeta.tocar()