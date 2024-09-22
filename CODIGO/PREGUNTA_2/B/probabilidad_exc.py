#Ahora debo calcular la probabilidad de excedencia
from lectura_xlsx import df_precipitaciones

def calcular_probabilidad_excedencia(df, columna):

    # Ordenar los datos de mayor a menor
    df_sorted = df.sort_values(by=columna, ascending=False)
    df_sorted.reset_index(drop=True, inplace=True)
    
    # Número total de eventos
    N = len(df_sorted)
    
    # Calcular la probabilidad de excedencia
    df_sorted['Probabilidad_Excedencia'] = ((df_sorted.index + 1) / (N + 1)) * 100
    
    return df_sorted

# Ejemplo de uso
columna = 'ACCESS1-0 [r1i1p1]'  # Cambia esto por el nombre de tu columna real
df_probabilidad_exc = calcular_probabilidad_excedencia(df_precipitaciones, columna)

