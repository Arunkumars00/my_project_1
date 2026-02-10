"""
Student Management System
A complete system to manage student records using Python and MySQL
"""

import mysql.connector
from mysql.connector import Error
from datetime import datetime
from config import DB_CONFIG, APP_NAME, APP_VERSION
import sys


class StudentManagementSystem:
    """Main class for Student Management System"""
    
    def __init__(self):
        """Initialize database connection"""
        self.connection = None
        self.cursor = None
        self.connect_to_database()
    
    def connect_to_database(self):
        """Establish connection to MySQL database"""
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print(f"✓ Connected to MySQL Database: {DB_CONFIG['database']}\n")
        except Error as e:
            print(f"✗ Error connecting to MySQL: {e}")
            print("\nPlease ensure:")
            print("1. MySQL server is running")
            print("2. Database credentials in config.py are correct")
            print("3. Database has been created using database_setup.sql")
            sys.exit(1)
    
    def add_student(self):
        """Add a new student to the database"""
        print("\n" + "="*50)
        print("ADD NEW STUDENT")
        print("="*50)
        
        try:
            first_name = input("First Name: ").strip()
            last_name = input("Last Name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone (optional): ").strip() or None
            dob = input("Date of Birth (YYYY-MM-DD): ").strip() or None
            grade_level = input("Grade Level (e.g., 9th Grade): ").strip() or None
            gpa_input = input("GPA (0.00-4.00, optional): ").strip()
            gpa = float(gpa_input) if gpa_input else None
            address = input("Address (optional): ").strip() or None
            
            query = """
                INSERT INTO students 
                (first_name, last_name, email, phone, date_of_birth, grade_level, gpa, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (first_name, last_name, email, phone, dob, grade_level, gpa, address)
            
            self.cursor.execute(query, values)
            self.connection.commit()
            
            print(f"\n✓ Student '{first_name} {last_name}' added successfully!")
            print(f"  Student ID: {self.cursor.lastrowid}")
            
        except mysql.connector.IntegrityError as e:
            print(f"\n✗ Error: Email already exists in the database.")
        except ValueError:
            print(f"\n✗ Error: Invalid GPA value. Please enter a number.")
        except Error as e:
            print(f"\n✗ Database Error: {e}")
    
    def view_all_students(self):
        """Display all students in the database"""
        print("\n" + "="*50)
        print("ALL STUDENTS")
        print("="*50)
        
        try:
            query = "SELECT * FROM students ORDER BY last_name, first_name"
            self.cursor.execute(query)
            students = self.cursor.fetchall()
            
            if not students:
                print("\nNo students found in the database.")
                return
            
            print(f"\nTotal Students: {len(students)}\n")
            
            for student in students:
                self.display_student_details(student)
                print("-" * 50)
                
        except Error as e:
            print(f"\n✗ Database Error: {e}")
    
    def search_student(self):
        """Search for a student by ID, name, or email"""
        print("\n" + "="*50)
        print("SEARCH STUDENT")
        print("="*50)
        print("\n1. Search by Student ID")
        print("2. Search by Name")
        print("3. Search by Email")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        try:
            if choice == '1':
                student_id = input("Enter Student ID: ").strip()
                query = "SELECT * FROM students WHERE student_id = %s"
                self.cursor.execute(query, (student_id,))
            elif choice == '2':
                name = input("Enter name (first or last): ").strip()
                query = """
                    SELECT * FROM students 
                    WHERE first_name LIKE %s OR last_name LIKE %s
                """
                search_term = f"%{name}%"
                self.cursor.execute(query, (search_term, search_term))
            elif choice == '3':
                email = input("Enter email: ").strip()
                query = "SELECT * FROM students WHERE email LIKE %s"
                self.cursor.execute(query, (f"%{email}%",))
            else:
                print("\n✗ Invalid choice!")
                return
            
            students = self.cursor.fetchall()
            
            if not students:
                print("\n✗ No students found matching the search criteria.")
                return
            
            print(f"\n✓ Found {len(students)} student(s):\n")
            for student in students:
                self.display_student_details(student)
                print("-" * 50)
                
        except Error as e:
            print(f"\n✗ Database Error: {e}")
    
    def update_student(self):
        """Update student information"""
        print("\n" + "="*50)
        print("UPDATE STUDENT")
        print("="*50)
        
        try:
            student_id = input("\nEnter Student ID to update: ").strip()
            
            # Check if student exists
            query = "SELECT * FROM students WHERE student_id = %s"
            self.cursor.execute(query, (student_id,))
            student = self.cursor.fetchone()
            
            if not student:
                print(f"\n✗ No student found with ID: {student_id}")
                return
            
            print("\nCurrent Student Details:")
            self.display_student_details(student)
            
            print("\nEnter new values (press Enter to keep current value):")
            
            first_name = input(f"First Name [{student['first_name']}]: ").strip() or student['first_name']
            last_name = input(f"Last Name [{student['last_name']}]: ").strip() or student['last_name']
            email = input(f"Email [{student['email']}]: ").strip() or student['email']
            phone = input(f"Phone [{student['phone']}]: ").strip() or student['phone']
            dob = input(f"Date of Birth [{student['date_of_birth']}]: ").strip() or student['date_of_birth']
            grade_level = input(f"Grade Level [{student['grade_level']}]: ").strip() or student['grade_level']
            gpa_input = input(f"GPA [{student['gpa']}]: ").strip()
            gpa = float(gpa_input) if gpa_input else student['gpa']
            address = input(f"Address [{student['address']}]: ").strip() or student['address']
            
            update_query = """
                UPDATE students 
                SET first_name = %s, last_name = %s, email = %s, phone = %s,
                    date_of_birth = %s, grade_level = %s, gpa = %s, address = %s
                WHERE student_id = %s
            """
            values = (first_name, last_name, email, phone, dob, grade_level, gpa, address, student_id)
            
            self.cursor.execute(update_query, values)
            self.connection.commit()
            
            print(f"\n✓ Student ID {student_id} updated successfully!")
            
        except ValueError:
            print(f"\n✗ Error: Invalid GPA value.")
        except mysql.connector.IntegrityError:
            print(f"\n✗ Error: Email already exists in the database.")
        except Error as e:
            print(f"\n✗ Database Error: {e}")
    
    def delete_student(self):
        """Delete a student from the database"""
        print("\n" + "="*50)
        print("DELETE STUDENT")
        print("="*50)
        
        try:
            student_id = input("\nEnter Student ID to delete: ").strip()
            
            # Check if student exists
            query = "SELECT * FROM students WHERE student_id = %s"
            self.cursor.execute(query, (student_id,))
            student = self.cursor.fetchone()
            
            if not student:
                print(f"\n✗ No student found with ID: {student_id}")
                return
            
            print("\nStudent to be deleted:")
            self.display_student_details(student)
            
            confirm = input("\n⚠ Are you sure you want to delete this student? (yes/no): ").strip().lower()
            
            if confirm == 'yes':
                delete_query = "DELETE FROM students WHERE student_id = %s"
                self.cursor.execute(delete_query, (student_id,))
                self.connection.commit()
                print(f"\n✓ Student ID {student_id} deleted successfully!")
            else:
                print("\n✗ Deletion cancelled.")
                
        except Error as e:
            print(f"\n✗ Database Error: {e}")
    
    def display_statistics(self):
        """Display statistics about students"""
        print("\n" + "="*50)
        print("STUDENT STATISTICS")
        print("="*50)
        
        try:
            # Total students
            self.cursor.execute("SELECT COUNT(*) as total FROM students")
            total = self.cursor.fetchone()['total']
            
            # Average GPA
            self.cursor.execute("SELECT AVG(gpa) as avg_gpa FROM students WHERE gpa IS NOT NULL")
            avg_gpa = self.cursor.fetchone()['avg_gpa']
            
            # Students by grade level
            self.cursor.execute("""
                SELECT grade_level, COUNT(*) as count 
                FROM students 
                WHERE grade_level IS NOT NULL
                GROUP BY grade_level 
                ORDER BY grade_level
            """)
            grade_distribution = self.cursor.fetchall()
            
            print(f"\nTotal Students: {total}")
            print(f"Average GPA: {avg_gpa:.2f}" if avg_gpa else "Average GPA: N/A")
            
            if grade_distribution:
                print("\nStudents by Grade Level:")
                for grade in grade_distribution:
                    print(f"  {grade['grade_level']}: {grade['count']} student(s)")
            
        except Error as e:
            print(f"\n✗ Database Error: {e}")
    
    def display_student_details(self, student):
        """Helper method to display student information"""
        print(f"Student ID: {student['student_id']}")
        print(f"Name: {student['first_name']} {student['last_name']}")
        print(f"Email: {student['email']}")
        print(f"Phone: {student['phone'] or 'N/A'}")
        print(f"Date of Birth: {student['date_of_birth'] or 'N/A'}")
        print(f"Grade Level: {student['grade_level'] or 'N/A'}")
        print(f"GPA: {student['gpa'] if student['gpa'] is not None else 'N/A'}")
        print(f"Address: {student['address'] or 'N/A'}")
        print(f"Enrollment Date: {student['enrollment_date']}")
    
    def close_connection(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("\n✓ Database connection closed.")


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print(f"{APP_NAME} v{APP_VERSION}")
    print("="*50)
    print("\n1. Add New Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. View Statistics")
    print("7. Exit")
    print("\n" + "="*50)


def main():
    """Main function to run the Student Management System"""
    sms = StudentManagementSystem()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            sms.add_student()
        elif choice == '2':
            sms.view_all_students()
        elif choice == '3':
            sms.search_student()
        elif choice == '4':
            sms.update_student()
        elif choice == '5':
            sms.delete_student()
        elif choice == '6':
            sms.display_statistics()
        elif choice == '7':
            print("\nThank you for using Student Management System!")
            sms.close_connection()
            break
        else:
            print("\n✗ Invalid choice! Please enter a number between 1 and 7.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
        sys.exit(0)
