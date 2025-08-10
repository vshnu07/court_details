import sqlite3
DATABASE = 'court_data.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            raw_response TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_query(case_type, case_number, filing_year, raw_response):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO queries (case_type, case_number, filing_year, raw_response)
        VALUES (?, ?, ?, ?)
    ''', (case_type, case_number, filing_year, raw_response))
    conn.commit()
    conn.close()
