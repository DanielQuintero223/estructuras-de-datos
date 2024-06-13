class vehiculo():
    # constructor
    def __init__(self, tipo_vehiculo, velocidad, escudo, ataque,escoltas , dinero_recogido, peso):
        self.tipo_vehiculo = tipo_vehiculo
        self.velocidad = velocidad
        self.escudo = escudo
        self.ataque = ataque
        self.escoltas = escoltas
        self.dinero_recogido = dinero_recogido
        self.peso = peso

    # Getters
    def get_tipo_vehiculo(self):
        return self.tipo_vehiculo

    def get_velocidad(self):
        return self.velocidad

    def get_escudo(self):
        return self.escudo

    def get_ataque(self):
        return self.ataque

    def get_escoltas(self):
        return self.escoltas

    def get_dinero_recogido(self):
        return self.dinero_recogido

    def get_peso(self):
        return self.peso

    # Setters
    def set_tipo_vehiculo(self, tipo_vehiculo):
        self.tipo_vehiculo = tipo_vehiculo

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_escudo(self, escudo):
        self.escudo = escudo

    def set_ataque(self, ataque):
        self.ataque = ataque

    def set_escoltas(self, escoltas):
        self.escoltas = escoltas

    def set_dinero_recogido(self, dinero_recogido):
        self.dinero_recogido = dinero_recogido

    def set_peso(self, peso):
        self.peso = peso




    def mostrar_vehiculos(self):
        print("Tipo de vehiculo: ", self.tipo_vehiculo)
        print("Velocidad: ", self.velocidad)
        print("Escudo: ", self.escudo)
        print("Ataque: ", self.ataque)
        print("Escoltas: ", self.escoltas)
        print("Peso: ", self.peso)