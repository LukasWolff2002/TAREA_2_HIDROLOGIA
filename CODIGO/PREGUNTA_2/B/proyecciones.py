from interpolacion import df_normal, df_log_normal, df_pearson, df_gumbel, eje_y
import numpy as np
from kt_segun_distribucion import K, yn, sigman
from interpolacion import pendiente_normal, pendiente_log_normal, pendiente_pearson, pendiente_gumbel
from interpolacion import intercepto_normal, intercepto_log_normal, intercepto_pearson, intercepto_gumbel

print(f'{pendiente_normal=}')
print(f'{pendiente_log_normal=}')
print(f'{pendiente_pearson=}')
print(f'{pendiente_gumbel=}')
print('')
print(f'{intercepto_normal=}')
print(f'{intercepto_log_normal=}')
print(f'{intercepto_pearson=}')
print(f'{intercepto_gumbel=}')
print('')
#Nesecito hacer la proyeccion para T = 10, 50, 100 y 200
#para 10 lo obtengo rapido

def Kt_normal (T):
    #priero calculo el valor de la probabilidad de excedencia
    P_exc = 1/T
    print('-------------')
    print(f'{P_exc=}')
    #Con esta probabilidad de excedencia tengo que calcular el valor Kt
    #Ahusto el valor de P_exc_50
    P_exc = 1 - P_exc if P_exc < 0.5 else P_exc
    #Calculo w
    print(f'{P_exc=}')
    print('-------------')
    w = (np.log(1/(P_exc)))**0.5
    #Ahora calculo el valor de z
    Z = -w + (2.515517 + 0.802853*w + 0.010328 * (w**2))/(1 + 1.432788 * w + 0.189269 * (w**2) + 0.001308 * (w**3))
    #Por lo tanto, el valor de Kt para T = 50 es
    return Z

def Kt_log_normal (T):
    #priero calculo el valor de la probabilidad de excedencia
    P_exc = 1/T
    #Con esta probabilidad de excedencia tengo que calcular el valor Kt
    #Ahusto el valor de P_exc_50
    P_exc = 1 - P_exc if P_exc < 0.5 else P_exc
    #Calculo w
    w = (np.log(1/(P_exc)))**0.5
    w = np.log(w)
    #Ahora calculo el valor de z
    Z = -w + (2.515517 + 0.802853*w + 0.010328 * (w**2))/(1 + 1.432788 * w + 0.189269 * (w**2) + 0.001308 * (w**3))
    #Por lo tanto, el valor de Kt para T = 50 es
    return Z

def Kt_Pearson_III (T):
    Z = Kt_normal(T)
    return (Z +(Z**2-1)*K + (Z**3-6*Z)*(K**2)/3 - (Z**2-1)*K**3+Z*K**4+K**5/3)

def Kt_gumbel (T):
    yt = -np.log(-np.log((T-1)/T))
    return (yt - yn) / sigman

#Para T = 10
Kt_10_Normal = Kt_normal(10)
Kt_10_Log_Normal = Kt_log_normal(10)
Kt_10_Pearson = Kt_Pearson_III(10)
Kt_10_gumbel = Kt_gumbel(10)

print(f'{Kt_10_Normal=}')
print(f'{Kt_10_Log_Normal=}')
print(f'{Kt_10_Pearson=}')
print(f'{Kt_10_gumbel=}')
print('')


#Para T = 50
Kt_50_Normal = Kt_normal(50)
Kt_50_Log_Normal = Kt_log_normal(50)
Kt_50_Pearson = Kt_Pearson_III(50)
Kt_50_gumbel = Kt_gumbel(50)

print(f'{Kt_50_Normal=}')
print(f'{Kt_50_Log_Normal=}')
print(f'{Kt_50_Pearson=}')
print(f'{Kt_50_gumbel=}')
print('')

#Para T = 100
Kt_100_Normal = Kt_normal(100)
Kt_100_Log_Normal = Kt_log_normal(100)
Kt_100_Pearson = Kt_Pearson_III(100)
Kt_100_gumbel = Kt_gumbel(100)

