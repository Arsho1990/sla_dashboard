#!/usr/bin/env python3
import oracledb
import json

try:
    # Connect to database
    conn = oracledb.connect(
        user="asnafees",
        password="Gryhhhbbn1",
        dsn="172.16.0.84:1521/orcl.avanza.pk"
    )
    cursor = conn.cursor()
    
    # Check RDV_LICENSE table
    print("=" * 50)
    print("🔹 RDV_LICENSE Table")
    print("=" * 50)
    
    cursor.execute("SELECT COUNT(*) FROM RDV_LICENSE")
    rdv_count = cursor.fetchone()[0]
    print(f"Total RDV License Records: {rdv_count}")
    
    if rdv_count > 0:
        cursor.execute("SELECT * FROM RDV_LICENSE WHERE ROWNUM <= 3")
        for row in cursor.fetchall():
            print(f"Row: {row}")
        
        # Check STATUS column
        cursor.execute("SELECT DISTINCT STATUS FROM RDV_LICENSE")
        statuses = [row[0] for row in cursor.fetchall()]
        print(f"Unique STATUS values: {statuses}")
    
    # Check NIMBUS_LICENSE table
    print("\n" + "=" * 50)
    print("🔹 NIMBUS_LICENSE Table")
    print("=" * 50)
    
    cursor.execute("SELECT COUNT(*) FROM NIMBUS_LICENSE")
    nim_count = cursor.fetchone()[0]
    print(f"Total Nimbus License Records: {nim_count}")
    
    if nim_count > 0:
        cursor.execute("SELECT * FROM NIMBUS_LICENSE WHERE ROWNUM <= 3")
        for row in cursor.fetchall():
            print(f"Row: {row}")
        
        # Check STATUS column
        cursor.execute("SELECT DISTINCT STATUS FROM NIMBUS_LICENSE")
        statuses = [row[0] for row in cursor.fetchall()]
        print(f"Unique STATUS values: {statuses}")
    
    # Test the actual query from app.py
    print("\n" + "=" * 50)
    print("🔹 Testing API Query")
    print("=" * 50)
    
    cursor.execute("SELECT STATUS, COUNT(*) as count FROM RDV_LICENSE GROUP BY STATUS")
    rdv_status = cursor.fetchall()
    print(f"RDV Status Query Result: {rdv_status}")
    
    cursor.execute("SELECT STATUS, COUNT(*) as count FROM NIMBUS_LICENSE GROUP BY STATUS")
    nim_status = cursor.fetchall()
    print(f"Nimbus Status Query Result: {nim_status}")
    
    cursor.close()
    conn.close()
    
    print("\n✅ Database check complete!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
