import os
import requests

def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the text content from the response
        text_content = response.text
        
        return text_content
    else:
        print(f"Failed to scrape website. Status code: {response.status_code}")
        return None

def save_text_content(text_content, output_file):
    # Create the 'docs' directory if it doesn't exist
    os.makedirs('data/docs', exist_ok=True)
    
    # Save the text content to a file
    with open(output_file, 'w') as file:
        file.write(text_content)

def main():
    # Specify the URL of the website you want to scrape
    website_url = "https://example.com"
    
    # Scrape the website
    text_content = scrape_website(website_url)
    
    if text_content:
        # Save the text content to a file in the 'data/docs' directory
        output_file = os.path.join('data/docs', 'website_content.txt')
        save_text_content(text_content, output_file)
        print("Website content scraped and saved successfully.")

if __name__ == "__main__":
    main()
