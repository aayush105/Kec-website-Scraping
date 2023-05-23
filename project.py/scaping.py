from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

html_text = requests.get("https://exam.ioe.edu.np").text
soup = BeautifulSoup(html_text, "lxml")
notice = soup.find('table', class_='table')

# Find all span elements
name = notice.find_all('span')

for index,span in enumerate (name):
    data = span.text
    # print(data)
    if 'Notice' in data or 'Result' in data:
        # Find all a elements
        links = notice.find_all('a')
        for a in links:
            # Get the name and href attribute value
            name = a.text
            
            href = a.get('href')
            # print(href)
            
            # Combine the base URL with the relative URL of the link
            url = urljoin('https://exam.ioe.edu.np/', href)
            print(f'Name: {name.strip()}')
            print(f'href: {url}\n')
            # with open(f'Directory/{index}.txt', 'w') as f:
            #     f.write(f"Name: {name} \n")
            #     f.write(f"href: {url} \n")
            # print(f'File saved:{index}') 
    
    

# if __name__=='__main__':
#     while True:
#         find_jobs()
#         time_wait=10;
#         print(f'Waiting {time_wait} minutes...')
#         time.sleep(time_wait*60)


