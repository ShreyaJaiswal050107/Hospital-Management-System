# Hospital Management System

## Overview

The Hospital Management System is a Python-based application developed to manage
basic hospital activities in an organized and efficient way.

The system provides separate modules for managing patients, doctors,
appointments, billing, and reports. It uses a menu-driven interface and
provides input validation and error handling to handle invalid or incorrect
inputs.

## Features

The system provides the following major features:

### 1. Patient Management
- Add new patient records
- View all patients
- Search for a patient
- Update patient information
- Delete patient records
- Validate patient details

### 2. Doctor Management
- Add new doctor records
- View all doctors
- Search for a doctor
- Update doctor information
- Delete doctor records
- Validate doctor details

### 3. Appointment Management
- Book appointments
- View appointments
- Search for appointments
- Update appointments
- Cancel appointments
- Check whether the entered patient and doctor exist
- Validate date and time

### 4. Billing Management
- Generate patient bills
- View bills
- Search for bills
- Update bills
- Delete bills
- Calculate the total bill amount
- Validate billing amounts

### 5. Reports and Analytics
- Display hospital summary
- Generate patient reports
- Generate doctor reports
- Display appointment reports
- Display billing reports
- Calculate total revenue

## 6. Technologies Used

- Python
- Python Lists
- Functions
- Conditional Statements
- Loops
- Dictionaries/Records
- Exception Handling (`try-except`)
- Modular Programming

## 7. Project Structure

# 🏥 Hospital Management System

A simple, modular, menu-driven **Hospital Management System** developed using Python. The project manages patients, doctors, appointments, billing, and hospital reports.

---

## 📂 Project Structure

```text
Hospital-Management-System/
│
├── main.py
├── patient.py
├── doctor.py
├── appointment.py
├── billing.py
├── reports.py
├── README.md
├── statement.md
└── design_documentation.md
```

### 📄 File Description

| File | Purpose |
| ---- | ------- |
| `main.py` | Controls the main menu and overall program flow |
| `patient.py` | Handles patient management |
| `doctor.py` | Handles doctor management |
| `appointment.py` | Handles appointment management |
| `billing.py` | Handles billing operations |
| `reports.py` | Generates reports and hospital summary |
| `statement.md` | Contains the problem statement, scope, target users, and high-level features |
| `design_documentation.md` | Contains requirements, architecture, workflow, and UML design |
| `README.md` | Project documentation |

---

## ▶️ How to Run

### 1️⃣ Install Python

Make sure Python is installed on your computer.

### 2️⃣ Open the Project

Open the project folder in **Visual Studio Code**.

### 3️⃣ Open the Terminal

In VS Code, open:

**Terminal → New Terminal**

### 4️⃣ Run the Program

Execute:

```bash
python main.py
```

The Hospital Management System will start with the main menu.

---

## 🏠 Main Menu

The application provides the following main options:

```text
========== HOSPITAL MANAGEMENT SYSTEM ==========

1. Patient Management
2. Doctor Management
3. Appointment Management
4. Billing Management
5. Reports & Analytics
6. Exit
```

Users can select the required module and perform the available operations.

---

## 🔄 System Workflow

```text
Start
  ↓
Main Menu
  ↓
Choose Module
  ↓
┌─────────────────────────────┐
│ Patient Management          │
│ Doctor Management           │
│ Appointment Management      │
│ Billing Management          │
│ Reports & Analytics         │
└─────────────────────────────┘
  ↓
Perform Operation
  ↓
Validate Input
  ↓
Display Result
  ↓
Return to Main Menu
  ↓
Exit
```

---

## 🛡️ Validation & Error Handling

The system includes validation and error handling to make the application more reliable.

Some validations include:

- 🔹 Empty IDs are not accepted
- 🔹 Empty names are not accepted
- 🔹 Duplicate IDs are checked
- 🔹 Age must be a valid positive number
- 🔹 Doctor experience must be valid
- 🔹 Gender is validated
- 🔹 Patient and doctor existence is checked before appointments
- 🔹 Date and time formats are validated
- 🔹 Billing amounts must be valid numbers
- 🔹 Invalid menu choices are handled

The `try-except` mechanism is used to handle incorrect data types and prevent the program from terminating unexpectedly.

---

## 🧪 Testing

The system was tested using both valid and invalid inputs.

### Functional Testing

The following operations were successfully tested:

| Test Case | Module | Input / Action | Expected Result | Status |
| --------- | ------ | -------------- | --------------- | ------ |
| TC01 | Patient Management | Add patient with valid details | Patient is added successfully | Pass |
| TC02 | Patient Management | Enter invalid age such as `abc` | Error message is displayed | Pass |
| TC03 | Patient Management | Enter duplicate patient ID | Duplicate ID is rejected | Pass |
| TC04 | Patient Management | Search existing patient | Patient details are displayed | Pass |
| TC05 | Doctor Management | Add doctor with valid details | Doctor is added successfully | Pass |
| TC06 | Doctor Management | Enter invalid experience such as `abc` | Error message is displayed | Pass |
| TC07 | Doctor Management | Enter duplicate doctor ID | Duplicate ID is rejected | Pass |
| TC08 | Appointment Management | Book appointment with valid IDs | Appointment is booked successfully | Pass |
| TC09 | Appointment Management | Enter non-existing patient ID | Error message is displayed | Pass |
| TC10 | Appointment Management | Enter non-existing doctor ID | Error message is displayed | Pass |
| TC11 | Appointment Management | Enter invalid date/time | Error message is displayed | Pass |
| TC12 | Billing Management | Generate bill with valid charges | Bill is generated successfully | Pass |
| TC13 | Billing Management | Enter invalid billing amount | Error message is displayed | Pass |
| TC14 | Billing Management | Enter negative billing amount | Invalid amount is rejected | Pass |
| TC15 | Reports & Analytics | Generate hospital summary | Hospital summary is displayed | Pass |
| TC16 | Reports & Analytics | Generate individual reports | Required report is displayed | Pass |
| TC17 | Main Menu | Enter invalid menu choice | Error message is displayed | Pass |
| TC18 | Main Program | Press `Ctrl+C` | Program handles interruption | Pass |

### Error Testing

The following error cases were tested:

- Invalid patient age
- Invalid doctor experience
- Invalid billing amount
- Non-existing patient ID
- Non-existing doctor ID
- Invalid menu choices
- Empty input fields
- Duplicate IDs

The system displayed appropriate error messages and continued running correctly.

### Testing Summary

| Result | Count |
| ------ | ----- |
| Total Test Cases | 18 |
| Passed | 18 |
| Failed | 0 |


---

## 🚀 Future Enhancements

The project can be extended in the future with additional features such as:

- Permanent data storage using a database
- Login and user authentication
- Role-based access for hospital staff
- Medicine and pharmacy management
- Improved report generation
- Graphical User Interface (GUI)

---

## 🎓 Learning Outcomes

Through this project, the following Python concepts were applied:

- Functions
- Lists and data structures
- Conditional statements
- Loops
- Modular programming
- Input validation
- Exception handling
- Menu-driven programming
- Integration of multiple Python modules

---

## ✅ Conclusion

The Hospital Management System provides a simple and organized approach to managing essential hospital operations.

The project demonstrates how Python programming concepts can be combined to create a modular, functional, and user-friendly application.

---

## 📌 Project
**Name- Shreya Jaiswal**

**Course- Python Essentials**

**project- Hospital Management System**
