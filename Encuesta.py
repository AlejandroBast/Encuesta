from Opinion import Opinion
class Encuesta:
    def __init__(self):
        self.encuestados = []

    def agregarOpinion(self, opi):
        self.encuestados.append(opi)
        print("se ha agregado correctamente")

    def promedioTotal(self):
        if not self.encuestados:
            return print("No hay datos para promediar")
        
        valoraciones = sum(opinion.valor for opinion in self.encuestados)
        return print(f"El promedio total de las valoraciones es: {valoraciones / len(self.encuestados)}")
        
    def numeroTotalOpiniones(self):
        return print(f"El numero total de encuestas realizadas es: {len(self.encuestados)}")
    
    def promedioPorSectorDemografico(self, rango_edad, estado_civil):
        if not self.encuestados:
            return print("No hay opiniones del sector mencionado registradas  en la encuesta.")
        

        opiniones_sector = [opinion.valor for opinion in self.encuestados if opinion.estado_civil == estado_civil and opinion.rango_edad == rango_edad]

        promedio = sum(opiniones_sector) / len(opiniones_sector)
        print(f"El promedio para el sector demográfico {rango_edad} y {estado_civil} es: {promedio}")