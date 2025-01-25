import requests

class GithubScraper:
    def __init__(self, github_link):
        if not github_link:
            raise ValueError("GitHub link cannot be empty")
        self.github_link = github_link.strip()
        self.username = self.github_link.split('/')[-1]

    def fetch_repositories(self):
        """Fetching the repositories of the GitHub user."""
        
        api_url = f"https://api.github.com/users/{self.username}/repos"
        response = requests.get(api_url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

    def project_details(self):
        """ Getting project info and related things for the django models """
        try:
            repositories = self.fetch_repositories()
            
            if not repositories:
                return f"No public repositories found for {self.username}."

            project_info = []
            for repo in repositories:
                languages_url = requests.get(repo['languages_url'])
                languages = list(languages_url.json())
                
                project_info.append({
                    'name': repo.get('name', 'N/A'),
                    'description': repo.get('description', 'No description'),
                    'github_link' : repo.get('html_url','N/A'),
                    'language': languages,
                    'deployed_link': repo.get('homepage', 'N/A')
                })

            return project_info

        except Exception as e:
            return str(e)

if __name__ == "__main__":
    github_link = "https://github.com/dineshreddypaidi"
    
    scraper = GithubScraper(github_link)
    for details in scraper.project_details():
        print(details)