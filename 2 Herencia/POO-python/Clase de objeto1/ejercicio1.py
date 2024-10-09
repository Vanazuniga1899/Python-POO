class Electrodomestico: 
    # Constructor
    def _init_(self, marca, color, capacidad): 
        self.marca = marca 
        self.color = color 
        self.capacidad = capacidad
        self.consumo_electrico = int(input("Consumo electrico:")) 
        
    # Método público
    def registrar(self): 
        print("-----------------------") 
        print("ELEMENTO REGISTRADO") 
        print("-----------------------") 
        print("Marca: ", self.marca) 
        print("Color: ", self.color) 
        print("Capacidad: ", self.capacidad) 
        print("No. de consumo electrico:", self.consumo_electrico) 
            
class Refrigerador(Electrodomestico): 
    # Constructor de la subclase
    def __init__(self, marca, color, capacidad, tipo_regrigerador):
        # Llamada al constructor de la superclase
        super()._init_(marca, color, capacidad)  
        self.tipo_regrigerador = tipo_regrigerador  # atributo privado 
        self.temperatura = int(input("Temperatura inicial en grados centígrados: "))
        
    # Método privado
    def ajustar_temperatura(self): 
        print("tipo_regrigerador: ", self.tipo_regrigerador)  # imprimiendo el tipo_regrigerador 
        
        if self.temperatura > 7:  
            print("...........") 
            print(f"El refrigerador {self.marca}, con color {self.color} y capacidad {self.capacidad} tiene una temperatura normal") 
        else: 
             print("-----------------") 
             print(f"El refrigerador {self.marca}, con color {self.color} y capacidad {self.capacidad} tiene una temperatura anormal!")  
             
# Instanciando la subclase Refrigerador
objecto_refrigerador = Refrigerador("Redmi 12pro", "Negro", "230 litros", "ElP") 
objecto_refrigerador.registrar()  # Registrando el refrigerador 
objecto_refrigerador.ajustar_temperatura()  # Ajustando la temperatura del refrigerador