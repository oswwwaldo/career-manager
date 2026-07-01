import requests
#pylint: skip-file

'''
    Communicates and retrives book information from the Hardcover API, rate limited at 60 requests per minute, 
    indivdual queries have 30 second timeouts and the token lifespan expires 6/25/27
'''

HARDCOVER_API_URL = "https://api.hardcover.app/v1/graphql"
HARDCOVER_API_TOKEN = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJIYXJkY292ZXIiLCJ2ZXJzaW9uIjoiOCIsImp0aSI6ImUyYjIyMmNiLWIyMDMtNDA0MS04YmYyLTAyYjg0YTMxNmU4OSIsImFwcGxpY2F0aW9uSWQiOjIsInN1YiI6IjExOTUwNSIsImF1ZCI6IjEiLCJpZCI6IjExOTUwNSIsImxvZ2dlZEluIjp0cnVlLCJpYXQiOjE3ODI0NDQzMTcsImV4cCI6MTgxMzk4MDMxNywiaHR0cHM6Ly9oYXN1cmEuaW8vand0L2NsYWltcyI6eyJ4LWhhc3VyYS1hbGxvd2VkLXJvbGVzIjpbInVzZXIiXSwieC1oYXN1cmEtZGVmYXVsdC1yb2xlIjoidXNlciIsIngtaGFzdXJhLXJvbGUiOiJ1c2VyIiwiWC1oYXN1cmEtdXNlci1pZCI6IjExOTUwNSJ9LCJ1c2VyIjp7ImlkIjoxMTk1MDV9fQ.kKduIcsFRccBQUfqTTsc6bl8GMqrj6s39PRymyTd0jw"

# 2. Define Headers (Hardcover recommends setting a descriptive User-Agent)
headers = {
    "Authorization": HARDCOVER_API_TOKEN,
    "Content-Type": "application/json",
    "User-Agent": "MyLocalBookScript/1.0 (Contact: myemail@example.com)"
}

# 3. Define the GraphQL Query
# This basic 'me' query verifies your identity
query = """
query {
  me {
    id
    username
  }
}
"""

# 4. Execute the HTTP POST request
response = requests.post(HARDCOVER_API_URL, json={'query': query}, headers=headers)

# 5. Handle the output
if response.status_code == 200:
    data = response.json()
    print("Successfully connected to Hardcover!")
    print(data)
else:
    print(f"Failed to connect. Status Code: {response.status_code}")
    print(response.text)