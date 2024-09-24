from probabilidad_exc import df_probabilidad_exc
import numpy as np

#Para distribucion Normal
media = df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'].mean()
desviacion_std = df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'].std()
df_probabilidad_exc['Kt Normal'] = (df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'] - media) / desviacion_std

#para distribucion Log-Normal
df_probabilidad_exc['Log de Precipitación'] = np.log(df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'])
media_log = df_probabilidad_exc['Log de Precipitación'].mean()
desviacion_std_log = df_probabilidad_exc['Log de Precipitación'].std()
df_probabilidad_exc['Kt Log-Normal'] = (df_probabilidad_exc['Log de Precipitación'] - media_log) / desviacion_std_log
df_probabilidad_exc.drop('Log de Precipitación', axis=1, inplace=True)

#Para una dsitribucion Person III
# Parámetros estimados de la distribución gamma

df_probabilidad_exc['W Pearson'] = (np.log(1/(df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'])**2))**0.5
W=df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)']
df_probabilidad_exc["Z Pearson"] = W - (2.516 +0.803*W+0.0103*W**2)/(1+1.432*W+0.189*W**2+0.001308*W**3)
Z= df_probabilidad_exc["Z Pearson"]
media= df_probabilidad_exc["MAXIMA EN 24 HS. PRECIPITACION (mm)"].mean()
desviacion_std = df_probabilidad_exc["MAXIMA EN 24 HS. PRECIPITACION (mm)"].std()
mediana = df_probabilidad_exc["MAXIMA EN 24 HS. PRECIPITACION (mm)"].median()
Cs= 3*(media -mediana)/desviacion_std
K= Cs/6
df_probabilidad_exc["Kt Pearson"] = Z +(Z**2-1)*K + (Z**3-6*Z)*(K**2)/3 - (Z**2-1)*K**3+Z*K**4+K**5/3
print(df_probabilidad_exc["Kt Pearson"])



#Para una distribucion Gumbel
mu = np.mean(df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'])  # Esto es una simplificación
beta = np.std(df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'], ddof=1) * np.sqrt(6) / np.pi
# Constante de Euler-Mascheroni
gamma = 0.57721566490153286060
# Calcular la media y la desviación estándar de la distribución de Gumbel
media_gumbel = mu + gamma * beta
desviacion_std_gumbel = np.pi * beta / np.sqrt(6)
# Calcular el coeficiente Kt para la distribución Gumbel
df_probabilidad_exc['Kt Gumbel'] = (df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'] - media_gumbel) / desviacion_std_gumbel

df = df_probabilidad_exc