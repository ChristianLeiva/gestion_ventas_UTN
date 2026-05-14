
import pandas as pd
import matplotlib.pyplot as plt
import os

# Definimos la ruta relativa al archivo CSV
ruta_datos = 'datos/sales_sample_2024.csv'

if os.path.exists(ruta_datos):
    print("✅ Cargando datos desde ventas.csv...")
    df = pd.read_csv(ruta_datos)
    
    # Convertimos la fecha a formato datetime para que el gráfico salga ordenado
    # Ajustá 'sales_date' al nombre real de la columna en CSV
    if 'sales_date' in df.columns:
        df['sales_date'] = pd.to_datetime(df['sales_date'])
        df = df.sort_values('sales_date')
else:
    print("Error: No se encontró datos/sales_sample_2024.csv, usando datos de respaldo.")
    data = {
        'sales_date': ['2026-01-01', '2026-02-01', '2026-03-01'],
        'sales_amount': [5000, 7000, 6500]
    }
    df = pd.DataFrame(data)

# --- PROCESAMIENTO ---
total = df['sales_amount'].sum()
promedio = df['sales_amount'].mean()

print(f"Total de Ventas: ${total:,.2f}")
print(f"Promedio de Ventas: ${promedio:,.2f}")

# --- GRÁFICO ---
plt.figure(figsize=(10, 5))
plt.plot(df['sales_date'], df['sales_amount'], marker='o', linestyle='-', color='blue')
plt.title('Análisis de Ventas - Escenario B')
plt.xlabel('Fecha')
plt.ylabel('Monto')
plt.grid(True)

# Guardar resultado
plt.savefig('resultados/grafico_ventas.png')
print("✅ Resultado exportado a resultados/grafico_ventas.png")
