import numpy as np

# Constantes
R = 287  # Constante de los gases en J/(mol·K)
g = 9.81  # Aceleración gravitacional en m/s²
L = 2.5e6  # Calor latente de vaporización en J/kg
eps = 0.622  # Relación de masas moleculares de vapor de agua y aire seco

# Parámetros dados
P0 = 98000  # Presión en Pa (980 mb convertidos a Pa)
T0 = 12   # Temperatura inicial en C
grad_T = -6.5 / 1000  # Gradiente de temperatura en K/m
z0 = 500  # Altitud inicial en m
z_top = 10500  # Altitud final de la columna en m



# Función para calcular la temperatura a una altitud z
def temperatura(z):
    return T0 + grad_T * (z - z0)

# Función para calcular la presión a una altitud z
def presion(z):
    Tz = temperatura(z)
    H = R * Tz / (g*grad_T)
    return P0 * np.exp(-(z - z0) / H)

# Función para calcular la presión de saturación de vapor de agua (Clausius-Clapeyron)
def presion_saturacion_vapor(T):
    return 611 * np.exp((17.27*T0)/(T0 + 237.3))

# Función para calcular el contenido de agua precipitable (w) en un intervalo de altitud
def agua_precipitable(z, dz):
    Tz = temperatura(z)
    Pz = presion(z)
    es = presion_saturacion_vapor(Tz)
    r = eps * es / (Pz - es)
    return r * dz

# Cálculo del APP integrando sobre la columna de 10 km
dz = 100  # Intervalo de altura en metros
z_vals = np.arange(z0, z_top, dz)
agua_total = sum(agua_precipitable(z, dz) for z in z_vals)
agua_total = agua_total * 1000  # Convertir a kg/m² (equivale a mm)
print("pregunta 1.a")
print("")
print(f"Agua precipitable total (histórica): {agua_total:.2f} mm")
print("")

# Aumento de temperatura de 2°C
T0_new = T0 + 2

# Función modificada para la nueva temperatura
def temperatura_nueva(z):
    return T0_new + grad_T * (z - z0)

# Función modificada para la nueva presión a una altitud z
def presion_nueva(z):
    Tz = temperatura_nueva(z)
    H = R * Tz / (g*grad_T)
    return P0 * np.exp(-(z - z0) / H)

# Función modificada para calcular el contenido de agua precipitable en un intervalo de altitud
def agua_precipitable_nueva(z, dz):
    Tz = temperatura_nueva(z)
    Pz = presion_nueva(z)
    es = presion_saturacion_vapor(Tz)
    r = eps * es / (Pz - es)
    return r * dz

# Cálculo del APP con la nueva temperatura
agua_total_nueva = sum(agua_precipitable_nueva(z, dz) for z in z_vals)
agua_total_nueva = agua_total_nueva * 1000  # Convertir a kg/m² (equivale a mm)

print(f"Agua precipitable total (futura): {agua_total_nueva:.2f} mm")

# Cambio porcentual
cambio_porcentual = (agua_total_nueva - agua_total) / agua_total * 100
print("pregunta 1.b")
print(f"Cambio porcentual: {cambio_porcentual:.2f}%")
