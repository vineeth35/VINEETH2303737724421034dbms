-- Create the database
CREATE DATABASE restaurant;

-- Use the created database
USE restaurant;

-- Create the staff table
CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_name VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);

-- Insert sample data
INSERT INTO staff (staff_name, position, salary) VALUES 
('John Doe', 'Manager', 50000.00),
('Jane Smith', 'Chef', 40000.00),
('Robert Brown', 'Waiter', 25000.00);

select * from staff;