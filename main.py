import requests

def get_number_of_repositories(username, access_token):
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return user_data["public_repos"]
    else:
        print(f"Error: Unable to fetch data for user {username}.")
        return None


def get_contribution_stats(username, access_token):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        total_contributions = 0

        for repo in repos:
            contributions_url = repo["contributors_url"]
            contributors_response = requests.get(contributions_url, headers=headers)
            if contributors_response.status_code == 200:
                contributors = contributors_response.json()
                for contributor in contributors:
                    if contributor["login"] == username:
                        total_contributions += contributor["contributions"]

        return total_contributions
    else:
        print(f"Error: Unable to fetch data for user {username}.")
        return None


if __name__ == "__main__":
    username = "Chris-derek"
    access_token = "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"

    num_repos = get_number_of_repositories(username, access_token)
    print(f"Number of repositories for {username}: {num_repos}")

    contribution_stats = get_contribution_stats(username, access_token)
    print(f"Total contributions to projects: {contribution_stats}")
