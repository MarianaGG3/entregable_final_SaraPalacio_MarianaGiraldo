
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

    
        