#!/usr/bin/env python3
import oracledb

conn = oracledb.connect(user='asnafees', password='Gryhhhbbn1', dsn='172.16.0.84:1521/orcl.avanza.pk')
cursor = conn.cursor()

# Check RDV_LICENSES table structure
cursor.execute("""
    SELECT COLUMN_NAME FROM USER_TAB_COLUMNS 
    WHERE TABLE_NAME = 'RDV_LICENSES'
    ORDER BY COLUMN_ID
""")
print('RDV_LICENSES columns:')
for col in cursor.fetchall():
    print(f'  - {col[0]}')

# Check NIMBUS_LICENSES table structure
cursor.execute("""
    SELECT COLUMN_NAME FROM USER_TAB_COLUMNS 
    WHERE TABLE_NAME = 'NIMBUS_LICENSES'
    ORDER BY COLUMN_ID
""")
print('\nNIMBUS_LICENSES columns:')
for col in cursor.fetchall():
    print(f'  - {col[0]}')

# Check if UNISON_LICENSES exists
cursor.execute("""
    SELECT COUNT(*) FROM USER_TABLES WHERE TABLE_NAME = 'UNISON_LICENSES'
""")
unison_exists = cursor.fetchone()[0] > 0
print(f'\nUNISON_LICENSES exists: {unison_exists}')

conn.close()
