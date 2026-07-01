#!/usr/bin/env python3
import oracledb
import json

try:
    conn = oracledb.connect(
        user="asnafees",
        password="Gryhhhbbn1",
        dsn="172.16.0.84:1521/orcl.avanza.pk"
    )
    cursor = conn.cursor()
    
    print("=" * 60)
    print("📊 CHECKING ACTUAL LICENSE DATA")
    print("=" * 60)
    
    # Check RDV_LICENSE data
    print("\n🔹 RDV_LICENSE Table:")
    cursor.execute("SELECT COUNT(*) FROM RDV_LICENSE")
    rdv_total = cursor.fetchone()[0]
    print(f"Total Records: {rdv_total}")
    
    if rdv_total > 0:
        # Check STATUS distribution
        cursor.execute("SELECT STATUS, COUNT(*) as cnt FROM RDV_LICENSE GROUP BY STATUS")
        rdv_status = cursor.fetchall()
        print(f"RDV Status Distribution: {rdv_status}")
        
        # Check features
        features = ['MTS_MPS', 'TP', 'TCPIP', 'SYBASE', 'WEBSERVICE', 'MSMQ', 'MQSERIES']
        print("\nRDV Features Usage:")
        for feature in features:
            cursor.execute(f"SELECT COUNT(*) FROM RDV_LICENSE WHERE {feature} IS NOT NULL AND {feature} != '0' AND {feature} != 'N'")
            count = cursor.fetchone()[0]
            print(f"  {feature}: {count}")
    
    # Check NIMBUS_LICENSE data
    print("\n🔹 NIMBUS_LICENSE Table:")
    cursor.execute("SELECT COUNT(*) FROM NIMBUS_LICENSE")
    nim_total = cursor.fetchone()[0]
    print(f"Total Records: {nim_total}")
    
    if nim_total > 0:
        # Check STATUS distribution
        cursor.execute("SELECT STATUS, COUNT(*) as cnt FROM NIMBUS_LICENSE GROUP BY STATUS")
        nim_status = cursor.fetchall()
        print(f"Nimbus Status Distribution: {nim_status}")
    
    # Check LICENSE_EDIT_LOG
    print("\n🔹 LICENSE_EDIT_LOG Table:")
    cursor.execute("SELECT COUNT(*) FROM LICENSE_EDIT_LOG")
    log_count = cursor.fetchone()[0]
    print(f"Total Edit Log Records: {log_count}")
    
    cursor.close()
    conn.close()
    print("\n✅ Database check complete!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
