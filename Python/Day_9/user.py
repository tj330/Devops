import requests

url = f"https://api.github.com/users/tj330"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("\nMy GitHub User Info:\n")
    print(f"Name: {data.get('name')}")
    print(f"Public Repos: {data.get('public_repos')}")
    print(f"Followers: {data.get('followers')}")
else:
    print("Failed to fetch GitHub data.")
