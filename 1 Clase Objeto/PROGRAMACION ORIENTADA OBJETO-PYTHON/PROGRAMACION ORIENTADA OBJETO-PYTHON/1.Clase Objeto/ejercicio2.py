#Defino la clase
class Animal:
    #Método constructor
    def __init__(self,nombre,raza, habitad,color, edad,peso):
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.raza = raza
        self.habitad= habitad
        self.color = color
        self.edad = edad 
        self.peso = peso

    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del Animal")
        print("Nombre: " + self.nombre)
        print("Raza: " + self.raza)
        print("Habitad: " + self.habitad)
        print("Color: " + self.color)
        print("Edad: " + self.edad)
        print("Peso: " + self.peso)
       
        print("--------------------------")

    #Método para hacer ruido
    def hacer_ruido (self):
        #Defino el atributo  hacer ruido
        self.hacer_ruido  = input("El animal esta haciedo ruido? sí o No: ")
        #Condicion para verificar sie el animal esta haciendo ruido
        if self.hacer_ruido:
            print("El animal "+self.nombre+" esta haciendo ruido")
            print("-----------------------------------")
        else:
            print("El animal "+self.nombre+" no esta haciendo ruido")


#Creamos los objetos a partir de instanciar la clase del Animal
objeto1 = Animal("Luis","Pez","Oceano Atlantico","Amarillo","2 años","1,6kg")
objeto2 = Animal("Anderson","Cangrejo ermitaño","Mares y rios","Rojo","7 años","1,kg")
objeto3 = Animal("tiburoncín","Tiburon brilloso","Oceano Atlantico","Azul","3 años","2kg")

#Mostrar los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.hacer_ruido()#Método que evaluar el ruido del animal
objeto2.mostrar_detalles()
objeto3.mostrar_detalles()




         