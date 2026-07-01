#!/usr/bin/env python3
import sys
try:
    import oracledb
    print("✅ oracledb imported successfully")
    
    conn = oracledb.connect(
        user="asnafees",
        password="Gryhhhbbn1",
        dsn="172.16.0.84:1521/orcl.avanza.pk"
    )
    print("✅ Connected to database")
    
    cursor = conn.cursor()
    print("✅ Cursor created")
    
    # Get all table names
    cursor.execute("""
        SELECT table_name FROM user_tables 
        WHERE table_name IN ('RDV_LICENSE', 'NIMBUS_LICENSE', 'LICENSE_EDIT_LOG')
    """)
    
    tables = cursor.fetchall()
    print(f"Found tables: {tables}")
    
    if tables:
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"  {table_name}: {count} records")
    
    cursor.close()
    conn.close()
    print("✅ Done!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
