from kt_segun_distribucion import df
import matplotlib.pyplot as plt

plt.figure(figsize=(19.2, 10.8))  # Tamaño en pulgadas que corresponde a 1920x1080 píxeles
plt.rcParams.update({'font.size': 16})  # Ajusta el tamaño base de la fuente
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.09)

def graficar_columnas(df, columna_x, columna_y, color):

    plt.plot(df[columna_y], df[columna_x], marker='o', linestyle='-', color=color)

    

graficar_columnas(df, 'MAXIMA EN 24 HS. PRECIPITACION (mm)', 'Kt Normal', 'red')
graficar_columnas(df, 'MAXIMA EN 24 HS. PRECIPITACION (mm)', 'Kt Log-Normal', 'green')
graficar_columnas(df, 'MAXIMA EN 24 HS. PRECIPITACION (mm)', 'Kt Pearson III', 'blue')
graficar_columnas(df, 'MAXIMA EN 24 HS. PRECIPITACION (mm)', 'Kt Gumbel', 'black')
# Título del gráfico 
plt.title(f'Gráfico de Precipitacion vs Coeficiente de Frecuencia',fontsize=25)
plt.legend(['Normal', 'Log-Normal', 'Pearson III', 'Gumbel'], fontsize=18)
# Etiquetas de los ejes
plt.ylabel("Precipitacion", fontsize=18)
plt.xlabel("Frecuencia segun distribucion", fontsize=18)

# Guardar el gráfico como una imagen JPG con la resolución deseada
plt.savefig('grafico.jpg', format='jpg', dpi=100)

# Cerrar la figura para liberar memoria
plt.close()