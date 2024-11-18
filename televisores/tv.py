class TV:
    numTV = 0  # Atributo de clase que lleva el conteo de televisores creados

    def __init__(self, marca, estado):
        self.marca = marca  # Marca asociada al televisor
        self.canal = 1  # Canal por defecto
        self.precio = 500  # Precio por defecto
        self.estado = estado  # Estado del televisor (encendido o apagado)
        self.volumen = 1  # Volumen por defecto
        self.control = None  # Control asociado (inicialmente ningún control)
        TV.numTV += 1  # Incrementamos el contador de televisores

    def setControl(self, control):
        self._control = control  # Asocia el control al televisor

    def getControl(self):
        return self._control    

    def getMarca(self):
        return self.marca  # Obtener la marca del televisor

    def setMarca(self, marca):
        self.marca = marca  # Establecer la marca del televisor

    def getCanal(self):
        return self.canal  # Obtener el canal actual

    def setCanal(self, canal):
        if self.estado and 1 <= canal <= 120:  # Verificamos que el televisor esté encendido y el canal esté en el rango permitido
            self.canal = canal  # Establecer el canal

    def getPrecio(self):
        return self.precio  # Obtener el precio del televisor

    def setPrecio(self, precio):
        self.precio = precio  # Establecer el precio del televisor

    def getVolumen(self):
        return self.volumen  # Obtener el volumen

    def setVolumen(self, volumen):
        if self.estado and 0 <= volumen <= 7:  # Verificamos que el televisor esté encendido y el volumen esté en el rango permitido
            self.volumen = volumen  # Establecer el volumen

    def getEstado(self):
        return self.estado  # Obtener el estado del televisor (encendido o apagado)

    def turnOn(self):
        self.estado = True  # Encender el televisor

    def turnOff(self):
        self.estado = False  # Apagar el televisor

    def canalUp(self):
        if self.estado and self.canal < 120:  # Verificamos que el televisor esté encendido y el canal no supere 120
            self.canal += 1  # Aumentar el canal

    def canalDown(self):
        if self.estado and self.canal > 1:  # Verificamos que el televisor esté encendido y el canal no sea menor a 1
            self.canal -= 1  # Disminuir el canal

    def volumenUp(self):
        if self.estado and self.volumen < 7:  # Verificamos que el televisor esté encendido y el volumen no supere 7
            self.volumen += 1  # Aumentar el volumen

    def volumenDown(self):
        if self.estado and self.volumen > 0:  # Verificamos que el televisor esté encendido y el volumen no sea menor a 0
            self.volumen -= 1  # Disminuir el volumen

    @classmethod
    def getNumTV(cls):
        return cls.numTV  # Obtener la cantidad de televisores creados
