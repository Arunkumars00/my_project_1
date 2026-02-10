-- Student Management System Database Setup

-- Create database
CREATE DATABASE IF NOT EXISTS student_management_db;

-- Use the database
USE student_management_db;

-- Create students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    date_of_birth DATE,
    enrollment_date DATE DEFAULT (CURRENT_DATE),
    grade_level VARCHAR(20),
    gpa DECIMAL(3,2),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create index on email for faster lookups
CREATE INDEX idx_email ON students(email);
CREATE INDEX idx_name ON students(last_name, first_name);

-- Insert sample data
INSERT INTO students (first_name, last_name, email, phone, date_of_birth, grade_level, gpa, address) VALUES
('John', 'Doe', 'john.doe@example.com', '555-0101', '2005-03-15', '10th Grade', 3.75, '123 Main St, City, State'),
('Jane', 'Smith', 'jane.smith@example.com', '555-0102', '2006-07-22', '9th Grade', 3.90, '456 Oak Ave, City, State'),
('Michael', 'Johnson', 'michael.j@example.com', '555-0103', '2005-11-08', '10th Grade', 3.50, '789 Pine Rd, City, State');
