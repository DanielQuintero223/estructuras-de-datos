class banco():
    def __init__(self, dineroG):
        self.dinero_guardado = dineroG
        
    def mostrar_banco(self):
        print("Dinero guardado en el banco : ", self.dinero_guardado)
    
    # Getter
    def get_dinero_guardado(self):
        return self.dinero_guardado

    # Setter
    def set_dinero_guardado(self, dinero_guardado):
        self.dinero_guardado = dinero_guardado
