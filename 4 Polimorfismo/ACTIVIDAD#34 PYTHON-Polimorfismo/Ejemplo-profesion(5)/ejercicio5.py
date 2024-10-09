# Clase Médico
class Medico:
    def __init__(self, nombres, apellidos, cedula, especialidad):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.especialidad = especialidad

    def trabajar(self):
        print("Hola, soy un Médico")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Especialidad: {self.especialidad}")
        print("Mi trabajo consiste en diagnosticar y tratar a los pacientes.")
        print("....................................")

# Clase Ingeniero
class Ingeniero:
    def __init__(self, nombres, apellidos, cedula, campo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.campo = campo

    def trabajar(self):
        print("Hola, soy un Ingeniero")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Campo de trabajo: {self.campo}")
        print("Mi trabajo consiste en diseñar, desarrollar y gestionar proyectos técnicos.")
        print("....................................")

# Clase Docente
class Docente:
    def __init__(self, nombres, apellidos, cedula, asignatura):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.asignatura = asignatura

    def trabajar(self):
        print("Hola, soy un Docente")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Asignatura: {self.asignatura}")
        print("Mi trabajo consiste en enseñar y guiar a los estudiantes.")
        print("....................................")

# Función que muestra la información de cualquier tipo de profesional
def mostrar_trabajo(profesional):
    profesional.trabajar()

# Instancias de cada clase
medico = Medico("Andrés", "Pérez", 11223344, "Cardiología")
ingeniero = Ingeniero("Lucía", "Gómez", 22334455, "Ingeniería Civil")
docente = Docente("Juan", "Ramírez", 33445566, "Matemáticas")

# Llamado al método trabajar() para cada objeto
mostrar_trabajo(medico)
mostrar_trabajo(ingeniero)
mostrar_trabajo(docente)
