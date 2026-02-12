import db

try:
    conn = db.get_connection()
    print("✅ MySQL Connected Successfully")
    conn.close()
except Exception as e:
    print("❌ Connection Failed:", e)
