#------------------------------------------------------------------------------------
# Creacion de  la clase para el manejo de creacion de opiniones
#------------------------------------------------------------------------------------
class Opinion:

#------------------------------------------------------------------------------------
# Metodos - constructor, y de retorno de atributos
#------------------------------------------------------------------------------------
    def __init__(self, valor, rango_edad, estado_civil):
        # valor entre 0 y 10
        self.valor = valor 

        # Menor de 18, Entre 18 y 54, 55 o más
        self.rango_edad = rango_edad 

        # Casado o Soltero
        self.estado_civil = estado_civil 

    # Valida que el valor sea correcto
    def consultarValor(self): 
        if 0 <= self.valor <= 10:
            return self.valor
        else:
            return print("Valor inválido")
        
    # retorna el rango de edad
    def consultarRangoEdad(self): 
        return self.rango_edad
    
    # retorna el estado civil
    def consultarEstadoCivil(self): 
        return self.estado_civil

