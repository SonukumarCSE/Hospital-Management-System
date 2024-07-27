import mysql.connector

class Patient:
    def __init__(self, connection, scanner):
        self.connection = connection
        self.scanner = scanner

    def add_patient(self):
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        gender = input("Enter Patient Gender: ")

        try:
            query = "INSERT INTO patients (name, age, gender) VALUES (%s, %s, %s)"
            cursor = self.connection.cursor()
            cursor.execute(query, (name, age, gender))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Patient Added Successfully!!")
            else:
                print("Failed to add Patient!!")
        except mysql.connector.Error as e:
            print(e)

    def view_patients(self):
        query = "SELECT * FROM patient"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result_set = cursor.fetchall()
            print("Patient: ")
            print("+------------+--------------------+----------+------------+")
            print("| Patient Id | Name               | Age      | Gender     |")
            print("+------------+--------------------+----------+------------+")
            for row in result_set:
                patient_id, name, age, gender = row
                print(f"| {patient_id:<10} | {name:<18} | {age:<8} | {gender:<10} |")
                print("+------------+--------------------+----------+------------+")
        except mysql.connector.Error as e:
            print(e)

    def get_patient_by_id(self, patient_id):
        query = "SELECT * FROM patient WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (patient_id,))
            result_set = cursor.fetchone()
            return result_set is not None
        except mysql.connector.Error as e:
            print(e)
        return False
