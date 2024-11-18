class Control:
    def __init__(self):
        self.tv = None  # Control inicialmente no enlazado con ningún televisor

    def enlazar(self, televisor):
        self.tv = televisor  # Enlazamos el control con un televisor
        televisor.setControl(self)  # Enlazamos el televisor con el control

    def getTv(self):
        return self.tv  # Retorna el televisor asociado al control

    def setTv(self, tv):
        self.tv = tv  # Establece el televisor asociado al control

    def turnOn(self):
        if self.tv:  # Si hay un televisor asociado
            self.tv.turnOn()  # Llamamos al método turnOn del televisor

    def turnOff(self):
        if self.tv:  # Si hay un televisor asociado
            self.tv.turnOff()  # Llamamos al método turnOff del televisor

    def canalUp(self):
        if self.tv:  # Si hay un televisor asociado
            self.tv.canalUp()  # Llamamos al método canalUp del televisor

    def canalDown(self):
        if self.tv:  # Si hay un televisor asociado
            self.tv.canalDown()  # Llamamos al método canalDown del televisor

    def volumenUp(self):
        if self.tv:  # Si hay un televisor asociado
            self.tv.volumenUp()  # Llamamos al método volumenUp del televisor

    def volumenDown(self):
        if self.tv:  # Si hay un televisor asociado
            self.tv.volumenDown()  # Llamamos al método volumenDown del televisor

    def setCanal(self, canal):
        if self.tv:  # Si hay un televisor asociado
            self.tv.setCanal(canal)  # Establecemos el canal directamente en el televisor

    def setVolumen(self, volumen):
        if self.tv:  # Si hay un televisor asociado
            self.tv.setVolumen(volumen)  # Establecemos el volumen directamente en el televisor
