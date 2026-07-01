import oracledb
import sys

try:
    print("Connecting to database...", flush=True)
    conn = oracledb.connect(user='asnafees', password='Gryhhhbbn1', dsn='172.16.0.84:1521/orcl.avanza.pk')
    cursor = conn.cursor()
    print("Connected!", flush=True)

    # List all tables
    print('Tables in schema:', flush=True)
    cursor.execute("SELECT TABLE_NAME FROM USER_TABLES ORDER BY TABLE_NAME")
    tables = cursor.fetchall()
    for t in tables:
        print(f'  {t[0]}')

    print()

    # Check NIMBUS_LICENSES
    try:
        print('NIMBUS_LICENSES count:', flush=True)
        cursor.execute('SELECT COUNT(*) FROM NIMBUS_LICENSES')
        count = cursor.fetchone()[0]
        print(f'  {count}', flush=True)
    except Exception as e:
        print(f'  Error: {e}', flush=True)

    print()

    # Check RDV_LICENSES
    try:
        print('RDV_LICENSES count:', flush=True)
        cursor.execute('SELECT COUNT(*) FROM RDV_LICENSES')
        count = cursor.fetchone()[0]
        print(f'  {count}', flush=True)
    except Exception as e:
        print(f'  Error: {e}', flush=True)

    cursor.close()
    conn.close()
except Exception as e:
    print(f'Fatal error: {e}', flush=True)
    import traceback
    traceback.print_exc()

