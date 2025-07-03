import plotly.express as px
import requests

# make an API call and store the response 
url = 'https://api.github.com/search/repositories?q=language:python+sort:stars:10000'
headers = {
    "Accept": "application/vnd.github.v3+json"
}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# store API response in a variable 
response_dict = r.json()

# process results 
print(response_dict.keys())

# process repo information 
repo_dicts = response_dict['items']
repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# make visualization 
fig = px.bar(x=repo_names, y=stars, title='Most-Starred Python Projects on GitHub')
fig.update_layout(xaxis_title='Repository', yaxis_title='Stars')
fig.update_layout(title_x=0.5)
fig.show()
