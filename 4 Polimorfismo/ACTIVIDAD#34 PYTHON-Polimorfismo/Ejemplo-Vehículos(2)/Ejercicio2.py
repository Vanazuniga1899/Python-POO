# Clase Carro
class Carro:
    def __init__(self, modelo, color, año,cinturon_seguridad):
        self.modelo = modelo
        self.color = color
        self.año = año
        self.Cinturon_seguridad = cinturon_seguridad

    def descripcion(self):
        print("----CARRO----")
        print(f"{self.modelo} ")
        print(f"Color: {self.color}")
        print(f"Año: {self.año}")
        print(f"Cinturon de seguridad: {self.Cinturon_seguridad}")
        print(f"....................................")


# Clase Moto
class moto:
    def __init__(self, modelo, color, año,m_electrica):
        self.modelo = modelo
        self.color = color
        self.año = año
        self.m_electica = m_electrica

    def descripcion(self):
        print("----MOTO----")
        print(f"{self.modelo} {self.color}")
        print(f"Año: {self.año}")
        print(f"Moto electrica: {self.m_electica}")
        print(f"....................................")


# Clase Bicicleta
class Bicicleta:
    def __init__(self, modelo, color, año,pedales):
        self.modelo = modelo
        self.color = color
        self.año = año
        self.pedales = pedales

    def descripcion(self):
        print("----BICICLETA----")
        print(f"{self.modelo} {self.color}")
        print(f"Año: {self.año}")
        print(f"Pedales: {self.pedales}")
        print(f"....................................")

# Función que muestra la información de cualquier tipo de objeto
def mostrar_informacion(Vehiculo):
    Vehiculo.descripcion()

# Instancias de cada clase
objeto_carro = Carro("Toyota", "Gris", 2018, "Precausion")
objeto_moto = moto("honda", "Roja", 2016, "Maxima velocidad")
objeto_bicicleta = Bicicleta("Bicicleta de ruta", "Negra", 2023, "Capacitables")

# Llamado al método descripcion para cada objeto
mostrar_informacion(objeto_carro)
objeto_carro.descripcion()
mostrar_informacion(objeto_moto)
objeto_moto.descripcion()
mostrar_informacion(objeto_bicicleta)
objeto_bicicleta.descripcion()