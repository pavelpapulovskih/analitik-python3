import pandas as pd
# Загрузка данных
data = pd.read_csv('kc_house_data.csv')
# Фильтрация данных
filtered_homes = data[(data['waterfront'] == 1) &
(data['price'] > 500000) &
(data['sqft_living'] > 2000)]
# Сохранение данных
filtered_homes.to_csv('high_value_waterfront_homes.csv',
index=False)