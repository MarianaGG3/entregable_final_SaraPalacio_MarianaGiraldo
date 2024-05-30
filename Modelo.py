import json
import os

class PacienteDato:
    def __init__(self,ruta='datos.json'):
        self.ruta= ruta
        self.load_data()

    def load_data(self):
        try:
            with open(self.ruta, 'r') as file:
                self.paciente= json.load(file)
        except FileExistsError:
            self.paciente=[]
            print('no existe')
        #if os.path.exists(self.ruta):
         #       with open(self.ruta, 'r') as file:
          #          self.paciente= json.load(file)
        #else:
         #   self.paciente=[]
            

    def salvar_datos(self):
        with open(self.ruta, 'w') as file:
            json.dump(self.paciente, file, indent=4)

    def añadir_paciente(self,paciente: dict):
        if not any(p['id'] == paciente['id'] for p in self.paciente):
            self.paciente.append(paciente)
            self.salvar_datos()
            return True
        return False
    
    def eliminar_paciente(self,paciente_id: str):
        initLen= len(self.paciente)
        self.paciente=[p for p in self.paciente if p['id']!= paciente_id]
        self.salvar_datos()
        if initLen == len(self.paciente):
            return 0
        else:
            return 1
        
    def buscar_paciente(self, pacientes_nombre: str): 
        pacientes_nombre=pacientes_nombre.lower().strip()
        #return [Paciente(**p) for p in self.paciente if p['nombre'].lower().startswith(buscar.lower())]
        return [p for p in self.paciente if p['nombre'].lower().strip().startswith(pacientes_nombre)]