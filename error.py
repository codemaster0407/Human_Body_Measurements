import pandas as pd

from sklearn.metrics import mean_absolute_error 

data = pd.read_excel('measurements_file_updated.xlsx')
# print(data)

mse_error_chest = mean_absolute_error(data['Chest'], data['Predicted chest'])
mse_error_waist = mean_absolute_error(data['Waist'], data['Predicted waist'])
mse_error_shoulder = mean_absolute_error(data['Shoulder'], data['Predicted Shoulder'])

print(f'Mean absolute error of chest is {mse_error_chest}')

print(f'Mean absolute error of waist is {mse_error_waist}')

print(f'Mean absolute error of shoulder is {mse_error_shoulder}')