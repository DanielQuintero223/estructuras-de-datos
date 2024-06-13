class punto():
    def __init__(self, nombre, dinero_recolectar):
        self.nombre = nombre
        self.dinero_ = dinero_recolectar
        
    def mostrar_dinero(self):
        print("El dinero almacenado en este punto de recolección es: ", self.dinero_)

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_dinero(self):
        return self.dinero_

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_dinero(self, dinero):
        self.dinero_ = dinero
