import json 
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout

filename = 'data/all_month.geojson'
with open(filename) as f:
	all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

filename = 'data/eq_past_month_readable.json'
with open(filename, 'w') as f:
	json.dump(all_eq_data, f, indent=4)

title = all_eq_data['metadata']['title']

lats, lons, mags = [], [], []
for eq_dict in all_eq_dicts:
	lats.append(eq_dict['geometry']['coordinates'][1])
	lons.append(eq_dict['geometry']['coordinates'][0])
	if eq_dict['properties']['mag'] >= 0:
		mags.append(eq_dict['properties']['mag'])


data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'marker': {
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title': 'Magnitude'}
	}
}]
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

