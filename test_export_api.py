#!/usr/bin/env python
import requests
import json

# Test SLA export endpoint
def test_sla_export():
    url = 'http://172.16.9.113:5000/api/export-sla'
    
    payload = {
        'format': 'xlsx',
        'columns': ['Bank Name', 'Currency', 'SLA %'],
        'data': [
            ['Bank1', 'PKR', '99.5'],
            ['Bank2', 'USD', '99.9'],
            ['Bank3', 'EUR', '99.8']
        ]
    }
    
    print("Testing SLA Export API...")
    print(f"URL: {url}")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        print(f"\nStatus Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        
        if response.status_code == 200:
            with open('test_sla_export.xlsx', 'wb') as f:
                f.write(response.content)
            print(f"✓ Excel file saved: test_sla_export.xlsx ({len(response.content)} bytes)")
        else:
            print(f"✗ Error: {response.text}")
            
    except Exception as e:
        print(f"✗ Connection failed: {e}")

# Test Licenses export endpoint
def test_licenses_export():
    url = 'http://172.16.9.113:5000/api/export-licenses'
    
    payload = {
        'format': 'xlsx',
        'table_type': 'rdv',
        'columns': ['Client', 'License GUID', 'Max Networks'],
        'data': [
            ['Client1', 'ABC-123', '5'],
            ['Client2', 'DEF-456', '10']
        ]
    }
    
    print("\n\nTesting Licenses Export API...")
    print(f"URL: {url}")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        print(f"\nStatus Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        
        if response.status_code == 200:
            with open('test_licenses_export.xlsx', 'wb') as f:
                f.write(response.content)
            print(f"✓ Excel file saved: test_licenses_export.xlsx ({len(response.content)} bytes)")
        else:
            print(f"✗ Error: {response.text}")
            
    except Exception as e:
        print(f"✗ Connection failed: {e}")

if __name__ == '__main__':
    test_sla_export()
    test_licenses_export()
    print("\n\nTests completed!")
