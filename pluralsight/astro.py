import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
people = json['people']
for person in people:
    print(f"{person['name']} is in space on the {person['craft']}.")
print(f"Total number of people in space: {len(people)}")
