import requests
from plotly.graph_objs import Bar
from plotly import offline


# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()
print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")

repo_names, stars = [], []

# Process results.
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
	stars.append(repo_dict['stargazers_count'])
	repo_links.append(f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}</a>")
	labels.append(f"{repo_dict['owner']['login']}<br />{repo_dict['description']}")

data = [{
	'type': 'bar',
	'x': repo_links,
	'y': stars,
	'hovertext': labels,
	'marker': {
		'color': 'rgb(60, 100, 150)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
	},
	'opacity': 0.6
}]

my_layout = {
	'title': 'Most-Starred Python Projects on Github',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Repository',
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
offline.plot(fig, filename='python_repos.html')
