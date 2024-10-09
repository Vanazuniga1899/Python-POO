#Defino la clase
class Empleado:
    #Método constructor
    def __init__(self,nombre,edad,puesto, salario,color,genero):
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.edad = edad 
        self.puesto= puesto
        self.salario = salario
        self.color = color
        self.genero = genero
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del empleado")
        print("Nombre: " + self.nombre)
        print("Edad: " + self.edad)
        print("Puesto: " + self.puesto)
        print("Color: " + self.color)
        print("Salario: " + self.salario)
        print("Genero: " + self.genero)

    
        print("--------------------------")

    #Método para el desempeño del empleado
    def desempeño_empleado (self):
        #Defino el atributo   desempeño del empleado
        self.desempeño_empleado  = input("El desempeño del empleado es bueno? sí o No: ")
        #Condicion para verificar si el empleado tiene un buen desempeño
        if self.desempeño_empleado:
            print(" El empleado "+ self.nombre +" tiene un buen desempeño ")
            print("-----------------------------------")
        else:
            print("El empleado " + self.nombre +" no tiene un buen desempeño ")


#Creamos los objetos a partir de instanciar la clase del Animal
objeto1 = Empleado("Luis","28 años","Ingeniero s.","2.000.000","Moreno","Masculino")
objeto2 = Empleado("Danna","26 años","Secretaria","1.245.950","Blanca","Femenina")
objeto3 = Empleado("Sebastían","40 años","Administrador","2.000.500","Blanco","Masculino")

#Mostrar los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.desempeño_empleado()#Método que evalua el desempeño del empleado
objeto2.mostrar_detalles()
objeto3.mostrar_detalles()
