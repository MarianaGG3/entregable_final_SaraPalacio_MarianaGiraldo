from Vista import *
from Modelo import *
import sys

data_base='datos.json'

class coordinador:
    def __init__(self):
        self.database= PacienteDato(data_base)
    

def main():
    app = QApplication(sys.argv)
    vista_=VentanaIngreso()
    vista_.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()