import requests
from bs4 import BeautifulSoup

def request_github_trending(url):
    return requests.get(url)

def extract(page):
    soup = BeautifulSoup(page.text, "html.parser")
    return soup.find_all("article")

def transform(html_repos):
    join_in = []
    for num in html_repos:
        repository_name = ''.join(num.select_one('h1.h3.lh-condensed').text.split())
        number_stars = ' '.join(num.select_one('span.d-inline-block.float-sm-right').text.split())
        developer_name = num.select_one('img.avatar.mb-1.avatar-user')['alt']
        join_in.append({'developer': developer_name, 'repository_name': repository_name, 'nbr_stars': number_stars})
    return join_in

def format(repositories_data):
    join_in = ["Developer, Repository Name, Number of Stars"]
    for respon in repositories_data:
        num = [respon['developer'], respon['repository_name'], respon['nbr_stars']]
        join_in.append(', '.join(num))
    return "\n".join(join_in)

def _code():
    url = "https://github.com/trending"
    page = request_github_trending(url)
    html_repos = extract(page)
    repositories_data = transform(html_repos)
    print(format(repositories_data))
