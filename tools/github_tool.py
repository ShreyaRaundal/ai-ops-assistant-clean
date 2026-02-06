import requests


def search_repos(query: str):
    """
    Search top GitHub repositories by query.
    """

    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 3
    }

    response = requests.get(url, params=params)
    data = response.json()

    repos = []
    for repo in data.get("items", []):
        repos.append({
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"]
        })

    return repos
