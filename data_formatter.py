import pandas as pd

df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')

df = pd.concat([df0, df1, df2])

pink_morsels = df[df['product'] == 'pink morsel'].copy()

pink_morsels['price'] = pink_morsels['price'].str.replace('$', '').astype(float)

pink_morsels['sales'] = pink_morsels['quantity'] * pink_morsels['price']

final_formatted_data = pink_morsels[['sales', 'date', 'region']]

final_formatted_data.to_csv('formatted_sales_data.csv', index=False)

print("Data processing complete! Check your folder for formatted_sales_data.csv")