
# 🎓 EduTrack v1.0

### 📚 Student Management System | Python

EduTrack is a command-line student management system developed as a personal project while studying Harvard's CS50P (Introduction to Programming with Python).

The application allows users to register students, manage grades, and generate basic academic performance reports.

Student records are stored in a CSV file, allowing data to be saved and accessed across different program sessions.

## ✨ Features

- 📝 Student Registration: Register new students with their names and grades (0–100).
- 👥 Display Students: View all registered students and the total number of students.
- 🔍 Search Students: Find students by name using a case-insensitive search.
- ✏️ Update Grades: Modify existing students' grades and save the changes.
- 📊 Performance Reports: Calculate the class average and identify students who scored above average.
- 🏆 Highest Grade: Identify a student with the highest grade.
- 📉 Lowest Grade: Identify a student with the lowest grade.
- 💾 CSV Data Storage: Save and retrieve student records between program sessions.
- 🛡️ Input Validation: Handle invalid entries and prevent grades outside the 0–100 range.

## 🛠️ Technologies Used

- 🐍 Python 3.12+
- 📂 CSV file handling using Python's built-in csv module
- 💻 Command-Line Interface (CLI)

No external Python libraries are required.

## 🚀 How to Run

### 1. Download the repository

Download the repository as a ZIP file or clone it using Git.

### 2. Check your Python version

Make sure Python 3.12 or newer is installed.

### 3. Open the project folder

Keep `edutrack1.0.py` and `grades.csv` in the same folder.

### 4. Run the application

Open a terminal in the project folder and execute:

    python edutrack1.0.py

### 5. Start using EduTrack!

Follow the interactive menu to register students, manage grades, or generate performance reports.

## 📋 Getting Started

The `grades.csv` file is initially empty and contains only the column headers: `name` and `grade`.

To get started:

1. Run the Python program.
2. Select option 1 from the main menu to register a new student.
3. Enter the student's name and grade (0–100).
4. Register a few more students to build your student database.
5. Once you have registered some students, you can explore the other features, such as searching for students, updating grades, and generating academic performance reports.

💡 Tip: Student records are automatically saved to `grades.csv`, so your data will still be available the next time you run the program. You do not need to enter the same students again.

## 📂 Project Structure

    edutrack/
    ├── edutrack1.0.py    # Main Python application
    ├── grades.csv        # Student records
    └── README.md         # Project documentation

## 🧠 What I Learned

While building EduTrack, I practiced several Python programming concepts:

- Defining and calling functions
- Working with lists and dictionaries
- Using loops and conditional statements
- Implementing input validation
- Handling exceptions with try and except
- Reading and writing CSV files
- Building an interactive menu-driven application
- Organizing a Python program into reusable functions

## 📌 Project Status

Version 1.0 — Initial Release

This is my first version of EduTrack, developed as a Python learning project during CS50P Week 6.

The current version runs entirely in the terminal and focuses on student record management and basic grade analysis.
