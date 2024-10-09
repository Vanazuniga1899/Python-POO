""" Crea una clase abstracta TareaEmpleado con un método abstracto realizar_tarea(). 
Implementa las clases Ingeniero y Doctor que heredan de TareaEmpleado e implementan el 
método realizar_tarea() de manera específica según su especialidad."""

from abc import ABC, abstractmethod

# Clase abstracta
class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

# Clase Ingeniero que hereda de TareaEmpleado
class Ingeniero(TareaEmpleado):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def realizar_tarea(self):
          return f"{self.nombre} la ingeniera, está programando en estos momentos."

# Clase Doctor que hereda de TareaEmpleado
class Doctor(TareaEmpleado):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def realizar_tarea(self):
        return f"{self.nombre} el doctor, está atendiendo a un paciente en estos momentos."

# Uso de las clases
ingeniero = Ingeniero("Diana")
doctor = Doctor("Mateo")

print(f"Tarea del ingeniero: {ingeniero.realizar_tarea()}")
print(f"Tarea del doctor: {doctor.realizar_tarea()}")
