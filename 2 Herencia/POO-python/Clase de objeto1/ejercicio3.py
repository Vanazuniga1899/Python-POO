class Instrumento: 
    # Constructor
    def _init_(self, tipo_instrumento, marca, material_fabrica): 
        self.tipo_instrumento = tipo_instrumento 
        self.marca = marca 
        self.material_fabrica = material_fabrica
        self.precio = int(input("Precio del producto:")) 

        
        # Método público
    def registrar(self): 
        print("-----------------------") 
        print("ELEMENTO REGISTRADO") 
        print("-----------------------") 
        print("Tipo de instrumento: ", self.tipo_instrumento) 
        print("Marca: ", self.marca) 
        print("Material fabricado: ", self.material_fabrica) 
        print("No. de precio sugerido:", self.precio) 

class Guitarra(Instrumento): 
    # Constructor de la subclase
    def __init__(self, tipo_instrumento, marca, material_fabricado,numero_cuerdas):
        # Llamada al constructor de la superclase
        super()._init_(tipo_instrumento, marca, material_fabricado)  
        self.numero_cuerdas = numero_cuerdas  # atributo privado 
        self.acordes_basicos = int(input("Acordes basicos: "))

 # Método privado
    def Tocar_Guitara(self): 
        print("numero de cuerdas: ", self.numero_cuerdas)  # imprimiendo el numero_cuerdas 
        
        if self.acordes_basicos >10:  
            print("...........") 
            print(f"El instrumento {self.tipo_instrumento}, de marca {self.marca} y material de fabrica {self.material_fabrica}  toca la guitarra !!") 
        else: 
             print("-----------------") 
             print(f"El instrumento {self.tipo_instrumento}, de marca {self.marca} y  material de fabrica {self.material_fabrica}  no toca la guitarra !!")  

            
        
# Instanciando la subclase Guitarra
objecto_guitarra = Guitarra("Guitarra clasica", "Yamaha", "Madera", "8") 
objecto_guitarra.registrar()  # Registrando el refrigerador 
objecto_guitarra.Tocar_Guitara()  # Ajustando la temperatura del refrigerador             