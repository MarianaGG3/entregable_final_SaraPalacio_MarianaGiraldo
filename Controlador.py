from Vista import *
from Modelo import *
import sys

def main():
    app = QApplication(sys.argv)
    vista_=VentanaIngreso()
    vista_.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()