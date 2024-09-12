import requests


def fetch_food_items(query):
    api_url = f"https://api.calorieninjas.com/v1/nutrition?query={query}"
    headers = {
        'X-Api-Key': "L3CXnXFXDdyk1eD+K2XfaQ==gzk5Thrkwk67Gkcv"
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json().get('items', [])
    return []
