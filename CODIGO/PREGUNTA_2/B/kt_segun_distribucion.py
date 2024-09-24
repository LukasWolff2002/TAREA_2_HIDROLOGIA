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
df_probabilidad_exc['Log de Precipitación'] = np.log(df_probabilidad_exc['ACCESS1-0 [r1i1p1]'])
media_log = df_probabilidad_exc['Log de Precipitación'].mean()
desviacion_std_log = df_probabilidad_exc['Log de Precipitación'].std()
df_probabilidad_exc['Kt Log-Normal'] = (df_probabilidad_exc['Log de Precipitación'] - media_log) / desviacion_std_log
df_probabilidad_exc.drop('Log de Precipitación', axis=1, inplace=True)

#Para una dsitribucion Person III
# Parámetros estimados de la distribución gamma

df_probabilidad_exc['W Pearson'] = (np.log(1/(df_probabilidad_exc['ACCESS1-0 [r1i1p1]'])**2))**0.5
W=np.log(df_probabilidad_exc['ACCESS1-0 [r1i1p1]'])
df_probabilidad_exc["Z Pearson"] = W - (2.516 +0.803*W+0.0103*W**2)/(1+1.432*W+0.189*W**2+0.001308*W**3)
Z= df_probabilidad_exc["Z Pearson"]
media= df_probabilidad_exc["ACCESS1-0 [r1i1p1]"].mean()
desviacion_std = df_probabilidad_exc["ACCESS1-0 [r1i1p1]"].std()
mediana = df_probabilidad_exc["ACCESS1-0 [r1i1p1]"].median()
Cs= 3*(media -mediana)/desviacion_std
K= Cs/6
df_probabilidad_exc["Kt Pearson III"] = (Z +(Z**2-1)*K + (Z**3-6*Z)*(K**2)/3 - (Z**2-1)*K**3+Z*K**4+K**5/3)




#Para una distribucion Gumbel
mu = np.mean(df_probabilidad_exc['ACCESS1-0 [r1i1p1]'])  # Esto es una simplificación
beta = np.std(df_probabilidad_exc['ACCESS1-0 [r1i1p1]'], ddof=1) * np.sqrt(6) / np.pi

#Considero n = 30 años, por lo tanto
n = 30
yn = 0.5362
sigman = 1.1124
T = 1/(df_probabilidad_exc['Probabilidad_Excedencia']/100)
yt = -np.log(-np.log((T-1)/T))
# Calcular el coeficiente Kt para la distribución Gumbel
df_probabilidad_exc['Kt Gumbel'] = (yt - yn) / sigman

df = df_probabilidad_exc


