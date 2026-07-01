import oracledb

conn = oracledb.connect(user='asnafees', password='Gryhhhbbn1', dsn='172.16.0.84:1521/orcl.avanza.pk')
cursor = conn.cursor()

print('RDV_LICENSES columns:')
cursor.execute("""SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='RDV_LICENSES' ORDER BY COLUMN_ID""")
rdv_cols = cursor.fetchall()
for col in rdv_cols:
    print(f'  {col[0]}')

print()
print('NIMBUS_LICENSES columns:')
cursor.execute("""SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='NIMBUS_LICENSES' ORDER BY COLUMN_ID""")
nim_cols = cursor.fetchall()
for col in nim_cols:
    print(f'  {col[0]}')

cursor.close()
conn.close()
