#!/usr/bin/env python3
import json
import requests

try:
    response = requests.get('http://172.16.9.113:5000/api/license-usage-data')
    data = response.json()
    
    print("✅ API Response:")
    print(f"RDV Status: {data.get('rdv_status', [])}")
    print(f"Nimbus Status: {data.get('nimbus_status', [])}")
    print(f"Unison Status: {data.get('unison_status', [])}")
    print(f"\nLicense Distribution:")
    for item in data.get('license_type_distribution', []):
        print(f"  {item['type']}: {item['count']}")
        
except Exception as e:
    print(f"❌ Error: {e}")
