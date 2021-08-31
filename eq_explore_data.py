import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
	json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
metadata = all_eq_data['metadata']
title = metadata['title']

mags, locations, hover_texts = [], [], []
for eq_dict in all_eq_dicts:
	mags.append(eq_dict['properties']['mag'])
	hover_texts.append(eq_dict['properties']['title'])

	location = eq_dict['geometry']['coordinates']
	locations.append(location)

lons, lats = [], []
for coordinate in locations:
	lons.append(coordinate[0])
	lats.append(coordinate[1])

print(lons)

data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': hover_texts,
	'marker': {
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title': 'Magnitude'}		
	},
}]
my_layout = Layout(title = title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

