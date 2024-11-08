import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

url = sys.argv[1]

try:
    ip_address = socket.gethostbyname(url)
    print(f"\nThe IP address of {url} is: {ip_address}\n")

    IPINFO_API_KEY = "87739c4795f928" 
    response = requests.get(f"https://ipinfo.io/{ip_address}/json?token={IPINFO_API_KEY}")
    response.raise_for_status()
    data = response.json()

    print(f"Location (lat, long): {data.get('loc', 'Unknown')}")
    print(f"Region: {data.get('region', 'Unknown')}")
    print(f"Country: {data.get('country', 'Unknown')}")

except Exception as e:
    print(f"Error processing {url}: {e}")
