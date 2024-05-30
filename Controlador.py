
from Modelo import *



class coordinador:
    def __init__(self):
        self.database= PacienteDato()

    def add_patient(self, data:dict):
        return self.database.añadir_paciente(data)

    def del_patient(self, id: str):
        self.database.eliminar_paciente(id)

    def search_patients(self, initName: str = ''):
        return self.database.buscar_paciente(initName)
    


    

