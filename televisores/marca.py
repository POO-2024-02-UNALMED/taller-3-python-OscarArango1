class Marca:
    def __init__(self, nombre):
        self._nombre = nombre  # Atributo privado para el nombre de la marca

    def getNombre(self):
        return self._nombre  # Método para obtener el nombre de la marca

    def setNombre(self, nombre):
        self._nombre = nombre  # Método para establecer el nombre de la marca
