import requests 
from bs4 import BeautifulSoup
import re 

url = "http://stackoverflow.com/?tab=month"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.04472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    questions_data = []
    
    questions = soup.select('.s-post-summary')
        
    for q in questions:
        title = q.select_one(".s-link")
        title = title.text.strip() if title else "No Title Found"
        
        votes_text = q.select_one(".s-post-summary--stats-item span")
        votes = int(re.search(r'\d+', votes_text.text.strip()).group()) if votes_text else 0
        
        answers_text = q.select_one(".s-post-summary--stats-item:nth-child(2) span")
        answers = int(re.search(r'\d+', answers_text.text.strip()).group()) if answers_text else 0
        
        views_text = q.select_one(".s-post-summary--stats-item:last-child span")
        views = int(re.search(r'\d+', views_text.text.strip()).group()) if views_text else 0
        
        questions_data.append({
            'title': title,
            'votes': votes,
            'answers': answers,
            'views': views
        })    
    
    print(questions_data)
else:
    print("Failed to fetch the webpage")