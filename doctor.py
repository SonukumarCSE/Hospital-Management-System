import mysql.connector

class Doctor:
    def __init__(self, connection):
        self.connection = connection
    def view_doctors(self):
        query = "SELECT * FROM doctor"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result_set = cursor.fetchall()
            print("Doctors: ")
            print("+------------+--------------------+------------------+")
            print("| Doctor Id  | Name               | Specialization   |")
            print("+------------+--------------------+------------------+")
            for row in result_set:
                doctor_id, name, specialization = row
                print(f"| {doctor_id:<10} | {name:<18} | {specialization:<16} |")
                print("+------------+--------------------+------------------+")
        except mysql.connector.Error as e:
            print(e)

    def get_doctor_by_id(self, doctor_id):
        query = "SELECT * FROM doctor WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (doctor_id,))
            result_set = cursor.fetchone()
            return result_set is not None
        except mysql.connector.Error as e:
            print(e)
        return False
