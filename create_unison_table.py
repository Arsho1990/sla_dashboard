#!/usr/bin/env python3
"""
Create UNISON_LICENSES table with required columns
"""
import oracledb

conn = oracledb.connect(user='asnafees', password='Gryhhhbbn1', dsn='172.16.0.84:1521/orcl.avanza.pk')
cursor = conn.cursor()

try:
    # Create UNISON_LICENSES table
    print("Creating UNISON_LICENSES table...")
    cursor.execute("""
        CREATE TABLE UNISON_LICENSES (
            ID NUMBER PRIMARY KEY,
            CLIENT_NAME VARCHAR2(255) NOT NULL,
            LICENSE_GUID VARCHAR2(255) NOT NULL,
            MAXAGENTSSEATS NUMBER,
            LAST_UPDATED TIMESTAMP DEFAULT SYSDATE,
            CREATED_AT TIMESTAMP DEFAULT SYSDATE
        )
    """)
    
    # Create sequence for ID
    print("Creating sequence for ID...")
    cursor.execute("""
        CREATE SEQUENCE UNISON_LICENSES_SEQ
        START WITH 1
        INCREMENT BY 1
    """)
    
    # Create trigger for auto-increment ID
    print("Creating trigger for auto-increment...")
    cursor.execute("""
        CREATE TRIGGER UNISON_LICENSES_TRIGGER
        BEFORE INSERT ON UNISON_LICENSES
        FOR EACH ROW
        BEGIN
            SELECT UNISON_LICENSES_SEQ.NEXTVAL INTO :NEW.ID FROM DUAL;
        END;
    """)
    
    conn.commit()
    print("✅ UNISON_LICENSES table created successfully!")
    
except Exception as e:
    if "already exists" in str(e).upper():
        print("⚠️  UNISON_LICENSES table already exists")
    else:
        print(f"❌ Error: {e}")
        conn.rollback()
finally:
    conn.close()
