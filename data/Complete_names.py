import pandas as pd
import numpy as np

# df = pd.read_csv('/Users/Franco/Desktop/Data Science/Analytics Computing/Football Assignment/Complete_names.csv', sep=';')
df = pd.read_csv('/Users/Franco/Desktop/data_science/fall_semester_2024/Analytics Computing/Football Assignment/Football Team Builder/data/Complete_names.csv', sep=';')
first_names = df['first_name']
last_names = df['last_name']

# print(str(first_names.sample(1)))

