from probabilidad_exc import df_probabilidad_exc
import numpy as np

#Para distribucion Normal
#primero que nada, si P es menor que 50, se debe calcular 1 - P

p_ajustado = (df_probabilidad_exc['Probabilidad_Excedencia']/100).apply(lambda x: 1 - x if x < 50 else x)
#primero debo calcular w
w = (np.log(1/(p_ajustado)))**0.5
#Si p es menor que 50, uasar 1 - P

#Ahora calculo el valor de z
Z = -w + (2.515517 + 0.802853*w + 0.010328 * (w**2))/(1 + 1.432788 * w + 0.189269 * (w**2) + 0.001308 * (w**3))
#Luego simplemente kt es igual a z
df_probabilidad_exc['Kt Normal'] = Z

#para distribucion Log-Normal
# df_probabilidad_exc['Log de Precipitación'] = np.log(df_probabilidad_exc['ACCESS1-0 [r1i1p1]'])
# media_log = df_probabilidad_exc['Log de Precipitación'].mean()
# desviacion_std_log = df_probabilidad_exc['Log de Precipitación'].std()
# df_probabilidad_exc['Kt Log-Normal'] = (df_probabilidad_exc['Log de Precipitación'] - media_log) / desviacion_std_log
# df_probabilidad_exc.drop('Log de Precipitación', axis=1, inplace=True)
w = np.log(w)
Z_log = -w + (2.515517 + 0.802853*w + 0.010328 * (w**2))/(1 + 1.432788 * w + 0.189269 * (w**2) + 0.001308 * (w**3))
df_probabilidad_exc['Kt Log-Normal'] = np.log(Z_log)

#Para una dsitribucion Person III
# Parámetros estimados de la distribución gamma


#Calculo el CS
media= df_probabilidad_exc["ACCESS1-0 [r1i1p1]"].mean()
desviacion_std = df_probabilidad_exc["ACCESS1-0 [r1i1p1]"].std()
mediana = df_probabilidad_exc["ACCESS1-0 [r1i1p1]"].median()
Cs= 3*(media -mediana)/desviacion_std
K= Cs/6
#Donde Z proviene de la distribucion normal
df_probabilidad_exc["Kt Pearson III"] = (Z +(Z**2-1)*K + (Z**3-6*Z)*(K**2)/3 - (Z**2-1)*K**3+Z*K**4+K**5/3)




#Para una distribucion Gumbel
#Considero n = 30 años, por lo tanto
n = 30
yn = 0.5362
sigman = 1.1124
T = 1/(df_probabilidad_exc['Probabilidad_Excedencia']/100)
yt = -np.log(-np.log((T-1)/T))


# Calcular el coeficiente Kt para la distribución Gumbel
df_probabilidad_exc['Kt Gumbel'] = (yt - yn) / sigman

df = df_probabilidad_exc


