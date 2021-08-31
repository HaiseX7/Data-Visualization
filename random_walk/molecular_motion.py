import matplotlib.pyplot as plt 

from random_walk import RandomWalk

while True:
	# Make a random walk
	rw = RandomWalk(5_000)
	rw.fill_walk()

	step_num = range(rw.num_points)

	# Plot the random walk
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15,9))
	ax.set_title('A Random Path', fontsize=24)
	ax.plot(rw.x_values, rw.y_values, linewidth=0.5)

	# Emphasize the first and last point
	ax.scatter(0, 0, c='green', edgecolors='none', s=100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
