class ladrones():
    def __init__(self, ataque, escudo):
        self.ataque = ataque * 3
        self.escudo = escudo * 3
        self.vehiculos = 3
    
    def mostrar_ladrones(self):
        print("Ataque: ", self.ataque)
        print("Escudo: ", self.escudo)
        print("Vehículos: ", self.vehiculos)

    # Getters
    def get_ataque(self):
        return self.ataque

    def get_escudo(self):
        return self.escudo

    def get_vehiculos(self):
        return self.vehiculos

    # Setters
    def set_ataque(self, ataque):
        self.ataque = ataque * 3

    def set_escudo(self, escudo):
        self.escudo = escudo * 3

    def set_vehiculos(self, vehiculos):
        self.vehiculos = vehiculos





