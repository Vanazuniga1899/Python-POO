#Defino la clase
class Celular:
    #Método constructor
    def __init__(self,nombre, marca,imei, bateria, camara):
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.marca = marca
        self.imei= imei
        self.bateria = bateria
        self.camara = camara 
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del Celular")
        print("Nombre: " + self.nombre)
        print("Marca: " + self.marca)
        print("IMEI: " + self.imei)
        print("Bateria: " + self.bateria)
        print("Camara: " + self.camara)
        print("--------------------------")
        
    #Método para Encender el Celular
    def encender (self):
        #Defino el atributo privado energia solo para el metodo encender
        self.energia  = int(input("Digite el valor de la carga: "))
        #Evaluamos si tiene carga el celular
        if self.energia >0:
            print("El celular "+self.nombre+" se puede encender")
            print(f"||||||||||| {self.energia} % de carga")
            print("-----------------------------------")
        else:
            print("El objeto "+self.nombre+" no se puede encender")
        

        
#Creamos los objetos a partir de instanciar la clase Celular     
objeto1 = Celular("Samsung","Galaxy s24","12861122","4000mAh","108mpx")
objeto2 = Celular("Xiaomi","Mi 12","12361122","5600mAh","108mpx")
objeto3 = Celular("iphone 13","Apple","2561122","5600mAh","108mpx")

#Mostrar los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.encender() #Método que evaluar el enceendido del celular
objeto2.mostrar_detalles()
objeto3.mostrar_detalles()

