# Design Documentation

## 1. Problem Statement

Managing hospital information manually can make it difficult to organize
patient records, doctor information, appointments, and billing details.

The Hospital Management System is developed to provide a simple,
menu-driven Python application that helps manage these basic hospital
operations in an organized manner.

The system brings different hospital management activities together into
separate modules and provides validation and error handling to reduce
incorrect data entry.




## 2. Objectives

1. To develop a simple and organized system for managing basic hospital
   operations.

2. To manage patient information such as patient ID, name, age, gender,
   and disease.

3. To manage doctor information such as doctor ID, name, specialization,
   department, and experience.

4. To provide an organized way to book, view, search, update, and cancel
   appointments.

5. To manage patient billing and calculate the total bill amount.

6. To generate useful reports related to patients, doctors, appointments,
   and billing.

7. To reduce incorrect data entry by implementing input validation.

8. To handle invalid inputs and incorrect data types using exception
   handling.

9. To divide the system into separate Python modules so that the code is
   easier to understand, maintain, test, and modify.

10. To demonstrate the practical application of Python programming concepts
    such as functions, lists, conditional statements, loops, modular
    programming, and exception handling.





## 3. Functional Requirements

The Hospital Management System shall provide the following functional
requirements:

### 3.1 Patient Management

The system shall:

- Allow the user to add a new patient.
- Store patient details such as patient ID, name, age, gender, and disease.
- Display all patient records.
- Search for a patient using the patient ID.
- Update existing patient information.
- Delete a patient record.
- Prevent duplicate patient IDs.
- Validate patient information before adding or updating a record.

### 3.2 Doctor Management

The system shall:

- Allow the user to add a new doctor.
- Store doctor details such as doctor ID, name, specialization, department,
  and experience.
- Display all doctor records.
- Search for a doctor using the doctor ID.
- Update existing doctor information.
- Delete a doctor record.
- Prevent duplicate doctor IDs.
- Validate doctor information before adding or updating a record.

### 3.3 Appointment Management

The system shall:

- Allow the user to book an appointment.
- Store appointment ID, patient ID, doctor ID, date, time, and reason.
- Display all appointments.
- Search for an appointment using the appointment ID.
- Update appointment details.
- Cancel an appointment.
- Check whether the entered patient exists before booking an appointment.
- Check whether the entered doctor exists before booking an appointment.
- Validate the appointment date and time.
- Prevent duplicate appointment IDs.

### 3.4 Billing Management

The system shall:

- Allow the user to generate a bill for a patient.
- Store bill ID and patient ID.
- Record consultation, room, medicine, and other charges.
- Calculate the total bill amount.
- Display all bills.
- Search for a bill using the bill ID.
- Update billing information.
- Delete a bill.
- Validate billing amounts.
- Prevent duplicate bill IDs.

### 3.5 Reports and Analytics

The system shall:

- Display a summary of the hospital records.
- Display the total number of patients.
- Display the total number of doctors.
- Display the total number of appointments.
- Display the total number of bills.
- Calculate and display total revenue.
- Generate patient reports.
- Generate doctor reports.
- Generate appointment reports.
- Generate billing reports.

### 3.6 Input Validation and Error Handling

The system shall:

- Validate required input fields.
- Reject invalid or empty IDs and names.
- Validate numeric inputs such as age, experience, and billing amounts.
- Handle incorrect data types using exception handling.
- Display appropriate error messages for invalid inputs.
- Handle invalid menu choices without terminating the program.




## 4. Non-Functional Requirements

The Hospital Management System shall satisfy the following non-functional
requirements:

### 4.1 Usability

- The system shall provide a simple menu-driven interface.
- The options shall be clearly displayed to the user.
- Error messages shall be understandable and helpful.
- The system shall be easy to use for basic hospital record management.

### 4.2 Reliability

- The system shall handle invalid inputs without unexpectedly terminating.
- The system shall use exception handling for incorrect data types.
- The system shall validate important information before performing
  operations.
- The system shall maintain consistent records during program execution.

### 4.3 Performance

- The system shall respond quickly to normal user operations.
- Searching and displaying records shall be performed efficiently for the
  intended project scale.
- The system shall avoid unnecessary processing during normal operations.

### 4.4 Maintainability

- The system shall be divided into separate Python modules.
- Each module shall handle a specific area of hospital management.
- Functions shall be used to organize repeated or related operations.
- The code shall be structured so that individual modules can be modified
  without unnecessarily affecting other modules.

