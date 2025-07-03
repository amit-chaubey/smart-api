import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:sql+sort:stars'
headers = {
    "Accept": "application/vnd.github.v3+json"
}

def main():
    r = requests.get(url, headers=headers)
    print(f"Status Code: {r.status_code}")
    if r.status_code != 200:
        print("Failed to fetch data from GitHub API.")
        return

    # Store API response in a variable
    response_dict = r.json()

    # Process results
    print(response_dict.keys())
    print(f"Total Repositories: {response_dict.get('total_count', 0)}")

    # Explore information about the repositories
    repo_dicts = response_dict.get('items', [])
    print(f"Repositories returned: {len(repo_dicts)}")

    if not repo_dicts:
        print("No repositories found.")
        return

    # Examine the first repository
    repo_dict = repo_dicts[0]
    print(f"\nKeys: {len(repo_dict)}")
    for key in sorted(repo_dict.keys()):
        print(key)

    # Explore the first repository
    print(f"\nSelected information about first repo:")
    print(f"Name: {repo_dict.get('name')}")
    print(f"Owner: {repo_dict.get('owner', {}).get('login')}")
    print(f"Stars: {repo_dict.get('stargazers_count')}")
    print(f"Repository: {repo_dict.get('html_url')}")
    print(f"Created: {repo_dict.get('created_at')}")
    print(f"Updated: {repo_dict.get('updated_at')}")
    print(f"Description: {repo_dict.get('description')}")

    # Summarize the top repositories
    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        print(f"\nName: {repo_dict.get('name')}")
        print(f"Owner: {repo_dict.get('owner', {}).get('login')}")
        print(f"Repo: {repo_dict.get('html_url')}")
        print(f"Description: {repo_dict.get('description')}")

if __name__ == "__main__":
    main()