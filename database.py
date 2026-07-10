import sqlite3
conn = sqlite3.connect("cars.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
id INTEGER PRIMARY KEY, 
brand TEXT,
model TEXT,
year INTEGER,
fuel_type TEXT,
power INTEGER,
max_speed INTEGER
)
""")
conn.commit()