### 4.5 Error Handling

- The system shall validate user inputs before processing them.
- Incorrect data types shall be handled using `try-except`.
- Invalid menu choices shall display an appropriate message.
- Missing or invalid records shall be handled without crashing the program.

### 4.6 Resource Efficiency

- The system shall use Python lists and basic data structures to manage
  records during program execution.
- The system shall avoid unnecessary use of system resources.



## 5. System Architecture

The Hospital Management System follows a simple modular architecture.
The system is divided into separate Python modules, where each module is
responsible for a specific functional area. The `main.py` file acts as the
main controller and provides access to all modules.

### 5.1 Architecture Components

The system consists of the following components:

1. **Main Controller – `main.py`**
   - Controls the overall program flow.
   - Displays the main menu.
   - Accepts user choices.
   - Connects the different functional modules.

2. **Patient Management – `patient.py`**
   - Manages patient records.
   - Provides add, view, search, update, and delete operations.
   - Performs patient input validation.

3. **Doctor Management – `doctor.py`**
   - Manages doctor records.
   - Provides add, view, search, update, and delete operations.
   - Performs doctor input validation.

4. **Appointment Management – `appointment.py`**
   - Handles appointment booking, viewing, searching, updating, and
     cancellation.
   - Checks whether the selected patient and doctor exist.
   - Validates appointment date and time.

5. **Billing Management – `billing.py`**
   - Handles creation, viewing, searching, updating, and deletion of bills.
   - Validates billing amounts.
   - Calculates the total bill amount.

6. **Reports and Analytics – `reports.py`**
   - Generates patient, doctor, appointment, and billing reports.
   - Provides an overall hospital summary.
   - Calculates total revenue.

### 5.2 System Architecture Diagram

```text
                    ┌─────────────────────────┐
                    │        main.py          │
                    │    Main Controller      │
                    │                         │
                    │  • Main Menu            │
                    │  • User Input           │
                    │  • Module Selection     │
                    └────────────┬────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
          ▼                      ▼                      ▼
 ┌─────────────────┐    ┌─────────────────┐    ┌────────────────────┐
 │   patient.py    │    │    doctor.py    │    │  appointment.py    │
 │                 │    │                 │    │                    │
 │ Patient         │    │ Doctor          │    │ Appointment         │
 │ Management      │    │ Management      │    │ Management          │
 └────────┬────────┘    └────────┬────────┘    └─────────┬──────────┘
          │                      │                       │
          │                      │              ┌────────┴────────┐
          │                      │              │                 │
          │                      │              ▼                 ▼
          │                      │       Patient Check      Doctor Check
          │                      │
          └──────────────┬───────┴──────────────────────────────┐
                         │                                      │
                         ▼                                      ▼
                ┌─────────────────┐                    ┌─────────────────┐
                │   billing.py    │                    │   reports.py    │
                │                 │                    │                 │
                │ Billing         │                    │ Reports &       │
                │ Management      │                    │ Analytics       │
                └────────┬────────┘                    └─────────────────┘
                         │
                         ▼
                  Patient Validation


### 5.3 Module Dependencies

The modules have the following dependencies:

main.py
   │
   ├──→ patient.py
   ├──→ doctor.py
   ├──→ appointment.py
   ├──→ billing.py
   └──→ reports.py

appointment.py
   ├──→ patient.py
   └──→ doctor.py

billing.py
   └──→ patient.py

reports.py
   ├──→ patient.py
   ├──→ doctor.py
   ├──→ appointment.py
   └──→ billing.py


### 5.4 **Data Flow**

The basic data flow of the system is:

User
  ↓
main.py
  ↓
Select Required Module
  ↓
Enter Information
  ↓
Input Validation
  ↓
Relevant Module
  ↓
Perform Operation
  ↓
Update / Read Records
  ↓
Display Result
  ↓
Return to Main Menu

The current implementation stores records using Python data structures
during program execution. A permanent database is not used in the current
version.


Now **5.1, 5.2, 5.3, and 5.4 are all consistently bold**.
give all this at once so that i can copy it at once

Absolutely. Here is the entire Section 5 in one block so you can copy-paste it directly into your design_documentation.md.

## 5. System Architecture

The Hospital Management System follows a simple modular architecture.
The system is divided into separate Python modules, where each module is
responsible for a specific functional area. The `main.py` file acts as the
main controller and provides access to all modules.

### **5.1 Architecture Components**

The system consists of the following components:

1. **Main Controller – `main.py`**
   - Controls the overall program flow.
   - Displays the main menu.
   - Accepts user choices.
   - Connects the different functional modules.

2. **Patient Management – `patient.py`**
   - Manages patient records.
   - Provides add, view, search, update, and delete operations.
   - Performs patient input validation.

3. **Doctor Management – `doctor.py`**
   - Manages doctor records.
   - Provides add, view, search, update, and delete operations.
   - Performs doctor input validation.

4. **Appointment Management – `appointment.py`**
   - Handles appointment booking, viewing, searching, updating, and
     cancellation.
   - Checks whether the selected patient and doctor exist.
   - Validates appointment date and time.

5. **Billing Management – `billing.py`**
   - Handles creation, viewing, searching, updating, and deletion of bills.
   - Validates billing amounts.
   - Calculates the total bill amount.

6. **Reports and Analytics – `reports.py`**
   - Generates patient, doctor, appointment, and billing reports.
   - Provides an overall hospital summary.
   - Calculates total revenue.

### **5.2 System Architecture Diagram**

```text
                    ┌─────────────────────────┐
                    │        main.py          │
                    │    Main Controller      │
                    │                         │
                    │  • Main Menu            │
                    │  • User Input           │
                    │  • Module Selection     │
                    └────────────┬────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
          ▼                      ▼                      ▼
 ┌─────────────────┐    ┌─────────────────┐    ┌────────────────────┐
 │   patient.py    │    │    doctor.py    │    │  appointment.py    │
 │                 │    │                 │    │                    │
 │ Patient         │    │ Doctor          │    │ Appointment        │
 │ Management      │    │ Management      │    │ Management         │
 └────────┬────────┘    └────────┬────────┘    └─────────┬──────────┘
          │                      │                       │
          │                      │              ┌────────┴────────┐
          │                      │              │                 │
          │                      │              ▼                 ▼
          │                      │       Patient Check      Doctor Check
          │                      │
          └──────────────┬───────┴──────────────────────────────┐
                         │                                      │
                         ▼                                      ▼
                ┌─────────────────┐                    ┌─────────────────┐
                │   billing.py    │                    │   reports.py    │
                │                 │                    │                 │
                │ Billing         │                    │ Reports &       │
                │ Management      │                    │ Analytics       │
                └────────┬────────┘                    └─────────────────┘
                         │
                         ▼
                  Patient Validation

