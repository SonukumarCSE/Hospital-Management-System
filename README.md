
# Hospital Management System

This project is a console-based Hospital Management System built using Python and MySQL. It allows users to manage patients, doctors, and appointments in a hospital setting. The system provides functionalities to add patients, view patients, view doctors, and book appointments. 

## Table of Contents
1. [Installation](#installation)
2. [Database Setup](#database-setup)
3. [Usage](#usage)
4. [Files Overview](#files-overview)
5. [Functionality](#functionality)
6. [Future Improvements](#future-improvements)
7. [Contributing](#contributing)
8. [License](#license)

## Installation

1. **Python**: Ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/).
2. **MySQL**: Install MySQL Server and MySQL Connector for Python. You can follow [MySQL installation guide](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/) for your operating system.
3. **MySQL Connector for Python**: Install the MySQL Connector using pip:
   ```
   pip install mysql-connector-python
   ```

## Database Setup

Before running the application, you need to set up the MySQL database and tables.

1. **Create Database and Tables**:
   - Run the `db.py` script to create the database and tables.
   - This script creates a database named `my_new_database` and tables `patient`, `doctor`, and `appointment`.
   - It also inserts some initial data into these tables.

## Usage

1. **Run the Application**:
   - Execute the `hospitalm.py` script to start the application.
   - This script provides a menu-driven interface for managing patients, doctors, and appointments.

## Files Overview

### `hospitalm.py`

- **Purpose**: The main entry point of the application. It connects to the MySQL database and provides the user interface for interacting with the system.
- **Key Functions**:
  - `book_appointment`: Books an appointment for a patient with a doctor.
  - `check_doctor_availability`: Checks if a doctor is available on a given date.
  - `create_database_if_not_exists`: Ensures the database exists or creates it.
  - `main`: The main function that displays the menu and handles user input.

### `patient.py`

- **Purpose**: Manages patient-related functionalities.
- **Class `Patient`**:
  - `add_patient`: Adds a new patient to the database.
  - `view_patients`: Displays a list of all patients.
  - `get_patient_by_id`: Retrieves a patient by their ID.

### `doctor.py`

- **Purpose**: Manages doctor-related functionalities.
- **Class `Doctor`**:
  - `view_doctors`: Displays a list of all doctors.
  - `get_doctor_by_id`: Retrieves a doctor by their ID.

### `db.py`

- **Purpose**: Handles database setup, including creating the database, tables, and initial data.
- **Functions**:
  - `create_connection`: Establishes a connection to the MySQL server.
  - `create_database`: Creates the database if it does not exist.
  - `create_tables`: Creates necessary tables in the database.
  - `insert_data`: Inserts initial data into the tables.

## Functionality

1. **Add Patient**: Allows adding a new patient to the system.
2. **View Patients**: Displays all registered patients.
3. **View Doctors**: Displays all registered doctors.
4. **Book Appointment**: Schedules an appointment for a patient with a doctor, checking availability.

## Future Improvements

1. **User Authentication**: Implement a login system for doctors, patients, and admins.
2. **GUI**: Develop a graphical user interface for better user experience.
3. **Advanced Search**: Add more search and filtering options for patients and doctors.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is open-source and available under the [MIT License](LICENSE).
