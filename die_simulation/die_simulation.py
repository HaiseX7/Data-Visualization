from plotly.graph_objs import Bar, Layout
from plotly import offline

import matplotlib.pyplot as plt

from die import Die

class TwoDieSimulation:

	def __init__(self, die1_numsides, die2_numsides, num_rolls):
		# Create the die
		self.die1 = Die(die1_numsides)
		self.die2 = Die(die2_numsides)

		# Max result for the two die
		self.max_result = self.die1.num_sides + self.die2.num_sides
		self.num_rolls = num_rolls

		# Make some rolls, and store the results in a list
		self.results = [self.die1.roll() + self.die2.roll() for x in range(self.num_rolls)]
		self.frequencies = [self.results.count(x)/self.num_rolls for x in range(2, self.max_result+1)]

		self.die1_num = die1_numsides
		self.die2_num = die2_numsides

		self.x_values = list(range(2, self.max_result + 1))

	def make_plotly(self):
		# Visualize the results
		data = [Bar(x=self.x_values, y=self.frequencies)]

		# Config the plot
		x_axis_config = {'title': 'Result', 'dtick': 1}
		y_axis_config = {'title': 'Frequency of Result'}
		my_layout = Layout(title=
			f"Results of rolling D{self.die1_num} and D{self.die2_num} {self.num_rolls} times",
			xaxis=x_axis_config, yaxis=y_axis_config)

		# Plot the data
		offline.plot({'data': data, 'layout':my_layout}, 
			filename = f"d{self.die1_num}_d{self.die2_num}.html")

	def make_matplotlib(self):
		# Make the figure
		fig, ax = plt.subplots()
		ax.bar(self.x_values, self.frequencies)
		ax.set_title(f"Results of rolling D{self.die1_num} and D{self.die2_num} {self.num_rolls} times")
		ax.set_xlabel('Result')
		ax.set_ylabel('Frequencies')
		plt.show()

class ThreeDieSimulation:

	def __init__(self, die1_numsides, die2_numsides, die3_numsides, num_rolls):
		# Create the die
		self.die1 = Die(die1_numsides)
		self.die2 = Die(die2_numsides)
		self.die3 = Die(die3_numsides)

		# Max result for the two die
		self.max_result = self.die1.num_sides + self.die2.num_sides + self.die3.num_sides
		self.num_rolls = num_rolls

		# Make some rolls, and store the results in a list
		self.results = [self.die1.roll() + self.die2.roll() + self.die3.roll() for x in range(self.num_rolls)]
		self.frequencies = [self.results.count(x)/self.num_rolls for x in range(3, self.max_result+1)]

		self.die1_num = die1_numsides
		self.die2_num = die2_numsides
		self.die3_num = die3_numsides

		self.x_values = list(range(3, self.max_result + 1))

	def make_plotly(self):
		# Visualize the results
		data = [Bar(x=self.x_values, y=self.frequencies)]
		x_axis_config = {'title': 'Result', 'dtick': 1}
		y_axis_config = {'title': 'Frequency of Result'}
		my_layout = Layout(title=f"Results of rolling D{self.die1_num} and D{self.die2_num} and D{self.die3_num} {self.num_rolls} times", 
			xaxis=x_axis_config, yaxis=y_axis_config)
		offline.plot({'data': data, 'layout':my_layout}, filename = f"d{self.die1_num}_d{self.die2_num}_{self.die3_num}.html")

	def make_matplotlib(self):
		# Make the figure
		fig, ax = plt.subplots()
		ax.bar(self.x_values, self.frequencies)
		ax.set_title(f"Results of rolling D{self.die1_num} and D{self.die2_num} and D{self.die3_num} {self.num_rolls} times")
		ax.set_xlabel('Result')
		ax.set_ylabel('Frequencies')
		plt.show()


class TwoDieProductSimulation:

	def __init__(self, die1_numsides, die2_numsides, num_rolls):
	# Create the die
		self.die1 = Die(die1_numsides)
		self.die2 = Die(die2_numsides)

		# Max result for the two die
		self.max_result = self.die1.num_sides * self.die2.num_sides
		self.num_rolls = num_rolls
		
		# Make some rolls, and store the results in a list
		self.results = [self.die1.roll() * self.die2.roll() for x in range(self.num_rolls)]
		self.frequencies = [self.results.count(x)/self.num_rolls for x in range(2, self.max_result+1)]

		self.die1_num = die1_numsides
		self.die2_num = die2_numsides

		self.x_values = list(range(2, self.max_result + 1))

	def make_plotly(self):
		# Visualize the results
		data = [Bar(x=self.x_values, y=self.frequencies)]

		# Config the plot
		x_axis_config = {'title': 'Result', 'dtick': 1}
		y_axis_config = {'title': 'Frequency of Result'}
		my_layout = Layout(title=
			f"Results of rolling D{self.die1_num} and D{self.die2_num} {self.num_rolls} times",
			xaxis=x_axis_config, yaxis=y_axis_config)

		# Plot the data
		offline.plot({'data': data, 'layout':my_layout}, 
			filename = f"d{self.die1_num}_d{self.die2_num}.html")

	def make_matplotlib(self):
		# Make the figure
		fig, ax = plt.subplots()
		ax.bar(self.x_values, self.frequencies)
		ax.set_title(f"Products rolling D{self.die1_num} and D{self.die2_num} {self.num_rolls} times")
		ax.set_xlabel('Product')
		ax.set_ylabel('Frequencies')
		plt.show()