### 5.3 Module Dependencies

The modules have the following dependencies:

main.py
   │
   ├──→ patient.py
   ├──→ doctor.py
   ├──→ appointment.py
   ├──→ billing.py
   └──→ reports.py

appointment.py
   ├──→ patient.py
   └──→ doctor.py

billing.py
   └──→ patient.py

reports.py
   ├──→ patient.py
   ├──→ doctor.py
   ├──→ appointment.py
   └──→ billing.py

### 5.4 Data Flow

The basic data flow of the system is:

User
  ↓
main.py
  ↓
Select Required Module
  ↓
Enter Information
  ↓
Input Validation
  ↓
Relevant Module
  ↓
Perform Operation
  ↓
Update / Read Records
  ↓
Display Result
  ↓
Return to Main Menu

## 6. Process / Workflow Diagram

The workflow of the Hospital Management System describes how the user interacts with the system from starting the application to completing different hospital management operations.

### 6.1 Overall Workflow

                    ┌───────────────┐
                    │     START     │
                    └───────┬───────┘
                            ↓
                 ┌─────────────────────┐
                 │     Main Menu       │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │   Select Module     │
                 └──────────┬──────────┘
                            ↓
        ┌───────────────────┼────────────────────┐
        ↓                   ↓                    ↓
 ┌─────────────┐     ┌─────────────┐     ┌──────────────┐
 │   Patient   │     │   Doctor    │     │ Appointment  │
 │ Management  │     │ Management  │     │ Management   │
 └──────┬──────┘     └──────┬──────┘     └──────┬───────┘
        │                   │                    │
        └───────────────────┼────────────────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Billing / Reports   │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │   Validate Input    │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │  Perform Operation  │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │   Display Result    │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Return to Main      │
                 │ Menu?               │
                 └───────┬─────┬───────┘
                         │     │
                      Yes│     │No
                         ↓     ↓
                   Main Menu  EXIT


### 6.2 Module-Level Workflow

Each management module follows a basic workflow:

