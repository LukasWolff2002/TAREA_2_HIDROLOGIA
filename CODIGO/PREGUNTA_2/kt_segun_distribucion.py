from probabilidad_exc import df_probabilidad_exc

media = df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'].mean()
desviacion_std = df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'].std()
df_probabilidad_exc['Z_score'] = (df_probabilidad_exc['MAXIMA EN 24 HS. PRECIPITACION (mm)'] - media) / desviacion_std

print(df_probabilidad_exc)