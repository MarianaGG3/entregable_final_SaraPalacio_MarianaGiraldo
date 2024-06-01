import json


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
            

    def salvar_datos(self):
        with open(self.ruta, 'w') as file:
            json.dump(self.paciente, file, indent=4)

    def anadir_paciente(self,paciente: dict):
        if not any(p['id'] == paciente['id'] for p in self.paciente):
            self.paciente.append(paciente)
            self.salvar_datos()
            return True
        return False
    


    def eliminar_paciente(self, paciebnte_id: str):  # Cambiar aquí
        initLen= len(self.paciente)
        self.paciente=[p for p in self.paciente if p['id']!= paciebnte_id]  # Cambiar aquí también
        self.salvar_datos()
        if initLen == len(self.paciente):
            return 0
        else:
            return 1

    def buscar_paciente(self, pacientes_nombre: str):
        pacientes_nombre = pacientes_nombre.lower().strip()
        return [p for p in self.paciente if pacientes_nombre in p['nombre'].lower().strip() or pacientes_nombre in p['apellido'].lower().strip()]



class coordinador:
    def __init__(self):
        self.database= PacienteDato()

    def add_patient(self, data:dict):
        return self.database.anadir_paciente(data)

    def del_patient(self, id: str):
        self.database.eliminar_paciente(id)

    def search_patients(self, initName: str = ''):
        return self.database.buscar_paciente(initName)