import hashlib
import secrets
import sqlite3
from typing import Optional, Dict

class AuthenticationManager:
    def __init__(self, db_path: str = 'edutrack.db'):
        """
        Initialize the authentication manager with database connection
        
        Args:
            db_path (str): Path to SQLite database
        """
        self.db_path = db_path
        self._create_database()

    def _create_database(self):
        """Create database tables if they don't exist"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Students table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    student_id TEXT PRIMARY KEY,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    salt TEXT NOT NULL,
                    name TEXT,
                    is_active BOOLEAN DEFAULT 1
                )
            ''')
            
            # Faculty table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS faculty (
                    faculty_id TEXT PRIMARY KEY,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    salt TEXT NOT NULL,
                    name TEXT,
                    is_active BOOLEAN DEFAULT 1
                )
            ''')
            
            # Institution Managers table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS institution_managers (
                    manager_id TEXT PRIMARY KEY,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    salt TEXT NOT NULL,
                    institution_id TEXT,
                    name TEXT,
                    is_active BOOLEAN DEFAULT 1
                )
            ''')
            
            conn.commit()

    def _hash_password(self, password: str, salt: str = None) -> Dict[str, str]:
        """
        Hash password with salt
        
        Args:
            password (str): Plain text password
            salt (str, optional): Salt for password hashing
        
        Returns:
            Dict containing salt and password hash
        """
        if salt is None:
            salt = secrets.token_hex(16)
        
        # Use SHA-256 for password hashing
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        
        return {
            'salt': salt,
            'password_hash': password_hash
        }

    def register_student(self, student_id: str, email: str, password: str, name: str) -> bool:
        """
        Register a new student
        
        Args:
            student_id (str): Unique student identifier
            email (str): Student email
            password (str): Password
            name (str): Student name
        
        Returns:
            bool: Registration success status
        """
        try:
            hashed_password = self._hash_password(password)
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO students 
                    (student_id, email, password_hash, salt, name) 
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    student_id, 
                    email, 
                    hashed_password['password_hash'], 
                    hashed_password['salt'],
                    name
                ))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def authenticate_student(self, email: str, password: str) -> Optional[str]:
        """
        Authenticate a student
        
        Args:
            email (str): Student email
            password (str): Password attempt
        
        Returns:
            Optional student ID if authentication successful
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT student_id, password_hash, salt FROM students WHERE email = ?', (email,))
            result = cursor.fetchone()
            
            if result:
                student_id, stored_hash, salt = result
                hashed_attempt = self._hash_password(password, salt)
                
                if hashed_attempt['password_hash'] == stored_hash:
                    return student_id
        
        return None

    # Similar methods would be implemented for faculty and institution managers
    def register_faculty(self, faculty_id: str, email: str, password: str, name: str) -> bool:
        # Implementation similar to register_student
        pass

    def authenticate_faculty(self, email: str, password: str) -> Optional[str]:
        # Implementation similar to authenticate_student
        pass

    def register_institution_manager(self, manager_id: str, email: str, password: str, institution_id: str, name: str) -> bool:
        # Implementation similar to register_student
        pass

    def authenticate_institution_manager(self, email: str, password: str) -> Optional[str]:
        # Implementation similar to authenticate_student
        pass
