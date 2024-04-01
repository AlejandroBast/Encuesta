from Encuesta import  Encuesta
from Opinion import Opinion


### opiniones
# Menores de 18 años
opínion1 = Opinion(1, "Menor de 18", "soltero")
opínion2 = Opinion(6, "Menores de 18", "soltero")
# Entre 18 y 54 años
opínion3 = Opinion(5, "Entre 18 y 54", "soltero")
opínion4 = Opinion(5, "Entre 18 y 54", "casado")
# Con 55 o más años
opínion5 = Opinion(3, "55 o más", "casado")
opínion6 = Opinion(3, "55 o más", "casado")

# encuesta
encuestita = Encuesta()
encuestita.agregarOpinion(opínion1)
encuestita.agregarOpinion(opínion2)
encuestita.agregarOpinion(opínion3)
encuestita.agregarOpinion(opínion4)
encuestita.agregarOpinion(opínion5)
encuestita.agregarOpinion(opínion6)

# promedio total
encuestita.promedioTotal()

# numero total de encuestas
encuestita.numeroTotalOpiniones()

# promedio por Sector Demografico

encuestita.promedioPorSectorDemografico("Menor de 18", "soltero") # 6
encuestita.promedioPorSectorDemografico("Entre 18 y 54", "soltero") # 5
encuestita.promedioPorSectorDemografico("55 o más", "casado") # 3




#no cres q agregar un valor incorrecto en las encuestas seria un poco mas entendible,
#me refiero hacer una encuesta en el que valor sea mayor a 10 xd
# hmmmmmmm la verdad no te entendi xd, pero creo que te refieres ala comprobacion, no?
# aaaaa comprobar si es correcto
