import requests

#importing os, a package in python that allows python to interact with the
#operating system, allowing you to do stuff with repositories
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")

url = f"https://newsapi.org/v2/everything?q=google&sortBy=popularity&language=en&apiKey={api_key}"

#Playing around and getting used to using APIs
response = requests.get(url)

print(response.status_code)

print(json.dumps(response.json(), indent = 4, sort_keys=True))