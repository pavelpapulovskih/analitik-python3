import pandas as pd
# Загрузка данных
data = pd.read_csv('kc_house_data.csv')
# Расчет среднего соотношения жилой площади к общей площади
data['ratio'] = data['sqft_living'] / data['sqft_lot']
mean_ratio = data['ratio'].mean()
# Сохранение статистики
with open('living_vs_lot_analysis.txt', 'w') as f:f.write(f'Среднее соотношение жилой площади к общей площади:
{mean_ratio}\n')