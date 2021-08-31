import requests
from plotly.graph_objs import Bar
from plotly import offline

languages = ['c', 'javascript', 'go', 'java', 'perl', 'python', 'haskell']

language_dicts = []
stars = []
languages_xval = []
labels = []

for i in range(len(languages)):
	url = 'https://api.github.com/search/repositories?q=language:{}&sort=stars'.format(languages[i])
	r = requests.get(url)
	json = r.json()
	language_items = json['items']
	for project in language_items:
		labels.append(f"Owner: {project['owner']['login']}<br /> Description: {project['description']}")
		languages_xval.append(languages[i])
		stars.append(project['stargazers_count'])

data = [{
	'type': 'bar',
	'x': languages_xval,
	'y': stars,
	'hovertext': labels,
	'marker': {
		'color': 'rgb(40, 60, 150)',
	},
}]

my_layout = {
	'title': 'Most Starred Languages on Github (Top 30 Projects)',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Language',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Stars',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='other_languages.html')







	
