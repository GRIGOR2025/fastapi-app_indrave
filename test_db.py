import psycopg2
import os

os.environ['PYTHONIOENCODING'] = 'utf-8'

try:
    conn = psycopg2.connect("host=localhost dbname=drive_db user=postgres password=945146112")
    print("Связь установлена успешно!")
    conn.close()
except Exception as e:
    print(f"Oшибка: {e}")