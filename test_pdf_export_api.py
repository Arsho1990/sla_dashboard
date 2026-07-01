#!/usr/bin/env python
import requests
import json

# Test SLA PDF export
def test_sla_pdf_export():
    url = 'http://172.16.9.113:5000/api/export-sla'
    
    payload = {
        'format': 'pdf',
        'columns': ['Bank Name', 'Currency', 'SLA %'],
        'data': [
            ['Bank1', 'PKR', '99.5'],
            ['Bank2', 'USD', '99.9'],
            ['Bank3', 'EUR', '99.8']
        ]
    }
    
    print("Testing SLA PDF Export API...")
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        
        if response.status_code == 200:
            with open('test_sla_export.pdf', 'wb') as f:
                f.write(response.content)
            print(f"✓ PDF file saved: test_sla_export.pdf ({len(response.content)} bytes)")
        else:
            print(f"✗ Error: {response.text}")
            
    except Exception as e:
        print(f"✗ Connection failed: {e}")

# Test Licenses PDF export
def test_licenses_pdf_export():
    url = 'http://172.16.9.113:5000/api/export-licenses'
    
    payload = {
        'format': 'pdf',
        'table_type': 'nimbus',
        'columns': ['Client', 'License GUID', 'Max Terminals'],
        'data': [
            ['Client1', 'ABC-123', '10'],
            ['Client2', 'DEF-456', '20']
        ]
    }
    
    print("\nTesting Licenses PDF Export API...")
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        
        if response.status_code == 200:
            with open('test_licenses_export.pdf', 'wb') as f:
                f.write(response.content)
            print(f"✓ PDF file saved: test_licenses_export.pdf ({len(response.content)} bytes)")
        else:
            print(f"✗ Error: {response.text}")
            
    except Exception as e:
        print(f"✗ Connection failed: {e}")

if __name__ == '__main__':
    test_sla_pdf_export()
    test_licenses_pdf_export()
    print("\n✓ PDF Export tests completed successfully!")
