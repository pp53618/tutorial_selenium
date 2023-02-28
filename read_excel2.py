import pandas as pd

df = pd.read_excel(
    'Dane.xlsx',
    engine='openpyxl'
)

print(df)