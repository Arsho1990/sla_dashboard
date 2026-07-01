import requests

# Test the SLA usage API
response = requests.get('http://localhost:5000/api/sla-usage-data')
data = response.json()

print("✅ API Response:")
print(f"Current Year: {data.get('current_year')}")
print(f"\nCurrency Distribution: {data.get('currency_distribution')}")
print(f"\nUSD Banks (first 3): {data.get('bank_distribution', {}).get('USD', [])[:3]}")
print(f"\nPKR Banks (first 3): {data.get('bank_distribution', {}).get('PKR', [])[:3]}")
