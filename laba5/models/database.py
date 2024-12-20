import sqlite3
from typing import Dict, Any

class DatabaseManager:
    def __init__(self):
        self.db_name = "zhes.db"
        self.init_database()

    def init_database(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS residents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    services_cost REAL NOT NULL,
                    resident_type TEXT NOT NULL
                )
            ''')
            conn.commit()

    def add_resident(self, resident_data: Dict[str, Any]) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO residents (name, services_cost, resident_type)
                VALUES (?, ?, ?)
            ''', (
                resident_data['name'],
                resident_data['services_cost'],
                resident_data['resident_type']
            ))
            conn.commit()

    def get_all_residents(self) -> list:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM residents')
            return cursor.fetchall()

    def update_resident(self, resident_data: Dict[str, Any]) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE residents
                SET services_cost = ?, resident_type = ?
                WHERE name = ?
            ''', (
                resident_data['services_cost'],
                resident_data['resident_type'],
                resident_data['name']
            ))
            conn.commit()

    def delete_resident(self, name: str) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM residents WHERE name = ?', (name,))
            conn.commit()
