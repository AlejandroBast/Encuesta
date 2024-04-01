class Opinion:
    def __init__(self, valor, rango_edad, estado_civil):
        self.valor = valor
        self.rango_edad = rango_edad
        self.estado_civil = estado_civil

    def consultarValor(self):
        if 0 <= self.valor <= 10:
            return self.valor
        else:
            return "Valor inválido"

    def consultarRangoEdad(self):
        return self.rango_edad

    def consultarEstadoCivil(self):
        return self.estado_civil

