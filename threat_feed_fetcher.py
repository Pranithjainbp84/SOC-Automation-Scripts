import requests

def fetch_virus_total(api_key, domain):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {"x-apikey": api_key}
    response = requests.get(url, headers=headers)
    return response.json()
