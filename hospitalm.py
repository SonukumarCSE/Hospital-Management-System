import mysql.connector
from mysql.connector import Error
from doctor import Doctor
from patient import Patient

def book_appointment(patient, doctor, connection, scanner):
    print("Enter Patient Id: ", end='')
    patient_id = int(scanner())
    print("Enter Doctor Id: ", end='')
    doctor_id = int(scanner())
    print("Enter appointment date (YYYY-MM-DD): ", end='')
    appointment_date = scanner().strip()

    if patient.get_patient_by_id(patient_id) and doctor.get_doctor_by_id(doctor_id):
        if check_doctor_availability(doctor_id, appointment_date, connection):
            appointment_query = "INSERT INTO appointment (patient_id, doctor_id, appointment_date) VALUES (%s, %s, %s)"
            try:
                cursor = connection.cursor()
                cursor.execute(appointment_query, (patient_id, doctor_id, appointment_date))
                connection.commit()
                print("Appointment Booked!")
            except mysql.connector.Error as e:
                print("Failed to Book Appointment!")
                print(e)
        else:
            print("Doctor not available on this date!")
    else:
        print("Either doctor or patient doesn't exist!")

def check_doctor_availability(doctor_id, appointment_date, connection):
    query = "SELECT COUNT(*) FROM appointment WHERE doctor_id = %s AND appointment_date = %s"
    try:
        cursor = connection.cursor()
        cursor.execute(query, (doctor_id, appointment_date))
        count = cursor.fetchone()[0]
        return count == 0
    except mysql.connector.Error as e:
        print(e)
    return False

def create_database_if_not_exists(cursor, database_name):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

def main():
    url = "localhost"
    database = "my_new_database"
    username = "root"
    password = "1234"

    try:
        connection = mysql.connector.connect(
            host=url,
            user=username,
            password=password
        )
        cursor = connection.cursor()
        create_database_if_not_exists(cursor, database)
        connection.database = database  # Switch to the new database

        scanner = input  # Replace with appropriate input method if needed
        patient = Patient(connection, scanner)
        doctor = Doctor(connection)
        while True:
            print("HOSPITAL MANAGEMENT SYSTEM")
            print("1. Add Patient")
            print("2. View Patients")
            print("3. View Doctors")
            print("4. Book Appointment")
            print("5. Exit")
            print("Enter your choice: ", end='')
            choice = int(scanner())

            if choice == 1:
                patient.add_patient()
                print()
            elif choice == 2:
                patient.view_patients()
                print()
            elif choice == 3:
                doctor.view_doctors()
                print()
            elif choice == 4:
                book_appointment(patient, doctor, connection, scanner)
                print()
            elif choice == 5:
                print("THANK YOU! FOR USING HOSPITAL MANAGEMENT SYSTEM!!")
                break
            else:
                print("Enter a valid choice!")
    except mysql.connector.Error as e:
        print(e)
    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()
