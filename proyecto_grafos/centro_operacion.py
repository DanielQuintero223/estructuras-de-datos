class centro_operacion():
    def __init__(self, limiteD, limiteV, limiteE, dineroG, vehiculosG):
        self.limite_dinero = limiteD
        self.limite_vehiculos = limiteV
        self.limite_escoltas = limiteE
        self.dinero_guardado = dineroG
        self.vehiculos_guardados = vehiculosG
    
    def mostrar_centro_operacion(self):
        print("Límite de dinero: ", self.limite_dinero)
        print("Límite de vehículos: ", self.limite_vehiculos)
        print("Límite de escoltas: ", self.limite_escoltas)
        print("Dinero guardado: ", self.dinero_guardado)
        print("Vehículos guardados: ", self.vehiculos_guardados)

    # Getters
    def get_limite_dinero(self):
        return self.limite_dinero

    def get_limite_vehiculos(self):
        return self.limite_vehiculos

    def get_limite_escoltas(self):
        return self.limite_escoltas

    def get_dinero_guardado(self):
        return self.dinero_guardado

    def get_vehiculos_guardados(self):
        return self.vehiculos_guardados

    # Setters
    def set_limite_dinero(self, limite_dinero):
        self.limite_dinero = limite_dinero

    def set_limite_vehiculos(self, limite_vehiculos):
        self.limite_vehiculos = limite_vehiculos

    def set_limite_escoltas(self, limite_escoltas):
        self.limite_escoltas = limite_escoltas

    def set_dinero_guardado(self, dinero_guardado):
        self.dinero_guardado = dinero_guardado

    def set_vehiculos_guardados(self, vehiculos_guardados):
        self.vehiculos_guardados = vehiculos_guardados
