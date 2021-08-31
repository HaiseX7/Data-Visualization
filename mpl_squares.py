import matplotlib.pyplot as plt

squares = []
input_values = []
for i in range(1, 6):
	i = i**2
	squares.append(i)
for i in range(1, 6):
	input_values.append(i)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

# Set chart title and label axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=24)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()