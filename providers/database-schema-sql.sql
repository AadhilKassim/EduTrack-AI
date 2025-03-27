-- Create Database
CREATE DATABASE EduTrackAI;
USE EduTrackAI;

-- Students Table
CREATE TABLE Students (
    student_id VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    institution_id VARCHAR(20),
    enrollment_date DATE,
    last_login DATETIME,
    is_active BOOLEAN DEFAULT TRUE
);

-- Faculty Table
CREATE TABLE Faculty (
    faculty_id VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    department VARCHAR(100),
    institution_id VARCHAR(20),
    hire_date DATE,
    last_login DATETIME,
    is_active BOOLEAN DEFAULT TRUE
);

-- Institution Managers Table
CREATE TABLE InstitutionManagers (
    manager_id VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    institution_id VARCHAR(20) NOT NULL,
    position VARCHAR(100),
    last_login DATETIME,
    is_active BOOLEAN DEFAULT TRUE
);

-- Institutions Table
CREATE TABLE Institutions (
    institution_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50),
    location VARCHAR(255),
    founded_year INT,
    total_students INT,
    total_faculty INT
);

-- Indexes for performance
CREATE INDEX idx_student_email ON Students(email);
CREATE INDEX idx_faculty_email ON Faculty(email);
CREATE INDEX idx_manager_email ON InstitutionManagers(email);
