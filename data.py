import requests

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
question_list = response.json()

question_data = [i for i in question_list["results"]]
