#Importar el paquete o los paquetes con los que vamos analizar la información
import pandas as pd
def analizarCanastaBasica():


#2 Sin importar la fuente (sql, xls, JSON, csv...)
#crear una tabla tabulada que se llama DATAFRAME
 tabla=pd.read_csv("./data/bdcanasta.csv")
 print (tabla)
 #3 Aplico filtros para limpiar o seleccionar datos
 #print(tabla.head(20)) #primero N registros
 #print (tabla.tail())
 print(tabla.describe())