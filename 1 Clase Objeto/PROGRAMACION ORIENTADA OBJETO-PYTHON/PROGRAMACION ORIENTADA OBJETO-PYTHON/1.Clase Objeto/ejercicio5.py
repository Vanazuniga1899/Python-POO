#Defino la clase
class moto:
    #Método constructor
    def __init__(self,marca,color, año,peso):
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.color = color
        self.año= año
        self.peso = peso

    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion de la moto")
        print("Marca: " + self.marca)
        print("Color: " + self.color)
        print("Año: " + self.año)
        print("Peso: " + self.peso)
        print("--------------------------")

    #Método para encender la moto
    def encender_moto (self):
        #Defino el atributo  hacer ruido
        self.encender_moto   = input("la moto ensendera? sí o No: ")
        #Condicion para verificar si  la moto encendera
        if self.encender_moto:
            print("La moto "+self.marca+" esta haciendo ruido, ¡eso quiere decir que enciende exitosamente!")
            print("-----------------------------------")
        else:
            print("La moto "+self.marca+" no esta haciendo ruido, ¡eso quiere decir que no enciende!")


#Creamos los objetos a partir de instanciar la clase del moto
objeto1 = moto("Suzuki","Negra","2018","155kg")
objeto2 = moto("Kymco","Verde","2007","115kg")
objeto3 = moto("Hero","Negra","2016","160kg")
#Mostrar los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.encender_moto ()#Método que evaluar el encendedor de la moto
objeto2.mostrar_detalles()
objeto3.mostrar_detalles()