print(f'{Kt_100_Normal=}')
print(f'{Kt_100_Log_Normal=}')
print(f'{Kt_100_Pearson=}')
print(f'{Kt_100_gumbel=}')
print('')


#Para T = 200
Kt_200_Normal = Kt_normal(200)
Kt_200_Log_Normal = Kt_log_normal(200)
Kt_200_Pearson = Kt_Pearson_III(200)
Kt_200_gumbel = Kt_gumbel(200)

print(f'{Kt_200_Normal=}')
print(f'{Kt_200_Log_Normal=}')
print(f'{Kt_200_Pearson=}')
print(f'{Kt_200_gumbel=}')
print('')

#Por lo tanto, ahora calculo las precipitaciones

def precipitacion (k,n,b):
    if k < 0:
        return b + k*n
    else:
        return b +k*n

#para los periodos de 10 años
precipitacion_normal_10 = precipitacion(Kt_10_Normal,pendiente_normal,intercepto_normal)
precipitacion_log_normal_10 = precipitacion(Kt_10_Log_Normal,pendiente_log_normal,intercepto_log_normal)
precipitacion_pearson_10 = precipitacion(Kt_10_Pearson,pendiente_pearson,intercepto_pearson)
precipitacion_gumbel_10 = precipitacion(Kt_10_gumbel,pendiente_gumbel,intercepto_gumbel)

print(f'{precipitacion_normal_10=}')
print(f'{precipitacion_log_normal_10=}')
print(f'{precipitacion_pearson_10=}')
print(f'{precipitacion_gumbel_10=}')
print('')

#para los periodos de 50 años
precipitacion_normal_50 = precipitacion(Kt_50_Normal,pendiente_normal,intercepto_normal)
precipitacion_log_normal_50 = precipitacion(Kt_50_Log_Normal,pendiente_log_normal,intercepto_log_normal)
precipitacion_pearson_50 = precipitacion(Kt_50_Pearson,pendiente_pearson,intercepto_pearson)
precipitacion_gumbel_50 = precipitacion(Kt_50_gumbel,pendiente_gumbel,intercepto_gumbel)

print(f'{precipitacion_normal_50=}')
print(f'{precipitacion_log_normal_50=}')
print(f'{precipitacion_pearson_50=}')
print(f'{precipitacion_gumbel_50=}')
print('')

#para los periodos de 100 años
precipitacion_normal_100 = precipitacion(Kt_100_Normal,pendiente_normal,intercepto_normal)
precipitacion_log_normal_100 = precipitacion(Kt_100_Log_Normal,pendiente_log_normal,intercepto_log_normal)
precipitacion_pearson_100 = precipitacion(Kt_100_Pearson,pendiente_pearson,intercepto_pearson)
precipitacion_gumbel_100 = precipitacion(Kt_100_gumbel,pendiente_gumbel,intercepto_gumbel)

print(f'{precipitacion_normal_100=}')
print(f'{precipitacion_log_normal_100=}')
print(f'{precipitacion_pearson_100=}')
print(f'{precipitacion_gumbel_100=}')
print('')

#para los periodos de 200 años
precipitacion_normal_200 = precipitacion(Kt_200_Normal,pendiente_normal,intercepto_normal)
precipitacion_log_normal_200 = precipitacion(Kt_200_Log_Normal,pendiente_log_normal,intercepto_log_normal)
precipitacion_pearson_200 = precipitacion(Kt_200_Pearson,pendiente_pearson,intercepto_pearson)
precipitacion_gumbel_200 = precipitacion(Kt_200_gumbel,pendiente_gumbel,intercepto_gumbel)

print(f'{precipitacion_normal_200=}')
print(f'{precipitacion_log_normal_200=}')
print(f'{precipitacion_pearson_200=}')
print(f'{precipitacion_gumbel_200=}')
print('')

