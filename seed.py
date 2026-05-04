import psycopg2
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

conn = psycopg2.connect(
    dbname="SmartCityLogistics",
    user="postgres",
    password="LA_TUA_PASSWORD",
    host="localhost",
    port="PORT"
)

cur = conn.cursor()

# -------------------------
# CREATE VEHICLES
# -------------------------
vehicle_types = ["DRONE", "VAN", "CARGO_BIKE"]

for i in range(20):
    v_type = random.choice(vehicle_types)

    cur.execute("""
        INSERT INTO Vehicle (model, km_total, created_at, vehicle_type)
        VALUES (%s, %s, %s, %s)
        RETURNING vehicle_id
    """, (
        fake.word(),
        random.randint(100, 5000),
        fake.date_between(start_date='-2y', end_date='today'),
        v_type
    ))

# -------------------------
# CREATE STAFF
# -------------------------
for i in range(5):
    cur.execute("""
        INSERT INTO Staff (name, role)
        VALUES (%s, %s)
    """, (
        fake.name(),
        random.choice(["driver", "technician"])
    ))

# -------------------------
# CREATE MISSIONS
# -------------------------
for i in range(50):
    cur.execute("""
        INSERT INTO Mission (
            vehicle_id,
            staff_id,
            start_time,
            end_time,
            distance_km,
            status
        )
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        random.randint(1, 20),
        random.randint(1, 5),
        fake.date_time_between(start_date='-3m', end_date='now'),
        fake.date_time_between(start_date='-3m', end_date='now'),
        round(random.uniform(1, 50), 2),
        random.choice(["COMPLETED", "FAILED", "CANCELLED"])
    ))

# -------------------------
# CREATE MAINTENANCE
# -------------------------
for i in range(10):
    cur.execute("""
        INSERT INTO Maintenance (
            vehicle_id,
            staff_id,
            maintenance_date,
            description
        )
        VALUES (%s,%s,%s,%s)
    """, (
        random.randint(1, 20),
        random.randint(1, 5),
        fake.date_between(start_date='-6m', end_date='today'),
        fake.sentence()
    ))

conn.commit()
cur.close()
conn.close()

print("Database popolato con successo!")