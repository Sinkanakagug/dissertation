import pandas as pd

ALGORITHM_NAME = 'rgb_mod'
FILE_EXT = '.csv'

#Get the column with the data
df = pd.read_csv(ALGORITHM_NAME + FILE_EXT, header=None)
data = df[0]

#Filter to only the values that are greater than 0 (the algorithm was successful in finding a solution)
success_data = data[data > 0]
success_values = success_data.values
success_rate = (len(success_data) / len(data)) * 100
average_evaluations = success_data.mean()
max_value = success_data.max()
min_value = success_data.min()
std_dev = success_data.std()
variance = success_data.var()

print(f'The algorithm had a success rate of {success_rate}% and found a good solution, on average, in {average_evaluations} evaluations. The range of evaluations was between {min_value} and {max_value}. Standard deviation was {std_dev}. Variance was {variance}.')