#Grafiquemos las proyecciones
import matplotlib.pyplot as plt

plt.figure(figsize=(19.2, 10.8))  # Tamaño en pulgadas que corresponde a 1920x1080 píxeles
plt.rcParams.update({'font.size': 16})  # Ajusta el tamaño base de la fuente
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.09)

def graficar_columnas(df, columna_x, columna_y, color):
    plt.plot(df[columna_y], df[columna_x], linestyle='-', color=color)

def agregar_punto(x, y, tamaño, color, etiqueta=None):

    plt.scatter(x, y, s=tamaño, c=color, label=etiqueta)

    
#Ahora grafico
graficar_columnas(df_normal, 'ACCESS1-0 [r1i1p1]', 'Normal Interpolado', 'red')
graficar_columnas(df_log_normal, 'ACCESS1-0 [r1i1p1]', 'Log-Normal Interpolado', 'green')
graficar_columnas(df_pearson, 'ACCESS1-0 [r1i1p1]', 'Pearson III Interpolado', 'blue')
graficar_columnas(df_gumbel, 'ACCESS1-0 [r1i1p1]', 'Gumbel Interpolado', 'black')

#Agrego los puntos de las proyecciones
agregar_punto(Kt_10_Normal,precipitacion_normal_10, 100, 'red', 'Normal 10 años')
agregar_punto(Kt_10_Log_Normal,precipitacion_log_normal_10, 100, 'green', 'Log-Normal 10 años')
agregar_punto(Kt_10_Pearson,precipitacion_pearson_10, 100, 'blue', 'Pearson III 10 años')
agregar_punto(Kt_10_gumbel,precipitacion_gumbel_10, 100, 'black', 'Gumbel 10 años')

agregar_punto(Kt_50_Normal,precipitacion_normal_50, 200, 'red', 'Normal 50 años')
agregar_punto(Kt_50_Log_Normal,precipitacion_log_normal_50, 200, 'green', 'Log-Normal 50 años')
agregar_punto(Kt_50_Pearson,precipitacion_pearson_50, 200, 'blue', 'Pearson III 50 años')
agregar_punto(Kt_50_gumbel,precipitacion_gumbel_50, 200, 'black', 'Gumbel 50 años')

agregar_punto(Kt_100_Normal,precipitacion_normal_100, 300, 'red', 'Normal 100 años')
agregar_punto(Kt_100_Log_Normal,precipitacion_log_normal_100, 300, 'green', 'Log-Normal 100 años')
agregar_punto(Kt_100_Pearson,precipitacion_pearson_100, 300, 'blue', 'Pearson III 100 años')
agregar_punto(Kt_100_gumbel,precipitacion_gumbel_100, 300, 'black', 'Gumbel 100 años')

agregar_punto(Kt_200_Normal,precipitacion_normal_200, 400, 'red', 'Normal 200 años')
agregar_punto(Kt_200_Log_Normal,precipitacion_log_normal_200, 400, 'green', 'Log-Normal 200 años')
agregar_punto(Kt_200_Pearson,precipitacion_pearson_200, 400, 'blue', 'Pearson III 200 años')
agregar_punto(Kt_200_gumbel,precipitacion_gumbel_200, 400, 'black', 'Gumbel 200 años')


#Finalmente guardo el grafico como una imagen JPG con la resolución deseada
# Título del gráfico 
plt.title(f'Gráfico de',fontsize=25)
plt.legend(['Normal Interpolada', 'Log-Normal Interpolada', 'Pearson III Interpolada', 'Gumbel Interpolada'], fontsize=18)

# Etiquetas de los ejes
plt.ylabel("Precipitacion", fontsize=18)
plt.xlabel("Frecuencia segun distribucion", fontsize=18)

# Guardar el gráfico como una imagen JPG con la resolución deseada
plt.savefig('grafico_b_proyecciones.jpg', format='jpg', dpi=100)

# Cerrar la figura para liberar memoria
plt.close()



