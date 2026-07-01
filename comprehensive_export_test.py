#!/usr/bin/env python
"""
Comprehensive test for SLA Dashboard export functionality
Tests all export scenarios: Excel and PDF for both SLA and Licenses
"""
import requests
import json
from datetime import datetime

def test_all_exports():
    base_url = 'http://172.16.9.113:5000'
    
    test_cases = [
        {
            'name': 'SLA Data to Excel',
            'endpoint': '/api/export-sla',
            'payload': {
                'format': 'xlsx',
                'columns': ['Bank Name', 'Currency', 'SLA %', 'Status'],
                'data': [
                    ['Bank1', 'PKR', '99.5', 'Active'],
                    ['Bank2', 'USD', '99.9', 'Active'],
                    ['Bank3', 'EUR', '99.8', 'Inactive'],
                    ['Bank4', 'GBP', '99.6', 'Active']
                ]
            },
            'output_file': 'comprehensive_test_sla.xlsx'
        },
        {
            'name': 'SLA Data to PDF',
            'endpoint': '/api/export-sla',
            'payload': {
                'format': 'pdf',
                'columns': ['Bank Name', 'Currency', 'SLA %', 'Status'],
                'data': [
                    ['Bank1', 'PKR', '99.5', 'Active'],
                    ['Bank2', 'USD', '99.9', 'Active'],
                    ['Bank3', 'EUR', '99.8', 'Inactive'],
                    ['Bank4', 'GBP', '99.6', 'Active']
                ]
            },
            'output_file': 'comprehensive_test_sla.pdf'
        },
        {
            'name': 'RDV Licenses to Excel',
            'endpoint': '/api/export-licenses',
            'payload': {
                'format': 'xlsx',
                'table_type': 'rdv',
                'columns': ['Client', 'License GUID', 'Max Networks', 'Status'],
                'data': [
                    ['Client1', 'ABC-123', '5', 'Active'],
                    ['Client2', 'DEF-456', '10', 'Active'],
                    ['Client3', 'GHI-789', '3', 'Inactive']
                ]
            },
            'output_file': 'comprehensive_test_rdv.xlsx'
        },
        {
            'name': 'RDV Licenses to PDF',
            'endpoint': '/api/export-licenses',
            'payload': {
                'format': 'pdf',
                'table_type': 'rdv',
                'columns': ['Client', 'License GUID', 'Max Networks', 'Status'],
                'data': [
                    ['Client1', 'ABC-123', '5', 'Active'],
                    ['Client2', 'DEF-456', '10', 'Active'],
                    ['Client3', 'GHI-789', '3', 'Inactive']
                ]
            },
            'output_file': 'comprehensive_test_rdv.pdf'
        },
        {
            'name': 'Nimbus Licenses to Excel',
            'endpoint': '/api/export-licenses',
            'payload': {
                'format': 'xlsx',
                'table_type': 'nimbus',
                'columns': ['Client', 'License GUID', 'Max Terminals'],
                'data': [
                    ['NimbusClient1', 'NIM-123', '10'],
                    ['NimbusClient2', 'NIM-456', '20'],
                    ['NimbusClient3', 'NIM-789', '15']
                ]
            },
            'output_file': 'comprehensive_test_nimbus.xlsx'
        },
        {
            'name': 'Nimbus Licenses to PDF',
            'endpoint': '/api/export-licenses',
            'payload': {
                'format': 'pdf',
                'table_type': 'nimbus',
                'columns': ['Client', 'License GUID', 'Max Terminals'],
                'data': [
                    ['NimbusClient1', 'NIM-123', '10'],
                    ['NimbusClient2', 'NIM-456', '20'],
                    ['NimbusClient3', 'NIM-789', '15']
                ]
            },
            'output_file': 'comprehensive_test_nimbus.pdf'
        }
    ]
    
    print("=" * 70)
    print("SLA Dashboard - Comprehensive Export Functionality Test")
    print("=" * 70)
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    passed = 0
    failed = 0
    
    for test in test_cases:
        print(f"Testing: {test['name']}")
        print(f"Endpoint: {base_url}{test['endpoint']}")
        
        try:
            response = requests.post(
                f"{base_url}{test['endpoint']}",
                json=test['payload'],
                timeout=10
            )
            
            if response.status_code == 200:
                with open(test['output_file'], 'wb') as f:
                    f.write(response.content)
                
                file_size = len(response.content)
                content_type = response.headers.get('Content-Type', 'unknown')
                print(f"  ✓ SUCCESS - File saved: {test['output_file']} ({file_size} bytes)")
                print(f"  Content-Type: {content_type}")
                passed += 1
            else:
                print(f"  ✗ FAILED - Status Code: {response.status_code}")
                print(f"  Response: {response.text[:200]}")
                failed += 1
                
        except Exception as e:
            print(f"  ✗ EXCEPTION: {str(e)}")
            failed += 1
        
        print()
    
    # Summary
    print("=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"Total Tests: {len(test_cases)}")
    print(f"Passed: {passed} ✓")
    print(f"Failed: {failed} ✗")
    print(f"Success Rate: {(passed/len(test_cases)*100):.1f}%")
    print(f"Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    return failed == 0

if __name__ == '__main__':
    success = test_all_exports()
    exit(0 if success else 1)
