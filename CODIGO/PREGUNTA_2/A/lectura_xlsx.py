import pandas as pd

def leer_hoja_excel(archivo):

    try:
        # Leer la hoja especificada del archivo Excel
        df = pd.read_excel(archivo, engine='openpyxl')
        return df
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

# Ejemplo de uso
archivo = 'DATOS/precipitaciones.xlsx'

df_precipitaciones = leer_hoja_excel(archivo)

