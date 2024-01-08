import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://japac-ce-demo.siemplify-soar.com/swagger/index.html'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all occurrences of 'GET,' 'POST,' 'DELETE,' or 'PUT' buttons within the specified <div>
    relevant_divs = soup.find_all('div', class_='opblock-summary opblock-summary-get opblock-summary-post opblock-summary-delete opblock-summary-put')
    print(relevant_divs)
    # Extract and print the content after each occurrence
    for div in relevant_divs:
        method_button = div.find('button', class_='opblock-summary-method')
        method_span = div.find('span', class_='opblock-summary-method')

        # Use the text from the button if available, otherwise use the text from the span
        method = method_button.text.strip() if method_button else (method_span.text.strip() if method_span else "No HTTP method found.")

        content_after = div.find_next('p').text if div.find_next('p') else "No content found."
        print(f"Request: {method}\nContent After: {content_after}\n")
else:
    print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")
