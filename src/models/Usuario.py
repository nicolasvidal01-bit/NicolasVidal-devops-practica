import uuid

class Usuario:
    def __init__(self, nombre: str, correo: str):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.correo = correo

    def isadmin(self) -> bool:
        return False

class Cliente(Usuario):
    def __init__(self, nombre: str, correo: str, direccion: str):
        super().__init__(nombre, correo)
        self.direccion = direccion

class Administrador(Usuario):
    def __init__(self, nombre: str, correo: str):
        super().__init__(nombre, correo)

    def isadmin(self) -> bool:
        return True
