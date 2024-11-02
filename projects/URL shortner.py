import requests

def shorten_url(url):
    api_url = f"http://tinyurl.com/api-create.php?url={url}"
    response = requests.get(api_url)
    if response.status_code == 200:
        print(f"Shortened URL: {response.text}")
    else:
        print("Error creating shortened URL.")

# Example usage
shorten_url("https://www.example.com")
