# Import necessary modules 
import requests
from bs4 import BeautifulSoup

# Create a variable with the URL to the webpage
url = 'https://www.isro.gov.in/'

# Scrape the HTML at the url
r = requests.get(url)

# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(r.text, 'html.parser')

# Find all the <a> tags (links) on the page
links = soup.find_all('a')

# Use list comprehension to filter out unwanted links
filtered_links = [link for link in links if link.has_attr('href')]

# Iterate over the filtered links
for link in filtered_links:
    # Print out the link text and the link's href
    print(link.text + ": " + link['href'])
