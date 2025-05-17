import pandas as pd
from pathlib import Path

# Crear los datos de ejemplo
data = pd.DataFrame({
    'Sale_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Date': pd.to_datetime([
        '2024-01-05', '2024-01-06', '2024-02-12',
        '2024-03-20', '2024-04-10', '2024-04-15',
        '2024-05-01', '2024-05-05'
    ]),
    'Product': ['Laptop A', 'Cellphone B', 'Printer C', 'Monitor D', 'Keyboard E', 'Laptop A', 'Chair F', 'Cellphone B'],
    'Category': ['Electronics', 'Electronics', 'Office', 'Electronics', 'Office', 'Electronics', 'Office', 'Electronics'],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'North'],
    'Salesperson': ['Laura Garcia', 'Pedro Torres', 'Ana Ramirez', 'Juan Rodriguez', 'Laura Garcia', 'Pedro Torres', 'Ana Ramirez', 'Juan Rodriguez'],
    'Units': [3, 5, 2, 4, 6, 1, 3, 4],
    'UnitPrice': [750, 300, 200, 180, 50, 750, 120, 300]
})

# Calcular total
data['TotalSale'] = data['Units'] * data['UnitPrice']

# Guardar en Excel
output_dir = Path("SualbaDev_PowerBi")
output_dir.mkdir(exist_ok=True)
data.to_excel(output_dir / "sales_data.xlsx", index=False)

print("✅ Archivo Excel creado en: SualbaDev_PowerBi/sales_data.xlsx")
