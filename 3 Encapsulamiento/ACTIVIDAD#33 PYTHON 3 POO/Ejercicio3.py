#Clase libros con atributos encapsulados o privados
class Libros:
    #Metodo constructor
    def __init__(self,titulo,autor,isbn,editorial ):
        self.__titulo=titulo #privado
        self.__autor=autor #privado
        self.__isbn=isbn #privado
        self.editorial  = editorial  #publico
        
    #Metodo getter
    def obtener_titulo(self):
        return self.__titulo
    
    #Metodo getter
    def obtener_autor(self):
        return self.__autor
    
    #Metodo getter
    def obtener_isbn(self):
        return self.__isbn
    

    
    #Metodo setter
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo=nuevo_titulo
        
    #Metodo setter
    def establecer_autor(self, nuevo_autor):
        self.__autor=nuevo_autor  
       
     #Metodo setter
    def establecer_isbn(self, nuevo_isbn):
        self.__isbn=nuevo_isbn  
        
        
        
    #Metodo mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"Titulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Isbn: {self.__isbn}")
        print(f"Editorial: {self.editorial}")
#objeto
libro=Libros("El principito","Antoine de Saint",4,"Gran Travesía")
    
    
#Imprimir atributos publicos y privados
libro.mostrar_detalles()
    
print("-------------------------")
    
#Imprimir el atributo encapsulado modificado su acceso con getter y setter
libro.establecer_titulo("El viejo y el mar") #setter
print(f"Nombres: { libro.obtener_titulo() }") #getter
libro.establecer_autor("Hemingway, Ernest") #setter
print(f"Autor: { libro.obtener_autor() }") #getter
libro.establecer_isbn("3") #setter
print(f"Isbn: { libro.obtener_isbn() }") #getter
print(f"Editorial: { libro.editorial }") #publico
 


 
