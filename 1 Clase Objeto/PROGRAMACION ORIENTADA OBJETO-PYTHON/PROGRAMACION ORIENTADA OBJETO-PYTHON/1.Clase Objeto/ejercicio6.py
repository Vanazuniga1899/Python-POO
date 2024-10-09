class Figuras_Geometricas:
    # Método constructor
    def __init__(self, nombre, lados, color, area, perimetro):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.lados = lados
        self.color = color 
        self.area = area
        self.perimetro = perimetro
        
    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información de la figura:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de lados: {self.lados}")
        print(f"Color: {self.color}")
        print(f"Área: {self.area if self.area is not None else 'No disponible'}")
        print(f"Perímetro: {self.perimetro if self.perimetro is not None else 'No disponible'}")
        print("--------------------------------")
        
    # Método para calcular el perímetro de diferentes Figuras_Geometricas
    def calcular_perimetro(self):
        if self.nombre.lower() == "pentágono":
            lado = float(input("Digite la longitud de un lado del pentágono: "))
            if lado > 0:
                self.perimetro = 5 * lado
                print(f"El perímetro del pentágono es {self.perimetro} unidades.")
            else:
                print("El valor ingresado no es válido.")
        else:
            print(f"El cálculo del perímetro no está implementado para {self.nombre}.")
        print("--------------------------------")

# Creación de los objetos a partir de la clase Figuras_Geometricas
objeto1 = Figuras_Geometricas("Pentágono", 5, "Amarillo", "43.01cm²", "25cm")
objeto2 = Figuras_Geometricas("Círculo", 0, "Rojo", "78,54cm²", "31.42cm")
objeto3 = Figuras_Geometricas("Triángulo", 3, "Azul", "10cm²", "12cm")

# Mostrar detalles de los objetos
objeto1.mostrar_detalles()
objeto1.calcular_perimetro()# Calcular el perímetro del pentágono
objeto2.mostrar_detalles()
objeto3.mostrar_detalles()
