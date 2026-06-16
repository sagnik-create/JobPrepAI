import sqlite3

DB_PATH = "backend/db/database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        file_path TEXT,
        uploaded_at TEXT,
        parsed_at TEXT,
        version INTEGER,
        is_active BOOLEAN
    )
""")
    #Parsed Data Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS parsed_data(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resume_id INTEGER,
        name TEXT,
        email TEXT,
        phone TEXT,
        skills TEXT,
        experience TEXT,
        education TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes (id)
    )""")
    conn.commit()
    conn.close()
