
from Modelo import *
import sys
from PyQt5.QtWidgets import QApplication
from Vista import *


class coordinador:
    def __init__(self):
        self.database= PacienteDato()

    def add_patient(self, data:dict):
        return self.database.anadir_paciente(data)

    def del_patient(self, id: str):
        self.database.eliminar_paciente(id)

    def search_patients(self, initName: str = ''):
        return self.database.buscar_paciente(initName)


def main():
    app = QApplication(sys.argv)
    vista_=VentanaIngreso()
    vista_.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

        
    


    

