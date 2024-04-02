from Opinion import Opinion
#------------------------------------------------------------------------------------
# Creacion de la clase Encuesta para la gestion de las opiniones
#------------------------------------------------------------------------------------

class Encuesta:
#--------------------------------------------------------------------------------------------
# | Metodos | - constructor, agregar opinion a una encuesta, calcular el promedio,
# numero total de opiniones en una encuesta, calcular promedio por sectores demograficos 
#--------------------------------------------------------------------------------------------
    def __init__(self):
        self.encuestados = [] # Una lista para guardar las opiniones en la encuestas
    
    # Agrega una opinion a la encuesta
    def agregarOpinion(self, opinion_a_Agregar): 
        self.encuestados.append(opinion_a_Agregar)
        # print("se ha agregado correctamente") - para demostrar que se han agregado a la lista

    # calcula el promedio de las valoraciones de las opiniones en la encuesta
    def promedioTotalValoraciones(self):  
        if not self.encuestados: # comprueba que la lista no este vacia
            return print("No hay datos para promediar")
        
        valoraciones = sum(opinion.consultarValor() for opinion in self.encuestados) # suma  todas las valoraciones
        return print(f"El promedio total de las valoraciones es: {valoraciones / len(self.encuestados)}")

    #  Devuelve el total de personas encuestadas (numero de items en la lista)
    def numeroTotalOpiniones(self):
        return print(f"El numero total de encuestas realizadas es: {len(self.encuestados)}")
    
    # Calcula el promedio por sector demografico
    def promedioPorSectorDemografico(self, rango_edad, estado_civil):
        if not self.encuestados:
            return print("No hay opiniones del sector mencionado registradas  en la encuesta.")
        

        opiniones_sector = [
            opinion.consultarValor() for opinion in self.encuestados
            if opinion.consultarEstadoCivil() == estado_civil and opinion.consultarRangoEdad() == rango_edad
            ] # una lista en las que se agregaran solo las valoraciones de los sectores especificados
        

        promedio = sum(opiniones_sector) / len(opiniones_sector) # calcula el promedio
        print(f"El promedio para el sector demográfico {rango_edad} y {estado_civil} es: {promedio}")