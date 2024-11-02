import requests
from bs4 import BeautifulSoup

def get_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2')  # Adjust based on the website structure
    for idx, headline in enumerate(headlines):
        print(f"{idx + 1}. {headline.get_text()}")

# Example usage
get_headlines("https://example.com/news")
