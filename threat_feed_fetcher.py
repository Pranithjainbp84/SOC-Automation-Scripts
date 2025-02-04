import requests

# VirusTotal API key (replace with your actual key)
API_KEY = 'your_api_key_here'
VT_URL = 'https://www.virustotal.com/api/v3/domains/'

# Function to fetch threat intelligence for a domain
def fetch_virus_total(api_key, domain):
    headers = {'x-apikey': api_key}
    response = requests.get(f'{VT_URL}{domain}', headers=headers)
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return f"Error: Unable to fetch data for {domain}"

# Example usage
if __name__ == "__main__":
    domain = 'example.com'
    print(fetch_virus_total(API_KEY, domain))
