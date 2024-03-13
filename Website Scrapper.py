import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the article elements
        articles = soup.find_all('article')

        # Extract information from each article
        for article in articles:
            # Extract the title of the article
            title = article.find('h2').text.strip()

            # Extract the link to the article
            link = article.find('a')['href']

            # Print the title and link
            print(f"Title: {title}")
            print(f"Link: {link}")
            print()

    else:
        print("Failed to retrieve webpage.")

if __name__ == "__main__":
    url = input("Enter the URL of the website to scrape: ")
    scrape_website(url)
