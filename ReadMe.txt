User Management API with Flask, SQLite, and Pytest
==================================================

Overview:
---------
This project is a simple RESTful API for user management built using Flask and SQLite. 
It includes basic CRUD operations and uses Pytest for automation testing.

Goal:
-----
✔ Build a REST API using Flask  
✔ Use SQLite as the database  
✔ Automate testing with Pytest  

Project Structure:
------------------
📁 user_management_api/  
├── app.py               # Main Flask app  
├── models.py            # Database models  
├── routes.py            # API route handlers  
├── database.db          # SQLite database  
├── tests/               # Test cases using Pytest  
│   └── test_app.py  
└── requirements.txt     # Python dependencies

Phase 1: Project Setup
----------------------
✅ Created folder structure  
✅ Set up Python virtual environment  
✅ Installed Flask and required libraries  
✅ Added a basic Flask app with one route

Getting Started:
----------------
1. Clone this repository  
2. Create and activate a virtual environment  
3. Install dependencies:
   pip install -r requirements.txt  
4. Run the app:
   python app.py  
5. Run tests:
   pytest tests/

Upcoming Phases:
----------------
🔜 Add user registration and login  
🔜 Implement CRUD operations  
🔜 Add authentication (JWT)  
🔜 Extend test coverage with edge cases

Author:
-------
Your Name  
Location: Portland, OR  
