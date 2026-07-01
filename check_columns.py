import oracledb

conn = oracledb.connect(user='asnafees', password='Gryhhhbbn1', dsn='172.16.0.84:1521/orcl.avanza.pk')
cursor = conn.cursor()

# Check all columns in SLA table
cursor.execute("SELECT COLUMN_NAME, DATA_TYPE FROM USER_TAB_COLUMNS WHERE TABLE_NAME = 'SLA' ORDER BY COLUMN_NAME")
print('📊 SLA TABLE COLUMNS:')
for col in cursor.fetchall():
    print(f'  {col[0]}: {col[1]}')

# Check if YEAR_2026 exists
cursor.execute("SELECT COUNT(*) FROM USER_TAB_COLUMNS WHERE TABLE_NAME = 'SLA' AND COLUMN_NAME = 'YEAR_2026'")
result = cursor.fetchone()[0]
print(f'\n2026 Column Exists: {result > 0}')

# Get sample data
print('\n📋 Sample SLA Records:')
cursor.execute("SELECT BANK_NAME, PERIOD FROM SLA FETCH FIRST 3 ROWS ONLY")
for row in cursor.fetchall():
    print(f'  {row[0]} - {row[1]}')

cursor.close()
conn.close()
