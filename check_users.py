import oracledb

conn = oracledb.connect(user='asnafees', password='Gryhhhbbn1', dsn='172.16.0.84:1521/orcl.avanza.pk')
cursor = conn.cursor()

# Get all users
cursor.execute("SELECT USERNAME, PASSWORD, ROLE FROM USERS")
print('📋 All Users in Database:')
for row in cursor.fetchall():
    print(f'  Username: {row[0]}, Password: {row[1]}, Role: {row[2]}')

cursor.close()
conn.close()
