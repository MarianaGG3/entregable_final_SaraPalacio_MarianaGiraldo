from Vista import *
from Modelo import *
import sys

data_base='datos.json'

class coordinador:
    def __init__(self):
        self.database= PacienteDato(data_base)

    def add_patient(self, name, last_name, age, id):
        patient = patient(name, last_name, age, id)
        return self.database.añadir_paciente(patient)

    def remove_patient(self, id):
        self.database.eliminar_paciente(id)

    def search_patients(self, search):
        return self.database.buscar_paciente(search)

    

def main():
    app = QApplication(sys.argv)
    vista_=VentanaIngreso()
    vista_.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()