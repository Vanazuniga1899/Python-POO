class Electronico: 
    # Constructor
    def _init_(self, marca, modelo, tipo_procesdor): 
        self.marca = marca 
        self.modelo = modelo 
        self.tipo_procesador = tipo_procesdor
        self.memoria_RAM = int(input("Memoria RAM:"))

    # Método público
    def registrar(self): 
        print("-----------------------") 
        print("ELEMENTO REGISTRADO") 
        print("-----------------------") 
        print("Marca: ", self.marca) 
        print("Modelo: ", self.modelo) 
        print("Tipo de procesador: ", self.tipo_procesador) 
        print("No. de memoria RAM:", self.memoria_RAM)

class Laptop(Electronico): 
    # Constructor de la subclase
    def __init__(self, marca, modelo, tipo_procesador, tipo_discoDuro):
        # Llamada al constructor de la superclase
        super()._init_(marca, modelo, tipo_procesador)  
        self.tipo_discoDuro = tipo_discoDuro  # atributo privado 
        self.duracio_deBateria = int(input("Duracion de la bateria del dispositivo: "))  

# Método privado
    def encender_laptop(self): 
        print("tipo_discoDuro: ", self.tipo_discoDuro)  # imprimiendo el tipo_discoDuro 
        
        if self.duracio_deBateria > 100:  
            print("...........") 
            print(f"La laptop {self.marca}, de modelo {self.modelo} y tipo de procesador {self.tipo_procesador} enciende de manera normal!") 
        else: 
             print("-----------------") 
             print(f"El refrigerador {self.marca},  de modelo {self.modelo} y  tipo de procesador {self.tipo_procesador} no enciende!") 


          
# Instanciando la subclase Laptop
objecto_laptop = Laptop("Lenovo ", "Rosa", "MD Ryzen 5 3500U", "8 GB") 
objecto_laptop.registrar()  # Registrando 
objecto_laptop.encender_laptop()  # Encender laptop 