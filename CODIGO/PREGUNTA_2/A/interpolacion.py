from kt_segun_distribucion import df
import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

plt.figure(figsize=(19.2, 10.8))  # Tamaño en pulgadas que corresponde a 1920x1080 píxeles
plt.rcParams.update({'font.size': 16})  # Ajusta el tamaño base de la fuente
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.09)

def graficar_columnas(df, columna_x, columna_y, color):

    plt.plot(df[columna_y], df[columna_x], marker='o', linestyle='-', color=color)

eje_y = df['MAXIMA EN 24 HS. PRECIPITACION (mm)']

def linear_interpolation(eje_x, eje_y, x_new, nombre):
    # Calcular la pendiente (m) y la ordenada al origen (b) de la recta y = mx + b
    m, b = np.polyfit(eje_x, eje_y, 1)
    
    # Generar los puntos de la recta para los nuevos valores de x
    y_new = m * x_new + b
    
    # Crear un nuevo DataFrame con los resultados interpolados
    df_interpolated = pd.DataFrame({nombre: x_new, 'MAXIMA EN 24 HS. PRECIPITACION (mm)': y_new})
    
    # Devolver el DataFrame, la pendiente y la ordenada al origen
    return df_interpolated, m, b

#primero hago la interpolacion de Normal
eje_x = df['Kt Normal']
# Puntos nuevos donde queremos interpolar
x_new = np.linspace(min(eje_x), max(eje_x), num=100)
# Llamar a la función de interpolación
df_normal, pendiente_normal, intercepto_normal = linear_interpolation(eje_x, eje_y, x_new, 'Normal Interpolado')

#ahora hago la interpolacion de log normal
#Genero un pequeño ajuste para que no haya problemas con el logaritmo
# Selecciona la columna donde quieres hacer el reemplazo
columna = 'Kt Log-Normal'

# Identificar el valor máximo y mínimo
valor_maximo = df[columna].max()
valor_minimo = df[columna].min()

# Reemplazar el valor máximo por el valor mínimo
#df[columna] = df[columna].replace(valor_maximo, valor_minimo)

# Reemplazar los NaN por el valor mínimo
df[columna] = df[columna].fillna(valor_maximo)

eje_x = df['Kt Log-Normal']
# Puntos nuevos donde queremos interpolar
x_new = np.linspace(min(eje_x), max(eje_x), num=100)
# Llamar a la función de interpolación
df_log_normal, pendiente_log_normal, intercepto_log_normal = linear_interpolation(eje_x, eje_y, x_new, 'Log-Normal Interpolado')

#ahora hago la interpolacion de Pearson III
eje_x = df['Kt Pearson III']
# Puntos nuevos donde queremos interpolar
x_new = np.linspace(min(eje_x), max(eje_x), num=100)
# Llamar a la función de interpolación
df_pearson, pendiente_pearson, intercepto_pearson = linear_interpolation(eje_x, eje_y, x_new, 'Pearson III Interpolado')

#ahora hago la interpolacion de Gumbel
eje_x = df['Kt Gumbel']
# Puntos nuevos donde queremos interpolar
x_new = np.linspace(min(eje_x), max(eje_x), num=100)
# Llamar a la función de interpolación
df_gumbel, pendiente_gumbel, intercepto_gumbel = linear_interpolation(eje_x, eje_y, x_new, 'Gumbel Interpolado')

#Ahora grafico
graficar_columnas(df_normal, 'MAXIMA EN 24 HS. PRECIPITACION (mm)', 'Normal Interpolado', 'red')
graficar_columnas(df_log_normal, 'MAXIMA EN 24 HS. PRECIPITACION (mm)', 'Log-Normal Interpolado', 'green')
graficar_columnas(df_pearson, 'MAXIMA EN 24 HS. PRECIPITACION (mm)', 'Pearson III Interpolado', 'blue')
graficar_columnas(df_gumbel, 'MAXIMA EN 24 HS. PRECIPITACION (mm)', 'Gumbel Interpolado', 'black')


#Finalmente guardo el grafico como una imagen JPG con la resolución deseada
# Título del gráfico 
plt.title(f'Gráfico de',fontsize=25)
plt.legend(['Normal Interpolada', 'Log-Normal Interpolada', 'Pearson III Interpolada', 'Gumbel Interpolada'], fontsize=18)
# Etiquetas de los ejes
plt.ylabel("Precipitacion", fontsize=18)
plt.xlabel("Frecuencia segun distribucion", fontsize=18)

# Guardar el gráfico como una imagen JPG con la resolución deseada
plt.savefig('grafico_interpolado.jpg', format='jpg', dpi=100)

# Cerrar la figura para liberar memoria
plt.close()



