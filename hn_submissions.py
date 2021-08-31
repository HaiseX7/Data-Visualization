from operator import itemgetter
import requests


# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
	# Make a separate API call for each submission.
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()

	response_list = list(response_dict.values())

	# Build a dictionary for each article
	submission_dict = {
		'title': response_dict['title'],
		'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
		'comments': response_list[1],
	}
	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
	print(f"\nTitle: {submission_dict['title']}")
	print(f"Discussion link: {submission_dict['hn_link']}")
	print(f"Comments: {submission_dict['comments']}")

	{
		'by': 'mkotowski', 
		'descendants': 44, 
		'id': 28264408, 
		'kids': [28264684, 28266030, 28266748, 28265001, 
			28265471, 28266931, 28265908, 28265460, 28264888, 
			28264663, 28265078, 28265735, 28265595, 28265754, 
			28266953], 
		'score': 135, 
		'time': 1629629101, 
		'title': 'WinFsp – Windows File System Proxy', 
		'type': 'story', 
		'url': 'https://github.com/billziss-gh/winfsp'
	}