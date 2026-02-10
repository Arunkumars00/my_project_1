# Student Management System

A comprehensive student management system built with Python and MySQL. This application allows you to perform complete CRUD (Create, Read, Update, Delete) operations on student records with a user-friendly command-line interface.

## Features

✨ **Complete CRUD Operations**
- Add new students with detailed information
- View all students in the database
- Search students by ID, name, or email
- Update existing student records
- Delete student records with confirmation
- View statistics (total students, average GPA, grade distribution)

📊 **Student Information Tracked**
- Personal details (name, email, phone)
- Academic information (grade level, GPA)
- Contact information (address)
- Date of birth and enrollment date
- Auto-generated student ID

🔒 **Data Integrity**
- Unique email validation
- Input validation for GPA and dates
- Secure database connections
- Transaction management

## Prerequisites

Before running this application, ensure you have the following installed:

1. **Python 3.7 or higher**
   - Download from: https://www.python.org/downloads/

2. **MySQL Server**
   - Download from: https://dev.mysql.com/downloads/mysql/
   - Or install via package manager:
     - Windows: Use MySQL Installer
     - macOS: `brew install mysql`
     - Linux: `sudo apt-get install mysql-server`

## Installation

### Step 1: Clone or Download the Project

Download all project files to a directory on your computer.

### Step 2: Install Python Dependencies

Open a terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install mysql-connector-python
```

### Step 3: Set Up MySQL Database

1. **Start MySQL Server**
   - Windows: Start MySQL service from Services
   - macOS: `mysql.server start`
   - Linux: `sudo service mysql start`

2. **Log in to MySQL**
   ```bash
   mysql -u root -p
   ```
   Enter your MySQL root password when prompted.

3. **Run the Database Setup Script**
   
   From MySQL prompt:
   ```sql
   source /path/to/database_setup.sql
   ```
   
   Or from terminal:
   ```bash
   mysql -u root -p < database_setup.sql
   ```

   This will:
   - Create the `student_management_db` database
   - Create the `students` table with all necessary fields
   - Insert sample student data for testing

### Step 4: Configure Database Connection

Edit the `config.py` file and update the database credentials:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',           # Your MySQL username
    'password': 'your_password',  # Your MySQL password
    'database': 'student_management_db',
    'charset': 'utf8mb4',
    'autocommit': True
}
```

## Usage

### Running the Application

From the project directory, run:

```bash
python student_management.py
```

### Main Menu Options

```
==================================================
Student Management System v1.0.0
==================================================

1. Add New Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. View Statistics
7. Exit
```

### Detailed Feature Guide

#### 1. Add New Student
- Enter student details when prompted
- Required fields: First Name, Last Name, Email
- Optional fields: Phone, Date of Birth, Grade Level, GPA, Address
- System generates a unique Student ID automatically

#### 2. View All Students
- Displays all students in the database
- Shows complete information for each student
- Students are sorted by last name, then first name

#### 3. Search Student
Choose from three search options:
- **By Student ID**: Direct lookup using student ID number
- **By Name**: Search by first or last name (partial matches supported)
- **By Email**: Search by email address (partial matches supported)

#### 4. Update Student
- Enter the Student ID you want to update
- Current values are displayed
- Press Enter to keep current value, or type new value to change
- All fields can be updated except Student ID

#### 5. Delete Student
- Enter the Student ID to delete
- System displays student details for confirmation
- Type 'yes' to confirm deletion
- Deletion is permanent and cannot be undone

#### 6. View Statistics
Displays:
- Total number of students
- Average GPA across all students
- Distribution of students by grade level

#### 7. Exit
- Safely closes database connection
- Exits the application

## Database Schema

### Students Table Structure

| Field           | Type         | Description                    |
|-----------------|--------------|--------------------------------|
| student_id      | INT          | Auto-increment primary key     |
| first_name      | VARCHAR(50)  | Student's first name           |
| last_name       | VARCHAR(50)  | Student's last name            |
| email           | VARCHAR(100) | Unique email address           |
| phone           | VARCHAR(15)  | Contact phone number           |
| date_of_birth   | DATE         | Date of birth                  |
| enrollment_date | DATE         | Date of enrollment (auto)      |
| grade_level     | VARCHAR(20)  | Grade level (e.g., 9th Grade)  |
| gpa             | DECIMAL(3,2) | Grade Point Average (0.00-4.00)|
| address         | TEXT         | Student's address              |
| created_at      | TIMESTAMP    | Record creation timestamp      |
| updated_at      | TIMESTAMP    | Last update timestamp          |

## Example Workflow

1. **Start the application**
   ```bash
   python student_management.py
   ```

2. **Add a new student** (Option 1)
   - Enter: John, Smith, john.smith@email.com, etc.
   - Student is added with a unique ID

3. **View all students** (Option 2)
   - See the new student along with sample data

4. **Search for a student** (Option 3)
   - Search by name "John" to find the student

5. **Update student information** (Option 4)
   - Change GPA, phone number, etc.

6. **View statistics** (Option 6)
   - See updated average GPA and total count

## Troubleshooting

### Connection Errors

**Error: "Access denied for user 'root'@'localhost'"**
- Solution: Check MySQL username and password in `config.py`

**Error: "Can't connect to MySQL server"**
- Solution: Ensure MySQL server is running
- Check: `mysql.server status` (macOS) or Services (Windows)

**Error: "Unknown database 'student_management_db'"**
- Solution: Run the `database_setup.sql` script to create the database

### Import Errors

**Error: "No module named 'mysql.connector'"**
- Solution: Install the MySQL connector
  ```bash
  pip install mysql-connector-python
  ```

### Data Entry Errors

**Error: "Email already exists"**
- Solution: Each student must have a unique email address

**Error: "Invalid GPA value"**
- Solution: GPA must be a number between 0.00 and 4.00

## File Structure

```
student-management-system/
│
├── student_management.py   # Main application file
├── config.py               # Database configuration
├── database_setup.sql      # Database schema and sample data
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Security Considerations

1. **Never commit config.py with real passwords** to version control
2. Create a `config.example.py` for distribution
3. Use environment variables for production deployments
4. Implement user authentication for multi-user environments
5. Regularly backup your database

## Future Enhancements

Potential features to add:
- Course enrollment tracking
- Attendance management
- Grade management system
- Export data to CSV/Excel
- GUI interface using Tkinter or PyQt
- Web interface using Flask or Django
- User authentication and authorization
- Photo uploads for students
- Parent/guardian contact information
- Email notifications

## Technical Details

- **Language**: Python 3.7+
- **Database**: MySQL 5.7+
- **Python Library**: mysql-connector-python
- **Architecture**: Object-Oriented Programming (OOP)
- **Interface**: Command Line Interface (CLI)

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify all prerequisites are installed correctly
3. Ensure database setup was completed successfully
4. Check MySQL server logs for detailed error messages

---

**Version**: 1.0.0  
**Last Updated**: February 2026

Happy Student Managing! 🎓
