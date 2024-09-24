from probabilidad_exc import df_probabilidad_exc
import numpy as np


#Para distribucion Normal
#primero debo calcular w
w = (np.log(1/(df_probabilidad_exc['Probabilidad_Excedencia']/100)))**0.5
#Ahora calculo el valor de z
z = w - (2.515517 + 0.802853*w + 0.010328 * (w**2))/(1 + 1.432788 * w + 0.189269 * (w**2) + 0.001308 * (w**3))
#Luego simplemente kt es igual a z
df_probabilidad_exc['Kt Normal'] = z

#para distribucion Log-Normal
df_probabilidad_exc['Log de Precipitación'] = np.log(df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'])
media_log = df_probabilidad_exc['Log de Precipitación'].mean()
desviacion_std_log = df_probabilidad_exc['Log de Precipitación'].std()
df_probabilidad_exc['Kt Log-Normal'] = (df_probabilidad_exc['Log de Precipitación'] - media_log) / desviacion_std_log
df_probabilidad_exc.drop('Log de Precipitación', axis=1, inplace=True)

#Para una dsitribucion Person III
# Parámetros estimados de la distribución gamma
alpha = 2.5  # Parámetro de forma (similares a los de una Pearson Type II)
beta = 2     # Parámetro de escala

# Calcular la media y la desviación estándar de la distribución gamma
media = alpha * beta
desviacion_std = np.sqrt(alpha * beta**2)
df_probabilidad_exc['Kt Pearson III'] = (df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'] - media) / desviacion_std

#Para una distribucion Gumbel
mu = np.mean(df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'])  # Esto es una simplificación
beta = np.std(df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'], ddof=1) * np.sqrt(6) / np.pi

#Considero n = 30 años, por lo tanto
n = 30
yn = 0.5362
sigman = 1.1124
T = 1/(df_probabilidad_exc['Probabilidad_Excedencia']/100)
yt = -np.log(-np.log((T-1)/T))
# Calcular el coeficiente Kt para la distribución Gumbel
df_probabilidad_exc['Kt Gumbel'] = (yt - yn) / sigman

df = df_probabilidad_exc


