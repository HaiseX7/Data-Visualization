import matplotlib.pyplot as plt 
import plotly.express as px

from random_walk import RandomWalk


class RandomWalkVisual:

	def __init__(self, num_steps):
		self.rw = RandomWalk(num_steps)
		self.rw.fill_walk()
		self.num_steps = num_steps

	def make_matplotlib(self):
		while True:
			# Plot the random walk
			plt.style.use('classic')
			fig, ax = plt.subplots(figsize=(15,9))
			ax.set_title('A Random Walk', fontsize=24)
			sc = ax.scatter(self.rw.x_values, self.rw.y_values, c=self.num_steps, cmap=plt.cm.Blues, edgecolors='none', s=1.0)
			cbar = plt.colorbar(sc)
			cbar.set_label('# Of Steps', loc='center', labelpad = 20, rotation=270)

			# Emphasize the first and last point
			ax.scatter(0, 0, c='green', edgecolors='none', s=100)
			ax.scatter(self.rw.x_values[-1], self.rw.y_values[-1], c='red', edgecolors='none', s=100)

			# Remove the axes
			ax.get_xaxis().set_visible(False)
			ax.get_yaxis().set_visible(False)

			plt.show()

			keep_running = input("Make another walk? (y/n): ")
			if keep_running == 'n':
				break

	def make_plotly(self):
		fig = px.scatter(self.rw.x_values, self.rw.y_values)
		fig.update_traces(marker=dict(size=0.5))
		fig.show()


rwv = RandomWalkVisual(100_000)
rwv.make_plotly()


	