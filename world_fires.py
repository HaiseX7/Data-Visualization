import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline 

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

	lats, lons, brightnesses = [], [], []
	for row in reader:
		brightnesses.append(float(row[2]))
		lats.append(float(row[0]))
		lons.append(float(row[1]))

data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'marker': {
		'size': [(brightness/50) for brightness in brightnesses],
		'color': brightnesses,
		'colorscale': 'hot',
	}
}]

my_layout = Layout(title = 'Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'world_fires_7_day.html')