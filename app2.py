# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Simulamos un dataset
data = pd.DataFrame({
    'Fecha': pd.to_datetime([
        '2024-01-05', '2024-01-06', '2024-02-12',
        '2024-03-20', '2024-04-10', '2024-04-15',
        '2024-05-01', '2024-05-05'
    ]),
    'Producto': ['Laptop A', 'Celular B', 'Impresora C', 'Monitor D', 'Teclado E', 'Laptop A', 'Silla F', 'Celular B'],
    'Categoría': ['Electrónica', 'Electrónica', 'Oficina', 'Electrónica', 'Oficina', 'Electrónica', 'Oficina', 'Electrónica'],
    'Región': ['Norte', 'Sur', 'Este', 'Oeste', 'Norte', 'Sur', 'Este', 'Norte'],
    'Vendedor': ['Laura García', 'Pedro Torres', 'Ana Ramírez', 'Juan Rodríguez', 'Laura García', 'Pedro Torres', 'Ana Ramírez', 'Juan Rodríguez'],
    'Unidades': [3, 5, 2, 4, 6, 1, 3, 4],
    'PrecioUnitario': [750, 300, 200, 180, 50, 750, 120, 300],
})

data['TotalVenta'] = data['Unidades'] * data['PrecioUnitario']

# Interfaz de usuario
st.title("📊 Dashboard de Ventas Mensuales")
st.sidebar.header("Filtros")

regiones = st.sidebar.multiselect("Selecciona Región", options=data['Región'].unique(), default=data['Región'].unique())

# Filtrado
df_filtrado = data[data['Región'].isin(regiones)]

# KPIs
total_ventas = df_filtrado['TotalVenta'].sum()
total_unidades = df_filtrado['Unidades'].sum()
ticket_promedio = total_ventas / total_unidades if total_unidades > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Ventas", f"${total_ventas:,.0f}")
col2.metric("📦 Unidades Vendidas", f"{total_unidades}")
col3.metric("🎟️ Ticket Promedio", f"${ticket_promedio:,.2f}")

# Gráfico de ventas por producto
fig = px.bar(df_filtrado, x='Producto', y='TotalVenta', color='Categoría', title='Ventas por Producto')
st.plotly_chart(fig)

# Gráfico de tendencia por fecha
fig2 = px.line(df_filtrado.sort_values('Fecha'), x='Fecha', y='TotalVenta', title='Tendencia de Ventas')
st.plotly_chart(fig2)
