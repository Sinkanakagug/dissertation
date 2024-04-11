import matplotlib.pyplot as plt

x_data = ['RGB', 'PSO', 'GA', 'SA']
y_data = [88, 35, 15, 3]

plt.bar(x_data, y_data)

plt.xlabel('Algorithm')
plt.ylabel('Success rate (%)')

plt.show()