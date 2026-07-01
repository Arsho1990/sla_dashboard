#!/usr/bin/env python
import requests
import time

time.sleep(2)

print("=" * 60)
print("Testing Fixes")
print("=" * 60)

# Test PDF Export
print("\n1. Testing PDF Export with many columns...")
payload = {
    'format': 'pdf',
    'columns': ['Bank', 'Year2022', 'Year2023', 'Year2024', 'Year2025', 'Year2026', 'Year2027', 'Status'],
    'data': [['Bank1', '100', '200', '300', '400', '500', '600', 'Active']]
}
try:
    response = requests.post('http://172.16.9.113:5000/api/export-sla', json=payload, timeout=10)
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        print("   ✓ PDF export successful with multiple columns")
    else:
        print(f"   ✗ Error: {response.text[:100]}")
except Exception as e:
    print(f"   ✗ Exception: {str(e)[:100]}")

# Test Excel Export
print("\n2. Testing Excel Export...")
payload = {
    'format': 'xlsx',
    'columns': ['Bank Name', 'Status', 'Currency'],
    'data': [['Bank1', 'Active', 'PKR'], ['Bank2', 'Inactive', 'USD']]
}
try:
    response = requests.post('http://172.16.9.113:5000/api/export-sla', json=payload, timeout=10)
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        print("   ✓ Excel export successful")
    else:
        print(f"   ✗ Error: {response.text[:100]}")
except Exception as e:
    print(f"   ✗ Exception: {str(e)[:100]}")

# Test Dashboard Year Filter
print("\n3. Testing Dashboard Year Filter...")
try:
    response = requests.get('http://172.16.9.113:5000/dashboard', timeout=10)
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        html = response.text
        years_found = []
        for year in ['2022', '2023', '2024', '2025', '2026', '2027']:
            if f'value="{year}"' in html or f"value='{year}'" in html:
                years_found.append(year)
        if years_found:
            print(f"   ✓ Year filter found: {', '.join(years_found)}")
        else:
            print("   ⚠ No year options found in HTML")
    else:
        print(f"   ✗ Error: {response.status_code}")
except Exception as e:
    print(f"   ✗ Exception: {str(e)[:100]}")

print("\n" + "=" * 60)
print("Testing Complete")
print("=" * 60)
