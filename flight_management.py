import sqlite3

# الاتصال بقاعدة البيانات أو إنشائها إذا لم تكن موجودة
conn = sqlite3.connect('flight_management.db')
cursor = conn.cursor()

# إنشاء جدول للطائرات
cursor.execute('''
CREATE TABLE IF NOT EXISTS aircrafts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aircraft_number TEXT NOT NULL,
    model TEXT,
    capacity INTEGER,
    manufacturer TEXT
)
''')

# إنشاء جدول للرحلات
cursor.execute('''
CREATE TABLE IF NOT EXISTS flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_number TEXT NOT NULL,
    origin TEXT,
    destination TEXT,
    departure_time TEXT,
    aircraft_id INTEGER,
    FOREIGN KEY(aircraft_id) REFERENCES aircrafts(id)
)
''')

# حفظ التغييرات وإغلاق الاتصال
conn.commit()
conn.close()

print("Database and tables created successfully.")

# دالة لإضافة طائرة جديدة
def add_aircraft(aircraft_number, model, capacity, manufacturer):
    conn = sqlite3.connect('flight_management.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO aircrafts (aircraft_number, model, capacity, manufacturer)
    VALUES (?, ?, ?, ?)
    ''', (aircraft_number, model, capacity, manufacturer))
    
    conn.commit()
    conn.close()
    
    print(f"Aircraft {aircraft_number} added successfully.")

# دالة لإضافة رحلة جديدة
def add_flight(flight_number, origin, destination, departure_time, aircraft_id):
    conn = sqlite3.connect('flight_management.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO flights (flight_number, origin, destination, departure_time, aircraft_id)
    VALUES (?, ?, ?, ?, ?)
    ''', (flight_number, origin, destination, departure_time, aircraft_id))
    
    conn.commit()
    conn.close()
    
    print(f"Flight {flight_number} added successfully.")

# دالة لعرض الطائرات
def show_aircrafts():
    conn = sqlite3.connect('flight_management.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM aircrafts')
    aircrafts = cursor.fetchall()
    
    print("Aircraft List:")
    for aircraft in aircrafts:
        print(f"ID: {aircraft[0]}, Aircraft Number: {aircraft[1]}, Model: {aircraft[2]}, Capacity: {aircraft[3]}, Manufacturer: {aircraft[4]}")
    
    conn.close()

# دالة لعرض الرحلات
def show_flights():
    conn = sqlite3.connect('flight_management.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM flights')
    flights = cursor.fetchall()
    
    print("Flight List:")
    for flight in flights:
        print(f"ID: {flight[0]}, Flight Number: {flight[1]}, Origin: {flight[2]}, Destination: {flight[3]}, Departure Time: {flight[4]}, Aircraft ID: {flight[5]}")
    
    conn.close()

# دالة لحذف طائرة
def delete_aircraft(aircraft_id):
    conn = sqlite3.connect('flight_management.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM aircrafts WHERE id = ?', (aircraft_id,))
    
    conn.commit()
    conn.close()
    
    print(f"Aircraft with ID {aircraft_id} deleted successfully.")

# دالة لحذف رحلة
def delete_flight(flight_id):
    conn = sqlite3.connect('flight_management.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM flights WHERE id = ?', (flight_id,))
    
    conn.commit()
    conn.close()
    
    print(f"Flight with ID {flight_id} deleted successfully.")
