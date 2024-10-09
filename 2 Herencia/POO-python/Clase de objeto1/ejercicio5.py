class Reloj:
    # Constructor
    def __init__(self, marca, material): 
        self.marca = marca 
        self.material = material 
        self.precio_deReloj = int(input("Precio del reloj: ")) 

    # Método público
    def registrar(self): 
        print("-----------------------") 
        print("ELEMENTO REGISTRADO") 
        print("-----------------------") 
        print(f"Marca: {self.marca}") 
        print(f"Material: {self.material}") 
        print(f"No. Precio del reloj: {self.precio_deReloj}") 

class Reloj_inteligente(Reloj): 
    # Constructor de la subclase
    def __init__(self, marca, material, tipo_dePantalla):
        # Llamada al constructor de la superclase
        super().__init__(marca, material)  
        self.tipo_dePantalla = tipo_dePantalla  # Atributo privado 
        self.sistema_operativo = input("Sistema operativo: ")

    # Método público
    def encender_reloj(self): 
        print(f"Tipo de Pantalla: {self.tipo_dePantalla}")  # Imprimiendo el tipo_dePantalla
        
        # Verifica si el sistema operativo es mayor que 10
        try:
            if int(self.sistema_operativo) > 10:  
                print("...........") 
                print(f"El reloj {self.marca}, con material {self.material}, enciende !!") 
            else: 
                print("-----------------") 
                print(f"El reloj {self.marca}, con material {self.material}, no enciende !!") 
        except ValueError:
            print("El sistema operativo debe ser un número.")

# Instanciando la subclase Reloj_inteligente
objeto_reloj = Reloj_inteligente("Apple", "Aluminio", "OLED") 
objeto_reloj.registrar()  # Registrando  
objeto_reloj.encender_reloj()  # Encender el reloj
