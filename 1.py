import pandas as pd
# Загрузка данных
data = pd.read_csv('kc_house_data.csv')
# Добавление нового признака: средняя стоимость за квадратный метр жилой площади
data['price_per_sqft_living'] = data['price'] / data['sqft_living']
# Добавление нового признака: возраст дома
current_year = pd.to_datetime('today').year
data['age_of_house'] = current_year - data['yr_built']
# Создание новых признаков: год и месяц продажи
data['year_ch'] = pd.to_datetime(data['date'],
format='%Y%m%dT000000').dt.year
data['month_ch'] = pd.to_datetime(data['date'],
format='%Y%m%dT000000').dt.month
# Удаление ненужных колонок
data_cleaned = data.drop(columns=['date', 'zipcode', 'lat', 'long'])
# Сохранение измененных данных
data_cleaned.to_csv('modified_data.csv', index=False)








