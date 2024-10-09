#Clase producto con atributos encapsulados o privados
class Productos:
    #Metodo constructor
    def __init__(self,nombre,precio,cantidad,categoria):
        self.__nombre=nombre #privado
        self.__precio=precio #privado
        self.cantidad=cantidad #publico
        self.categoria=categoria #publico
    
        
    #Metodo getter
    def obtener_nombre(self):
        return self.__nombre
    
    #Metodo getter
    def obtener_precio(self):
        return self.__precio
    

    
    #Metodo setter
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre=nuevo_nombre
        
    #Metodo setter
    def establecer_precio(self, nuevo_precio):
        self.__precio=nuevo_precio 
        
        
    #Metodo mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nNombre: {self.__nombre}")
        print(f"Precio: {self.__precio} pesos")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoria: {self.categoria}")

#objeto
producto=Productos("samsung",1999900,"12","galaxy")
    
    
#Imprimir atributos publicos y privados
producto.mostrar_detalles()
    
print("-------------------------")
    
#Imprimir el atributo encapsulado modificado su acceso con getter y setter
producto.establecer_nombre("Redmi") #setter
print(f"Nombre: { producto.obtener_nombre() }") #getter
producto.establecer_precio("1999.900") #setter
print(f"Precio: { producto.obtener_precio() }") #getter
print(f"Cantidad: { producto.cantidad }") #getter
print(f"Categoria: { producto.categoria }") #publico

 