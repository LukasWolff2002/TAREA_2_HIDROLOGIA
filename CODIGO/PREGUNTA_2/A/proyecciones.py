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
        return b - k*n
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









#Aqui ajusto la recta
n_normal = -(eje_y[10]-eje_y[11])/(df_normal['Normal Interpolado'][10]-df_normal['Normal Interpolado'][11])
#Por lo tanto, la precipitacion a los 50 años con normal va a ser
