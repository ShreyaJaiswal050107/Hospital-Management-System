# Hospital Management System
# Main program
# This file connects all the hospital management modules.

from patient import (
    add_patient,
    view_patients,
    search_patient,
    update_patient,
    delete_patient
)

from doctor import (
    add_doctor,
    view_doctors,
    search_doctor,
    update_doctor,
    delete_doctor
)

from appointment import (
    book_appointment,
    view_appointments,
    search_appointment,
    update_appointment,
    cancel_appointment
)

from billing import (
    generate_bill,
    view_bills,
    search_bill,
    update_bill,
    delete_bill
)

from reports import (
    hospital_summary,
    patient_report,
    doctor_report,
    appointment_report,
    billing_report
)


def patient_menu():
    while True:
        print("\n========== PATIENT MANAGEMENT ==========")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "":
            print("Choice cannot be empty.")

        elif choice == "1":
            add_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            update_patient()

        elif choice == "5":
            delete_patient()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


def doctor_menu():
    while True:
        print("\n========== DOCTOR MANAGEMENT ==========")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Search Doctor")
        print("4. Update Doctor")
        print("5. Delete Doctor")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "":
            print("Choice cannot be empty.")

        elif choice == "1":
            add_doctor()

        elif choice == "2":
            view_doctors()

        elif choice == "3":
            search_doctor()

        elif choice == "4":
            update_doctor()

        elif choice == "5":
            delete_doctor()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


def appointment_menu():
    while True:
        print("\n========== APPOINTMENT MANAGEMENT ==========")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Search Appointment")
        print("4. Update Appointment")
        print("5. Cancel Appointment")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "":
            print("Choice cannot be empty.")

        elif choice == "1":
            book_appointment()

        elif choice == "2":
            view_appointments()

        elif choice == "3":
            search_appointment()

        elif choice == "4":
            update_appointment()

        elif choice == "5":
            cancel_appointment()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


def billing_menu():
    while True:
        print("\n========== BILLING MANAGEMENT ==========")
        print("1. Generate Bill")
        print("2. View Bills")
        print("3. Search Bill")
        print("4. Update Bill")
        print("5. Delete Bill")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "":
            print("Choice cannot be empty.")

        elif choice == "1":
            generate_bill()

        elif choice == "2":
            view_bills()

        elif choice == "3":
            search_bill()

        elif choice == "4":
            update_bill()

        elif choice == "5":
            delete_bill()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


def reports_menu():
    while True:
        print("\n========== REPORTS & ANALYTICS ==========")
        print("1. Hospital Summary")
        print("2. Patient Report")
        print("3. Doctor Report")
        print("4. Appointment Report")
        print("5. Billing Report")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "":
            print("Choice cannot be empty.")

        elif choice == "1":
            hospital_summary()

        elif choice == "2":
            patient_report()

        elif choice == "3":
            doctor_report()

        elif choice == "4":
            appointment_report()

        elif choice == "5":
            billing_report()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


def main():

    while True:
        print("\n")
        print("==============================================")
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("==============================================")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Billing Management")
        print("5. Reports & Analytics")
        print("6. Exit")
        print("==============================================")

        choice = input("Enter your choice: ").strip()

        if choice == "":
            print("Choice cannot be empty.")

        elif choice == "1":
            patient_menu()

        elif choice == "2":
            doctor_menu()

        elif choice == "3":
            appointment_menu()

        elif choice == "4":
            billing_menu()

        elif choice == "5":
            reports_menu()

        elif choice == "6":
            print("\nThank you for using the Hospital Management System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# Start the program
if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\n\nProgram stopped by user.")

    except Exception as error:
        print("\nAn unexpected error occurred.")
        print("Error:", error)

