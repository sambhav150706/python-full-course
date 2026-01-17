import requests

url = "https://api.github.com"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response Data:")
print(response.json())


'''200 → Success ✅

404 → Not Found ❌

403 → Forbidden 🚫

500 → Server Error ⚠️'''
