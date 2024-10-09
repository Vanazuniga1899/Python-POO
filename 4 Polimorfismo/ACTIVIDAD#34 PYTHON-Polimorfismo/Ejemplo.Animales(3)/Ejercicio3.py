# Clase Perro
class Perro:
    def __init__(self, especie, sexo, fecha_nacimiento,color):
        self.especie = especie
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.color = color

    def mostrar_info(self):
        print("----PERRO----")
        print(f"{self.especie} ")
        print(f"Color: {self.color}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Sexo del animal: {self.sexo}")


    def sonido(self):
        print("El perro hace ¡Guauu Guauu!")
        print(f"....................................")

    


# Clase Moto
class Gato:
    def __init__(self, especie, sexo, fecha_nacimiento,color):
        self.especie = especie
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.color = color


    def mostrar_info(self):
        print("----GATO----")
        print(f"{self.especie} {self.sexo}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Color: {self.color}")
    def sonido(self):
        print("El Gato hace ¡Miauu Miauu!")
        print(f"....................................")


# Clase Pajaro
class Pajaro:
    def __init__(self, especie, sexo, fecha_nacimiento,color,):
        self.especie = especie
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.color = color

    def mostrar_info(self):
        print("----PAJARO----")
        print(f"{self.especie} {self.sexo}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Color: {self.color}")

    def sonido(self):
        print("El pajaro hace ¡Pioo Pioo! ")
        
        print(f"....................................")

    


# Función que muestra la información de cualquier tipo de objeto


# Instancias de cada clase
objeto_perro = Perro("Dalmata", "M", 6, "Gris",)
objeto_gato = Gato("Egipcio", "H", 2, "piel",)
objeto_pajaro = Pajaro("Picaflor", "M", 3, "arcoiris")

# Llamado al método mostrar_info para cada objeto
objeto_perro.mostrar_info()
objeto_perro.sonido()
objeto_gato.mostrar_info()
objeto_gato.sonido()
objeto_pajaro.mostrar_info()
objeto_pajaro.sonido()

