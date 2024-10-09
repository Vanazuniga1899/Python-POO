#Defino la clase
class Carro:
    #Método constructor
    def __init__(self,marca,color, año,peso):
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.color = color
        self.año= año
        self.peso = peso

    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del Carro")
        print("Marca: " + self.marca)
        print("Color: " + self.color)
        print("Año: " + self.año)
        print("Peso: " + self.peso)
       
        print("--------------------------")

    #Método para encender el carro
    def encender_carro (self):
        #Defino el atributo  hacer ruido
        self.encender_carro   = input("El Carro ensendera? sí o No: ")
        #Condicion para verificar si  el Carro encendera
        if self.encender_carro:
            print("El Carro "+self.marca+" esta haciendo ruido, ¡eso quiere decir que enciende exitosamente!")
            print("-----------------------------------")
        else:
            print("El Carro "+self.marca+" no esta haciendo ruido, ¡eso quiere decir que no enciende!")


#Creamos los objetos a partir de instanciar la clase del Carro
objeto1 = Carro("Toyota","Roja","Fj40-1977","1,600kg")
objeto2 = Carro("Lamborghini huracán","Verde","2014","1,422kg")
objeto3 = Carro("sprint cherrolet","Azul","1989","685kg")
#Mostrar los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.encender_carro ()#Método que evaluar el encendedor del Carro
objeto2.mostrar_detalles()
objeto3.mostrar_detalles()




         