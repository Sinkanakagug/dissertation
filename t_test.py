from scipy import stats
import pandas as pd

#First algorithm to compare
csv1 = 'rgb.csv'
df1 = pd.read_csv(csv1, header=None)
data1 = df1[0]
success_data1 = data1[data1 > 0]
data_1 = success_data1.values

#Second algorithm to compare
csv2 = 'ga.csv'
df2 = pd.read_csv(csv2, header=None)
data2 = df2[0]
success_data2 = data2[data2 > 0]
data_2 = success_data2.values

def t_test_ind(data1, data2):
    t_stats, p_value = stats.ttest_ind(data2, data1)

    return t_stats, p_value

print(t_test_ind(data_1, data_2))