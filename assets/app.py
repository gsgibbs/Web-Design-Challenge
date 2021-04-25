import pandas as pd

a = pd.read_csv('cities.csv')

a.to_html('cities.html')

print(a.to_html)
