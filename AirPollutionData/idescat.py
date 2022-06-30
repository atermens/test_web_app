# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from . import EOI_DATA

#----------------------------------------------------------------------------------------------------------------------------------
# Indicador: Indice de envejecimiento
#
# Definicion: Expresa la relacion entre la cantidad de personas adultas mayores y la cantidad de menores.
#
# Calculo: Cociente entre personas de 65 y mas con respecto a las personas menores de 15, multiplicado por 100.
#
# 100 * (P_65_I_MES / P_0_14)
#
# Interpretacion estadistica: Un valor de 10 significa que hay 10 adultos mayores (de 65 y más) por cada 100 menores de 15.
#
# Interpretacion contextual y pertinencia: En la sociedad occidental, si bien se reconoce que la vejez es un fenomeno multidimensional, 
# suele estar definida por límites de edad. En los pueblos indígenas, lo que distingue la vejez es el cambio de etapa en el ciclo vital 
# y el limite cronologico pierde sentido; a lo sumo puede establecerse una frontera asociada a la perdida de capacidades fisiologicas 
# o cuando no pueden realizar tareas para la reproduccion material de la familia y comunidad. Asimismo, el estatus y el rol social 
# puede aumentar en la medida en que se "envejece", ya que se trata de las personas que atesoran la sabiduria y la memoria colectiva 
# que debe ser transmitida a los jovenes para asegurar la reproduccion cultural del grupo o pueblo. Por lo tanto, no cabe una 
# interpretacion "negativa", sino de continuidad cultural.
#
# Observaciones: Segun su interpretacion convencional, se trata de un indicador asociado a las transferencias intergeneracionales 
# y su aumento sistematico implica para los estados una mayor inversion en salud y seguridad social orientada a las personas de edad, 
# beneficios de los cuales no deberian estar exentos los pueblos indígenas.
#
# En Espanya el indice de envejecimiento con las cifras de 2021 se situaba en el 129.1% segun apunta el INE. 
# Siendo bastante superior (casi por un 30%) el numero de personas mayores de 65 años que el de adolescentes, podemos ver como el 
# envejecimiento de la poblacion es un hecho. Con el avance de la esperanza de vida y la disminucion de la natalidad, la piramide 
# demografica se va invirtiendo, teniendo cada vez una base mas estrecha.
#
# Ademas, analizando los datos que nos ofrece el INE podemos definir este aumento como progresivo y sostenido en el tiempo. 
# El indice de envejecimiento lleva subiendo sin parar en los ultimos años. En 2020 el indice de envejecimiento era del 125.75%. 
# En 2018, el indice de envejecimiento se situaba en el 120.46%. En 2017 este indice no superaba el 120%. 
#
# Como vemos, el indicador de envejecimiento crece anyo tras anyo debido a un envejecimiento de la poblacion y a un descenso en la 
# natalidad. En enero de 2021, se calculaba que las personas mayores de 65 anyos eran mas de 9 millones. 
# Esto se traduce en que alrededor del 19% de la población española son personas mayores.  Conviene recordar que las personas 
# mayores de 65 suponen mas o menos una quinta parte de los españoles para poder darles la importancia demografica que se merecen. 
#
# Para hacernos una mayor idea del volumen de personas mayores podemos compararlos con otros grupos en Espanya para relativizar 
# su importancia. En 2021, mismo anyo en el que se calculaban 9 millones de personas mayores de 65 años, se registraban 2.7 millones 
# de empleados publicos. Siendo los funcionarios un volumen de la poblacion activa importante, conviene recordar que las personas 
# mayores son un grupo de poblacion tres veces más numeroso.
#
# Si incluimos en estos calculos tanto al sector publico como al privado, se contabiliza que en 2022 hay 19 millones de personas 
# trabajando en nuestro pais. Este volumen de trabajadores es poco mas del doble que el de personas mayores de 65 anyos. 
# Hay que tener en cuenta que en estas cifras se contabiliza a todas las personas que estan cotizando, sin importar el tipo de contrato. 
# Trabajadores con media jornada, contratos de practicas o sueldos precarios tambien entran en esos 19 millones. 
# Estas cifras muestran un equilibrio delicado, ya que la cotizacion de estos trabajadores es un pilar fundamental del que dependen las pensiones. 
#
# El indice de envejecimiento creciente es una realidad que se debe tener en cuenta desde la administracion publica para crear una 
# sociedad inclusiva e igualitaria. 
# El cambio demografico que estamos viviendo ofrece una oportunidad para adaptarnos como sociedad si sabemos como. 
#
#----------------------------------------------------------------------------------------------------------------------------------


# buffer_poblacion_500m.csv
#            0     1     2     3      4       5
#EOI_DATA[codi_eoi]["POBLACION_500M "] = [TOTAL,HOMES,DONES,P_0_14,P_15_64,P_65_I_MES,P_ESPANYOL,P_ESTRANGE,P_NASC_CAT,P_NASC_RES,P_NASC_EST]


def get_CVP(eoi_code, iP = 1):
    # iP: num. indice o tasa
    # 0. El indice o mal llamada «tasa» de envejecimiento (por que no es una tasa), 
    #    en realidad es simplemente la proporcion de mayores de 64 anyos
    #    = ((Poblacion >64 anyos / Poblacion total) x100) (proporcion de individuos 
    #    mayores de 64 anyos sobre el total de la poblacion. Se suele expresar como porcentaje).
    #
    # 1. 100* (P_0_14 + P_65_I_MES) / TOTAL  que es la poblacio vulnerable (= docs Joan)
    #
    # 2. Index d'envelliment (IDESCAT). Poblacio de 65 anys i mes per cada 100 habitants de menys de 15 anys.
    
    dict = EOI_DATA.get(eoi_code, {})
    llista = dict.get("POBLACION_500M", [])
    if not llista: return np.nan
    
    # comprovem que hem trobat les dades associades a l'estacio. 
    total = float(llista[0])
    p_0_14 = float(llista[3])
    p_65 = float(llista[5])

    if iP == 0:
        return round(100.0 * p_65 / total, 2)
    elif iP == 1:
        return round(100.0 * (p_0_14 + p_65) / total, 2)
    elif iP == 2:
        return round(100.0 * p_65 / p_0_14, 2)
    else:
        return np.nan 



if __name__ == '__main__':  
    #'08101001': [52579,25616,26940,7585,35542,9280,36791,15545,19944,10495,21981]
    # total = 52579  |  p_0_14 = 7585  |  p_65 = 9280
    # iP=1: 100*9280/52579 = 17.6496319824
    # iP=2: 100*9280/7585 = 122.346736981
    
    cvp = get_CVP('08101001',1)
    print(f" CVP (iP=1) for 08101001: {cvp} | 17.6496319824")
    
    cvp = get_CVP('08101001')
    print(f" CVP (iP=1 default) for 08101001: {cvp}")
    
    cvp = get_CVP('08101001',2)
    print(f" CVP (iP=2) for 08101001: {cvp} | 122.346736981")

