import requests
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        for user in data:
            print(f"{user['title']}")

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        with open('posts.csv', 'w', newline='') as file:
            data = r.json()
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in data:
                writer.writerow({key: value for key, value in user.items() if key != 'userId'})