```text
Start
  ↓
Select Module
  ↓
Select Operation
  ↓
Enter Required Information
  ↓
Validate Input
  ↓
Is Input Valid?
  │
  ├── No → Display Error Message
  │          ↓
  │      Enter Again
  │
  └── Yes
       ↓
   Perform Operation
       ↓
   Display Result
       ↓
   Return to Module Menu
```

### 6.3 Appointment Workflow

The appointment module has additional validation because a patient and doctor must already exist.

```text
Enter Appointment Details
          ↓
    Validate Input
          ↓
     Check Patient ID
          ↓
    Patient Exists?
       │         │
      No        Yes
       ↓         ↓
    Display    Check Doctor ID
    Error           ↓
                Doctor Exists?
                 │         │
                No        Yes
                 ↓         ↓
              Display    Create
              Error    Appointment
                           ↓
                     Display Result
```

### 6.4 Billing Workflow

```text
Enter Billing Details
        ↓
Check Patient ID
        ↓
Validate Charges
        ↓
Calculate Total Amount
        ↓
Create / Update Bill
        ↓
Display Bill
```

The workflow ensures that user input is validated before the requested operation is performed.

---

## 7. UML Use Case Diagram

The Use Case Diagram represents the interaction between the user and the different functions provided by the Hospital Management System.

### 7.1 Actors

The primary actor of the system is:

- **User** – interacts with the system to manage patients, doctors, appointments, billing, and reports.

### 7.2 Use Cases

The user can perform the following operations:

- Manage Patients
- Manage Doctors
- Manage Appointments
- Manage Billing
- Generate Reports
- View Hospital Summary

### 7.3 Use Case Representation

                         UML USE CASE DIAGRAM
                    HOSPITAL MANAGEMENT SYSTEM


              ┌─────────────────────────────────────────────┐
              │       HOSPITAL MANAGEMENT SYSTEM            │
              │                                             │
              │   ( Manage Patients )                       │
              │                                             │
              │   ( Manage Doctors )                        │
              │                                             │
              │   ( Manage Appointments )                   │
              │                                             │
              │   ( Manage Billing )                        │
              │                                             │
              │   ( Generate Reports )                      │
              │                                             │
              │   ( View Hospital Summary )                 │
              │                                             │
              └─────────────────────────────────────────────┘
                         ↑      ↑      ↑      ↑
                         │      │      │      │
                         │      │      │      │
                    ┌────┴──────┴──────┴──────┴────┐
                    │              USER             │
                    │               O               │
                    │              /|\              │
                    │              / \              │
                    └───────────────────────────────┘

### 7.4 Use Case Details

| Use Case | Description |
| -------- | ----------- |
| **Manage Patients** | Add, view, search, update, and delete patient records |
| **Manage Doctors** | Add, view, search, update, and delete doctor records |
| **Manage Appointments** | Book, view, search, update, and cancel appointments |
| **Manage Billing** | Create, view, search, update, and delete bills |
| **Generate Reports** | Generate patient, doctor, appointment, and billing reports |
| **View Hospital Summary** | View the overall number of records and total revenue |

---

## 8. UML Class / Component Diagram

The project uses separate Python modules for different functional areas. The component-style representation below shows the main modules and their relationships.

### 8.1 Component Representation

```text
                  UML CLASS / COMPONENT DIAGRAM
                   HOSPITAL MANAGEMENT SYSTEM


                         ┌─────────────────┐
                         │     main.py     │
                         │ Main Controller │
                         └────────┬────────┘
                                  │
          ┌───────────────────────┼────────────────────────┐
          │                       │                        │
          ↓                       ↓                        ↓
 ┌─────────────────┐     ┌─────────────────┐      ┌─────────────────────┐
 │   patient.py    │     │    doctor.py    │      │  appointment.py     │
 │                 │     │                 │      │                     │
 │ Patient Mgmt.   │     │ Doctor Mgmt.    │      │ Appointment Mgmt.   │
 │                 │     │                 │      │                     │
 │ • Add Patient   │     │ • Add Doctor    │      │ • Book Appointment  │
 │ • View Patient  │     │ • View Doctor   │      │ • View Appointment  │
 │ • Search        │     │ • Search        │      │ • Search            │
 │ • Update        │     │ • Update        │      │ • Update            │
 │ • Delete        │     │ • Delete        │      │ • Cancel            │
 └────────┬────────┘     └────────┬────────┘      └──────────┬──────────┘
          │                       │                          │
          └───────────────────────┼──────────────────────────┘
                                  │
                                  ↓
                        ┌───────────────────┐
                        │    billing.py     │
                        │                   │
                        │   Billing Mgmt.   │
                        │                   │
                        │ • Generate Bill   │
                        │ • View Bill       │
                        │ • Search Bill     │
                        │ • Update Bill     │
                        │ • Delete Bill     │
                        └─────────┬─────────┘
                                  │
                                  ↓
                        ┌───────────────────┐
                        │    reports.py     │
                        │                   │
                        │ Reports &         │
                        │ Analytics         │
                        │                   │
                        │ • Patient Report  │
                        │ • Doctor Report   │
                        │ • Appointment     │
                        │   Report          │
                        │ • Billing Report  │
                        │ • Hospital        │
                        │   Summary         │
                        └───────────────────┘
```

