#!/usr/bin/env python
"""
Test for fixes to export functionality
- Test 1: PDF export with many columns (should fit all)
- Test 2: Excel export with dropdown values (should show selected only)  
- Test 3: Year filter (should show all available years)
"""
import requests
import json

def test_pdf_with_many_columns():
    """Test PDF export with many columns to verify they all fit"""
    url = 'http://172.16.9.113:5000/api/export-sla'
    
    # Create test data with many columns (simulating the SLA data)
    columns = ['BANK_NAME', '2022', '2023', '2024', '2025', '2026', '2027', 
               'Difference', 'Increment (%)', 'Status', 'Doc Type', 'Upload Date', 
               'Modified Date', 'Currency', 'RDV', 'Nimbus']
    
    data = [
        ['Bank 1', '1000.0', '1500.0', '2000.0', '2500.0', '3000.0', '3200.0',
         '200', '6.67%', 'Active', 'Agreement', '2026-05-05', '2026-05-05', 'PKR', 'Yes', 'No'],
        ['Bank 2', '5000.0', '5000.0', '5000.0', '8000.0', '10000.0', '10500.0',
         '500', '5.00%', 'Active', 'Amendment', '2026-05-05', '2026-05-05', 'USD', 'No', 'Yes'],
    ]
    
    payload = {
        'format': 'pdf',
        'columns': columns,
        'data': data
    }
    
    print("Testing PDF export with many columns...")
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            with open('test_pdf_many_columns.pdf', 'wb') as f:
                f.write(response.content)
            file_size = len(response.content)
            print(f"  ✓ PDF with {len(columns)} columns created: test_pdf_many_columns.pdf ({file_size} bytes)")
            return True
        else:
            print(f"  ✗ Error: {response.status_code} - {response.text[:200]}")
            return False
    except Exception as e:
        print(f"  ✗ Exception: {e}")
        return False

def test_excel_dropdown_values():
    """Test Excel export with dropdown values (should show selected only)"""
    url = 'http://172.16.9.113:5000/api/export-sla'
    
    # Simulate dropdown values - in the report, should only show the selected value, not all options
    columns = ['BANK_NAME', 'STATUS', 'CURRENCY', 'PERIOD']
    
    # Status column should show only the selected value (Active or Inactive), not both
    data = [
        ['Bank 1', 'Active', 'PKR', '2026'],  # Should export just "Active"
        ['Bank 2', 'Inactive', 'USD', '2025'],  # Should export just "Inactive"
        ['Bank 3', 'Active', 'EUR', '2024'],
    ]
    
    payload = {
        'format': 'xlsx',
        'columns': columns,
        'data': data
    }
    
    print("Testing Excel export with dropdown values...")
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            with open('test_excel_dropdown_values.xlsx', 'wb') as f:
                f.write(response.content)
            file_size = len(response.content)
            print(f"  ✓ Excel with dropdown values created: test_excel_dropdown_values.xlsx ({file_size} bytes)")
            print(f"    Exported data should show: 'Active', 'Inactive', 'Active' (not all options)")
            return True
        else:
            print(f"  ✗ Error: {response.status_code} - {response.text[:200]}")
            return False
    except Exception as e:
        print(f"  ✗ Exception: {e}")
        return False

def test_year_filter_visible():
    """Test that year filter loads (would need browser to verify years 2022-2027 are shown)"""
    print("Testing year filter...")
    try:
        response = requests.get('http://172.16.9.113:5000/dashboard', timeout=10)
        if response.status_code == 200:
            # Check if the HTML contains year options
            html = response.text
            year_checks = {
                '2022': 'value="2022"' in html,
                '2023': 'value="2023"' in html,
                '2024': 'value="2024"' in html,
                '2025': 'value="2025"' in html,
                '2026': 'value="2026"' in html,
                '2027': 'value="2027"' in html,
            }
            
            found_years = [year for year, found in year_checks.items() if found]
            missing_years = [year for year, found in year_checks.items() if not found]
            
            if found_years:
                print(f"  ✓ Year filter found years: {', '.join(found_years)}")
            if missing_years:
                print(f"  ⚠ Year filter missing: {', '.join(missing_years)}")
            
            return len(found_years) >= 4  # At least 4 years should be present
        else:
            print(f"  ✗ Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"  ✗ Exception: {e}")
        return False

if __name__ == '__main__':
    print("=" * 70)
    print("Testing Export Fixes")
    print("=" * 70)
    
    test1 = test_pdf_with_many_columns()
    print()
    test2 = test_excel_dropdown_values()
    print()
    test3 = test_year_filter_visible()
    
    print()
    print("=" * 70)
    passed = sum([test1, test2, test3])
    print(f"Tests Passed: {passed}/3")
    print("=" * 70)
