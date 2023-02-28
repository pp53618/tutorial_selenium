import xlrd as xlrd
import pandas as pd


wb = pd.read_excel("Dane.xlsx", engine='openpyxl')

print(wb.values)

