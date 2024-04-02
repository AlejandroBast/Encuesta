from Encuesta import  Encuesta
from Opinion import Opinion

### Ejemplo de uso

## Crear opiniones
# Menores de 18 años
opínion1 = Opinion(1, "Menor de 18", "soltero")
opínion2 = Opinion(0, "Menores de 18", "soltero")
opínion3 = Opinion(5, "Menor de 18", "soltero")
opínion4 = Opinion(4, "Menores de 18", "soltero")
opínion5 = Opinion(6, "Menor de 18", "soltero")

# Entre 18 y 54 años
opínion6 = Opinion(2, "Entre 18 y 54", "soltero")
opínion7 = Opinion(3, "Entre 18 y 54", "casado")
opínion8 = Opinion(8, "Entre 18 y 54", "casado")
opínion9 = Opinion(9, "Entre 18 y 54", "soltero")
opínion10 = Opinion(6, "Entre 18 y 54", "casado")

# Con 55 o más años
opínion11 = Opinion(8, "55 o más", "casado")
opínion12 = Opinion(7, "55 o más", "soltero")
opínion13 = Opinion(5, "55 o más", "casado")
opínion14 = Opinion(6, "55 o más", "casado")
opínion15 = Opinion(4, "55 o más", "casado")

# Creamos la encuesta para agregar las opiniones
encuestita = Encuesta()
encuestita.agregarOpinion(opínion1)
encuestita.agregarOpinion(opínion2)
encuestita.agregarOpinion(opínion3)
encuestita.agregarOpinion(opínion4)
encuestita.agregarOpinion(opínion5)
encuestita.agregarOpinion(opínion6)
encuestita.agregarOpinion(opínion7)
encuestita.agregarOpinion(opínion8)
encuestita.agregarOpinion(opínion9)
encuestita.agregarOpinion(opínion10)
encuestita.agregarOpinion(opínion11)
encuestita.agregarOpinion(opínion12)
encuestita.agregarOpinion(opínion13)
encuestita.agregarOpinion(opínion14)
encuestita.agregarOpinion(opínion15)

#calculamos el promedio
encuestita.promedioTotalValoraciones()

# mostramos el total de opiniones que hay en la encuesta
encuestita.numeroTotalOpiniones()

# calculamos el promedio por sectores
encuestita.promedioPorSectorDemografico("Menor de 18", "soltero")
encuestita.promedioPorSectorDemografico("Entre 18 y 54", "soltero")
encuestita.promedioPorSectorDemografico("Entre 18 y 54", "casado")
encuestita.promedioPorSectorDemografico("55 o más", "casado")
encuestita.promedioPorSectorDemografico("55 o más", "soltero")




#no cres q agregar un valor incorrecto en las encuestas seria un poco mas entendible,
#me refiero hacer una encuesta en el que valor sea mayor a 10 xd
# hmmmmmmm la verdad no te entendi xd, pero creo que te refieres ala comprobacion, no?
# aaaaa comprobar si es correcto
# ya solucione, era porque no acediamos a los atributos directamente, en vez de llamar a los metodos que retornan sus atributos
# no wn ksakaj alfin, llevamos bastante en esto
# ya funciona, jskajs re insanos uwu
