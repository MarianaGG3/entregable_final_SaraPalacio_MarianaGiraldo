import json
dicc_pacientes={}
class Paciente:
    datos_paciente=[]
    def __init__(self):
        self.__nombre=""
        self.__apellido=""
        self.__edad=int
        self.__id=int

    def verNombre(self):
        return self.__nombre
    def verApellido(self):
        return self.__apellido
    def verEdad(self):
        return self.__edad
    def verId(self):
        return self.__id
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarApellido(self,a):
        self.__apellido = a
    def asignarEdad(self,e):
        self.__edad = e
    def asignarId(self,c):
        self.__id = c

    def AgregarPaciente(self,c,n,a,e):
        c=verCedula
        n=verNombre
        a=verApellido
        e=verEdad
        dicc_pacientes[c] =[n,a,e]

class PacienteDato:
    def __init__(self,ruta):
        self.ruta= ruta
        self.load_data()

    def load_data(self):
        try:
            with open(self.ruta, 'r') as file:
                self.paciente= json.load(file)
        except FileNotFoundError:
            self.paciente=[]

    def salvar_datos(self):
        with open(self.ruta, 'w') as file:
            json.dump([paciente.__dict__ for paciente in self.paciente], file)

    def añadir_paciente(self,paciente):
        if any(p['id']== paciente.id for p in self.paciente):
            return False 
        self.paciente.append(paciente.__dict__)
        self.salvar_datos()
        return True
    
    def eliminar_paciente(self,id):
        self.paciente=[p for p in self.paciente if p['id']!= id]
        self.salvar_datos()
        
    def buscar_paciente(self, buscar):
        return [Paciente(**p) for p in self.paciente if p['nombre'].lower().startswith(buscar.lower())]