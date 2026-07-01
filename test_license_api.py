#!/usr/bin/env python3
import requests
import json

try:
    response = requests.get('http://localhost:5000/api/license-usage-data')
    data = response.json()
    
    print("✅ API Response Status:", response.status_code)
    print("\n📊 RDV Status Count:", len(data.get('rdv_status', [])))
    print("RDV Status Data:", data.get('rdv_status', []))
    
    print("\n📊 Nimbus Status Count:", len(data.get('nimbus_status', [])))
    print("Nimbus Status Data:", data.get('nimbus_status', []))
    
    print("\n📊 License Distribution:", data.get('license_type_distribution', []))
    
    print("\n📊 Features Usage:", data.get('features_usage', {}))
    
except Exception as e:
    print(f"❌ Error: {e}")
