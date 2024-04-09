import pandas as pd

from pandas import DataFrame

from contrato_de_dados import InventarioSchema

minha_tabela: DataFrame = pd.read_excel("data\inventario_mundo.xlsx")

print(minha_tabela)

try:
    InventarioSchema.validate(minha_tabela)
    print("Excel esta bom!")
except Exception as e:
    print(f"Teve erro de schema: {e}")