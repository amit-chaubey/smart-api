import plotly.express as px
import requests


def fetch_github_repos(language="python", min_stars=10000):
    """
    Fetch the most-starred GitHub repositories for a given language.
    Args:
        language (str): Programming language to filter by.
        min_stars (int): Minimum number of stars for repositories.
    Returns:
        list: List of repository dictionaries.
    """
    url = f"https://api.github.com/search/repositories?q=language:{language}+sort:stars+stars:>{min_stars}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"GitHub API error: {response.status_code}")
        return []
    data = response.json()
    return data.get('items', [])


def prepare_plot_data(repo_dicts):
    """
    Prepare data for Plotly visualization.
    Args:
        repo_dicts (list): List of repository dictionaries.
    Returns:
        tuple: (repo_links, stars, hover_texts)
    """
    repo_links, stars, hover_texts = [], [], []
    for repo in repo_dicts:
        repo_name = repo.get('name', 'N/A')
        repo_url = repo.get('html_url', '#')
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo.get('stargazers_count', 0))
        owner = repo.get('owner', {}).get('login', 'unknown')
        description = repo.get('description', 'No description')
        hover_text = f"{owner}<br />{description}"
        hover_texts.append(hover_text)
    return repo_links, stars, hover_texts


def plot_github_repos(repo_links, stars, hover_texts):
    """
    Create and show a bar chart of GitHub repositories using Plotly.
    """
    fig = px.bar(
        x=repo_links,
        y=stars,
        title='Most-Starred Python Projects on GitHub',
        labels={'x': 'Repository', 'y': 'Stars'},
        hover_name=hover_texts
    )
    fig.update_layout(xaxis_title='Repository', yaxis_title='Stars')
    fig.update_layout(title_x=0.5)
    fig.update_layout(title_font_size=24, xaxis_title_font_size=20, yaxis_title_font_size=20)
    fig.update_traces(marker_color='rgb(60, 100, 150)', marker_opacity=0.6)
    fig.show()


def main():
    """
    Main function to fetch data and plot the chart.
    """
    print("Fetching top Python repositories from GitHub...")
    repos = fetch_github_repos()
    if not repos:
        print("No repositories found or API error.")
        return
    print(f"Fetched {len(repos)} repositories. Preparing visualization...")
    repo_links, stars, hover_texts = prepare_plot_data(repos)
    plot_github_repos(repo_links, stars, hover_texts)


if __name__ == "__main__":
    main()



# # make an API call and store the response 
# url = 'https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000'
# headers = {
#     "Accept": "application/vnd.github.v3+json"
# }
#
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")
#
# # store API response in a variable 
# response_dict = r.json()
#
# # process results 
# print(response_dict.keys())
#
# # process repo information 
# # repo_dicts = response_dict['items']
# # repo_names, stars, hover_texts = [], [], []
#
# # for repo_dict in repo_dicts:
# #     repo_names.append(repo_dict['name'])
# #     stars.append(repo_dict['stargazers_count'])
# #     owner = repo_dict['owner']['login']
# #     description = repo_dict['description']
# #     hover_text = f"{owner}<br />{description}"
# #     hover_texts.append(hover_text)
#
# # for clickable links
# repo_dicts = response_dict['items']
# repo_links, stars, hover_texts = [], [], []
#
# for repo_dict in repo_dicts:
#     repo_name = (repo_dict['name'])
#     repo_url = repo_dict['html_url']
#     repo_link = f"<a href = '{repo_url}'>{repo_name}</a>"
#     repo_links.append(repo_link)
#     stars.append(repo_dict['stargazers_count'])
#     owner = repo_dict['owner']['login']
#     description = repo_dict['description']
#     hover_text = f"{owner}<br />{description}"
#     hover_texts.append(hover_text)
#
# # make visualization 
# fig = px.bar(x=repo_links, y=stars, title='Most-Starred Python Projects on GitHub', labels={'x': 'Repository', 'y': 'Stars'}, hover_name=hover_texts)
# fig.update_layout(xaxis_title='Repository', yaxis_title='Stars')
# fig.update_layout(title_x=0.5)
# fig.update_layout(title_font_size =24, xaxis_title_font_size =20, yaxis_title_font_size =20)
# fig.update_traces(marker_color = 'rgb(60, 100, 150)', marker_opacity = 0.6)
# fig.show()
