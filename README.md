# Railway Carshed Django App

Welcome to the Railway Carshed Django App! This app is designed to manage various aspects of a railway carshed, including user authentication, file input/output, data import/export, CRUD operations, Django forms, and database management. It utilizes MySQL for data storage and Bootstrap for a user-friendly interface.

## Features

- **User Authentication**: The app provides a secure user authentication system with login and registration functionality. Only authenticated users can access the app's features.

- **File Input/Output**: Users can upload files to the app, which can then be processed and utilized within the system.

- **File Import/Export**: The app supports importing and exporting data from/to files. Data can be imported from CSV files, and exported data can be saved in both CSV and PDF formats.

- **CRUD Operations**: The app supports Create, Read, Update, and Delete (CRUD) operations for managing various data related to the railway carshed.

- **Django Forms**: User-friendly forms are implemented using Django's form handling capabilities. This streamlines data input and ensures data integrity.

- **Batch Data Operations**: Users can add and update multiple data entries simultaneously, enhancing efficiency when dealing with a large dataset.

- **MySQL Database**: The app utilizes the MySQL database for storing and managing data. This provides a robust and reliable backend for the application.

- **Bootstrap Integration**: The app's frontend is designed using the Bootstrap framework, ensuring a responsive and visually appealing user interface.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/umesh537/carshed-main.git
   ```

2. Navigate to the project directory:

   ```bash
   cd carshed-main
   ```

3. Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the MySQL database settings in `settings.py`. Update the `DATABASES` dictionary with your MySQL database credentials.

5. Apply migrations to create the necessary database tables:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the app through your web browser at `http://localhost:8000/`.

8. On Command line create a superuser

```
 python3 manage.py createsuperuser
```

## Usage

1. Register an account or log in with existing credentials.

2. Explore the different features of the app, including file upload, data import/export, CRUD operations, and batch data operations.

3. Utilize the user-friendly forms provided by Django to input and manage data efficiently.

---

Thank you for choosing the Railway Carshed Django App! We hope this app enhances the efficiency and management of your railway carshed operations.
