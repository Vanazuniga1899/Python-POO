"""Crea una clase abstracta Empleado con un método abstracto calcular_salario().
Luego, crea dos clases concretas EmpleadoTiempoCompleto y EmpleadoPorHoras
que implementen calcular_salario() de manera distinta."""

from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual

        
    def calcular_salario(self):
        return self.salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, salario_horas, horas_trabajadas):
        self.salario_horas = salario_horas
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.salario_horas * self.horas_trabajadas

# Uso de las clases
empleado_completo = EmpleadoTiempoCompleto(3000)
print(f"Juan carlos, recibe un salario de empleado a tiempo completo de: {empleado_completo.calcular_salario()}")

empleado_por_horas = EmpleadoPorHoras(20, 100)
print(f"A diferencia de Luis, que recibe un salario de empleado por horas de: {empleado_por_horas.calcular_salario()}")