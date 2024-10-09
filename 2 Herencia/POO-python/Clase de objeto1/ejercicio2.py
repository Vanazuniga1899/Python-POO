class Dispositivo: 
    # Constructor
    def _init_(self, marca, modelo, año): 
        self.marca = marca 
        self.modelo = modelo 
        self.año = año
        self.capaciad_bateria = int(input("Capacidad de la bateria:")) 

        # Método público
    def registrar(self): 
        print("-----------------------") 
        print("ELEMENTO REGISTRADO") 
        print("-----------------------") 
        print("Marca: ", self.marca) 
        print("Modelo: ", self.modelo) 
        print("Año: ", self.año) 
        print("No. de capacidad de la bateria:", self.capaciad_bateria) 

class Smartphone(Dispositivo): 
    # Constructor de la subclase
    def __init__(self, marca, modelo, año,sistema_operativo):
        # Llamada al constructor de la superclase
        super()._init_(marca, modelo, año)  
        self.sistema_operativo = sistema_operativo  # atributo privado 
        self.tipo_conectividad = int(input("Tipo de conectividad: "))

 # Método privado
    def encender_Smartphone(self): 
        print("sistema_operativo: ", self.sistema_operativo)  # imprimiendo el sistema_operativo 
        
        if self.tipo_conectividad > 10:  
            print("...........") 
            print(f"El dispositivo {self.marca}, con modelo {self.modelo} y año {self.año}  enciende !!") 
        else: 
             print("-----------------") 
             print(f"El dispositivo {self.marca}, con modelo {self.modelo} y año {self.año}  no enciende !!")  

# Instanciando la subclase Smartphone
objecto_smartphone = Smartphone("Samsung", "Galaxy S21", "2021", "Androd 11 de fabrica") 
objecto_smartphone.registrar()  # Registrando el refrigerador 
objecto_smartphone.encender_Smartphone()  # Ajustando la temperatura del refrigerador             