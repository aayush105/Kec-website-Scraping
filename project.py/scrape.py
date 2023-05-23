from bs4 import BeautifulSoup
import re
import requests



content = requests.get("https://exam.ioe.edu.np")

soup = BeautifulSoup(content,'lxml')
a
soup.contents