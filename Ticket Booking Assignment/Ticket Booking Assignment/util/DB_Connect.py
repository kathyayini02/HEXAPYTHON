import pyodbc

def db_connection():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-ICDLTP1J;"  
        "DATABASE=TicketBookingSystem;"         
        "Trusted_Connection=yes;"
    )
    try:
        conn = pyodbc.connect(conn_str)
        print("✅ Connected!")
        return conn
    except Exception as e:
        print("❌ Connection failed:", e)
        return None
