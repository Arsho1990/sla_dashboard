#!/usr/bin/env python
"""
Minimal Flask app to test analytics dashboard UI
This version uses mock data instead of database connections
"""
from flask import Flask, render_template, jsonify, session

app = Flask(__name__)
app.secret_key = 'test-key-for-ui-testing'

@app.route('/')
def dashboard():
    # Simulate logged-in user
    session['username'] = 'test_user'
    session['role'] = 'admin'
    
    # Mock data for dashboard
    banks = ['Bank A', 'Bank B', 'Bank C']
    y2023 = [100, 200, 150]
    y2024 = [120, 210, 160]
    y2025 = [130, 220, 170]
    percent_23_to_24 = [20, 5, 6.67]
    percent_24_to_25 = [8.33, 4.76, 6.25]
    all_banks = banks
    currency_totals = [
        {'SLA_CURRENCY': 'PKR', 'YEAR_2023': 500000, 'YEAR_2024': 550000, 'YEAR_2025': 600000},
        {'SLA_CURRENCY': 'USD', 'YEAR_2023': 10000, 'YEAR_2024': 11000, 'YEAR_2025': 12000}
    ]
    
    return render_template('dashboard.html',
                         data=[],
                         banks=banks,
                         y2023=y2023,
                         y2024=y2024,
                         y2025=y2025,
                         percent_23_to_24=percent_23_to_24,
                         percent_24_to_25=percent_24_to_25,
                         all_banks=all_banks,
                         selected_bank=None,
                         role='admin',
                         currency_totals=currency_totals,
                         login_time=None,
                         logout_time=None)

@app.route('/api/sla-usage-data')
def sla_usage_data():
    """Mock SLA usage data"""
    return jsonify({
        'currency_distribution': [
            {'currency': 'PKR', 'amount': 600000},
            {'currency': 'USD', 'amount': 12000}
        ],
        'bank_distribution': [
            {'bank': 'Bank A', 'amount': 130},
            {'bank': 'Bank B', 'amount': 220},
            {'bank': 'Bank C', 'amount': 170}
        ],
        'trend_data': [
            {'period': 'Q1', 'y2023': 250000, 'y2024': 275000, 'y2025': 300000},
            {'period': 'Q2', 'y2023': 250000, 'y2024': 275000, 'y2025': 300000}
        ]
    })

@app.route('/api/license-usage-data')
def license_usage_data():
    """Mock license usage data"""
    return jsonify({
        'rdv_status': [
            {'status': 'Active', 'count': 45},
            {'status': 'Inactive', 'count': 5}
        ],
        'nimbus_status': [
            {'status': 'Active', 'count': 30},
            {'status': 'Inactive', 'count': 2}
        ],
        'license_type_distribution': [
            {'type': 'RDV Licenses', 'count': 50},
            {'type': 'Nimbus Licenses', 'count': 32}
        ],
        'features_usage': {
            'Networks': 35,
            'Adapters': 28,
            'TP': 22,
            'TCPIP': 40,
            'MSMQ': 18,
            'WebService': 25
        },
        'recent_changes': [
            {
                'TABLE_NAME': 'RDV_LICENSES',
                'CLIENT_NAME': 'Client A',
                'FIELD_NAME': 'MAXNETWORKS',
                'OLD_VALUE': '10',
                'NEW_VALUE': '20',
                'CHANGED_BY': 'admin',
                'CHANGE_TIME': '27-Apr-2026 02:30:00 PM'
            }
        ]
    })

@app.route('/login')
def login():
    return "Login page"

if __name__ == '__main__':
    print("Starting test Flask server on http://0.0.0.0:5000")
    print("This version uses mock data for testing the analytics UI")
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