### 8.2 Module Dependencies

```text
main.py
   │
   ├──→ patient.py
   ├──→ doctor.py
   ├──→ appointment.py
   ├──→ billing.py
   └──→ reports.py

appointment.py ──→ patient.py
appointment.py ──→ doctor.py

billing.py ──────→ patient.py

reports.py ──────→ patient.py
reports.py ──────→ doctor.py
reports.py ──────→ appointment.py
reports.py ──────→ billing.py
```

The dependencies show how the different modules communicate with each other. For example, the appointment module checks patient and doctor records before creating an appointment, while the reports module uses information from all major modules.

---

## 9. UML Sequence Diagram

The sequence diagram shows the interaction between the user, the main program, and the relevant modules when an appointment is booked.

### 9.1 Appointment Booking Sequence

```text
                UML SEQUENCE DIAGRAM
          APPOINTMENT BOOKING PROCESS


 User          main.py       appointment.py     patient.py     doctor.py
  │               │                │                │              │
  │──Select──────>│                │                │              │
  │ Appointment   │                │                │              │
  │ Management    │                │                │              │
  │               │                │                │              │
  │──Book────────>│                │                │              │
  │ Appointment   │                │                │              │
  │               │──Request──────>│                │              │
  │               │   Details      │                │              │
  │               │                │                │              │
  │               │                │──Check Patient>│              │
  │               │                │                │              │
  │               │                │<─Patient Found─│              │
  │               │                │                │              │
  │               │                │──Check Doctor────────────────>│
  │               │                │                               │
  │               │                │<────────Doctor Found─────────│
  │               │                │                               │
  │               │                │──Create Appointment           │
  │               │                │                               │
  │               │<──Result───────│                               │
  │               │                │                               │
  │<──Display─────│                │                               │
  │   Result      │                │                               │
  │               │                │                               │
```

The sequence demonstrates how the system checks the required patient and doctor records before creating an appointment.

---

## 10. Design Summary

### 10.1 Modular Programming

The system is divided into separate Python modules such as `patient.py`,
`doctor.py`, `appointment.py`, `billing.py`, and `reports.py`.

This decision was made to keep each functional area organized and easier
to understand, test, maintain, and modify.

### 10.2 Menu-Driven Interface

A menu-driven interface was selected because it provides a simple way for
the user to access different hospital management operations without
requiring a graphical interface.

The main menu provides direct access to patient management, doctor
management, appointment management, billing, and reports.

### 10.3 Lists and Basic Data Structures**

Python lists and basic data structures are used to store records during
program execution.

This approach keeps the implementation simple and suitable for the current
project scope while demonstrating Python data structures.

### 10.4 Input Validation

Input validation was included to reduce incorrect data entry.

The system validates information such as IDs, names, age, doctor
experience, gender, appointment date/time, and billing amounts.

The system also checks whether required patient and doctor records exist
before an appointment is created.

### 10.5 Exception Handling

`try-except` blocks are used where incorrect data types may be entered.

This prevents the program from terminating unexpectedly and allows the
system to display an appropriate error message.

### 10.6 Separate Reports Module

A separate `reports.py` module was created to keep reporting operations
independent from patient, doctor, appointment, and billing management.

This keeps the project organized and makes reporting functionality easier
to maintain.

### 10.7 No Permanent Database in Current Version

The current version uses Python data structures during program execution
instead of a permanent database.

This decision keeps the project within its current scope and focuses on
demonstrating Python programming, modular programming, validation, and
exception handling.

Permanent database storage can be considered as a future enhancement.

### 10.8 Simple Console-Based Interface

A console-based interface was selected to keep the implementation focused
on the core hospital management functionality.

A graphical user interface can be added as a future enhancement.
