import plotly.express as px
import requests

# make an API call and store the response 
url = 'https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000'
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
# repo_dicts = response_dict['items']
# repo_names, stars, hover_texts = [], [], []

# for repo_dict in repo_dicts:
#     repo_names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#     owner = repo_dict['owner']['login']
#     description = repo_dict['description']
#     hover_text = f"{owner}<br />{description}"
#     hover_texts.append(hover_text)

# for clickable links
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    repo_name = (repo_dict['name'])
    repo_url = repo_dict['html_url']
    repo_link = f"<a href = '{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)




# make visualization 
fig = px.bar(x=repo_links, y=stars, title='Most-Starred Python Projects on GitHub', labels={'x': 'Repository', 'y': 'Stars'}, hover_name=hover_texts)
fig.update_layout(xaxis_title='Repository', yaxis_title='Stars')
fig.update_layout(title_x=0.5)
fig.update_layout(title_font_size =24, xaxis_title_font_size =20, yaxis_title_font_size =20)
fig.update_traces(marker_color = 'rgb(60, 100, 150)', marker_opacity = 0.6)
fig.show()

# 