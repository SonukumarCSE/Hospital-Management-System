import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection."""
    try:
        connection = mysql.connector.connect(
            user='root',
            password='1234',
            host='localhost'
        )
        if connection.is_connected():
            print("Connected to MySQL server")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_database(cursor, database_name):
    """Create a database if it does not exist."""
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    cursor.execute(f"USE {database_name}")

def create_tables(cursor):
    """Create tables in the database."""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patient (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        gender VARCHAR(10) NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctor (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        specialization VARCHAR(255) NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointment (
        id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id INT NOT NULL,
        doctor_id INT NOT NULL,
        appointment_date DATE NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patient(id),
        FOREIGN KEY (doctor_id) REFERENCES doctor(id)
    )
    """)

def insert_data(cursor):
    """Insert data into the tables."""
    # Insert data into patient table
    cursor.execute("""
    INSERT INTO patient (name, age, gender)
    VALUES
        ('John Doe', 44, 'Male'),
        ('Jane Smith', 31, 'Female'),
        ('Alice Johnson', 49, 'Female')
    """)
    
    # Insert data into doctor table
    cursor.execute("""
    INSERT INTO doctor (name, specialization)
    VALUES
        ('Emily Brown', 'Cardiology'),
        ('Michael Williams', 'Neurology'),
        ('Sarah Davis', 'Pediatrics')
    """)
    
    # Insert data into appointment table
    cursor.execute("""
    INSERT INTO appointment (patient_id, doctor_id, appointment_date)
    VALUES
        (1, 1, '2024-08-01'),
        (2, 2, '2024-08-02'),
        (3, 3, '2024-08-03')
    """)

def main():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        create_database(cursor, 'my_new_database')
        create_tables(cursor)
        insert_data(cursor)
        connection.commit()  # Commit the transactions
        print("Data inserted successfully.")
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
