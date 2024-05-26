from Vista import *
from Modelo import *
import sys

app = QApplication(sys.argv)
vista_=VentanaIngreso()
vista_.show()
sys.exit(app.exec_())