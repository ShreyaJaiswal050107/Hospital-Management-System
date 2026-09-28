# Appointment Management Module 
# This module handles booking, viewing, searching, 
# updating and cancelling appointments.

from patient import patients
from doctor import doctors

appointments = []


def patient_exists(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return True

    return False


def doctor_exists(doctor_id):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return True

    return False


def valid_date(date):
    try:
        parts = date.split("-")

        if len(parts) != 3:
            return False

        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        if day < 1 or day > 31:
            return False

        if month < 1 or month > 12:
            return False

        if year < 2025:
            return False

        return True

    except ValueError:
        return False


def valid_time(time):
    try:
        parts = time.split(":")

        if len(parts) != 2:
            return False

        hour = int(parts[0])
        minute = int(parts[1])

        if hour < 0 or hour > 23:
            return False

        if minute < 0 or minute > 59:
            return False

        return True

    except ValueError:
        return False


def book_appointment():
    print("\n--- Book New Appointment ---")

    # Appointment ID
    while True:
        appointment_id = input(
            "Enter appointment ID: "
        ).strip()

        if appointment_id == "":
            print("Appointment ID cannot be empty.")
            continue

        duplicate = False

        for appointment in appointments:
            if appointment["id"] == appointment_id:
                duplicate = True
                break

        if duplicate:
            print("Appointment ID already exists.")
        else:
            break

    # Patient ID
    while True:
        patient_id = input(
            "Enter patient ID: "
        ).strip()

        if patient_id == "":
            print("Patient ID cannot be empty.")

        elif not patient_exists(patient_id):
            print("Patient ID not found. Please add the patient first.")

        else:
            break

    # Doctor ID
    while True:
        doctor_id = input(
            "Enter doctor ID: "
        ).strip()

        if doctor_id == "":
            print("Doctor ID cannot be empty.")

        elif not doctor_exists(doctor_id):
            print("Doctor ID not found. Please add the doctor first.")

        else:
            break

    # Date
    while True:
        date = input(
            "Enter appointment date (DD-MM-YYYY): "
        ).strip()

        if date == "":
            print("Date cannot be empty.")

        elif not valid_date(date):
            print("Please enter a valid date in DD-MM-YYYY format.")

        else:
            break

    # Time
    while True:
        time = input(
            "Enter appointment time (HH:MM): "
        ).strip()

        if time == "":
            print("Time cannot be empty.")

        elif not valid_time(time):
            print("Please enter a valid time in HH:MM format.")

        else:
            break

    # Reason
    while True:
        reason = input(
            "Enter reason for visit: "
        ).strip()

        if reason == "":
            print("Reason cannot be empty.")
        else:
            break

    appointment = {
        "id": appointment_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time,
        "reason": reason
    }

    appointments.append(appointment)

    print("Appointment booked successfully.")


def view_appointments():
    print("\n--- Appointment Records ---")

    if len(appointments) == 0:
        print("No appointments found.")
        return

    for appointment in appointments:
        print("\nAppointment ID :", appointment["id"])
        print("Patient ID     :", appointment["patient_id"])
        print("Doctor ID      :", appointment["doctor_id"])
        print("Date           :", appointment["date"])
        print("Time           :", appointment["time"])
        print("Reason         :", appointment["reason"])


def search_appointment():
    print("\n--- Search Appointment ---")

    appointment_id = input(
        "Enter appointment ID to search: "
    ).strip()

    if appointment_id == "":
        print("Appointment ID cannot be empty.")
        return

    for appointment in appointments:

        if appointment["id"] == appointment_id:
            print("\nAppointment Found!")
            print("Appointment ID :", appointment["id"])
            print("Patient ID     :", appointment["patient_id"])
            print("Doctor ID      :", appointment["doctor_id"])
            print("Date           :", appointment["date"])
            print("Time           :", appointment["time"])
            print("Reason         :", appointment["reason"])
            return

    print("Appointment not found.")


def update_appointment():
    print("\n--- Update Appointment ---")

    appointment_id = input(
        "Enter appointment ID to update: "
    ).strip()

    if appointment_id == "":
        print("Appointment ID cannot be empty.")
        return

    for appointment in appointments:

        if appointment["id"] == appointment_id:

            print("\nCurrent appointment details:")
            print("Patient ID :", appointment["patient_id"])
            print("Doctor ID  :", appointment["doctor_id"])
            print("Date       :", appointment["date"])
            print("Time       :", appointment["time"])
            print("Reason     :", appointment["reason"])

            print("\nEnter new details:")

            # New patient ID
            while True:
                patient_id = input(
                    "Enter new patient ID: "
                ).strip()

                if patient_id == "":
                    print("Patient ID cannot be empty.")

                elif not patient_exists(patient_id):
                    print("Patient ID not found.")

                else:
                    break

            # New doctor ID
            while True:
                doctor_id = input(
                    "Enter new doctor ID: "
                ).strip()

                if doctor_id == "":
                    print("Doctor ID cannot be empty.")

                elif not doctor_exists(doctor_id):
                    print("Doctor ID not found.")

                else:
                    break

            # New date
            while True:
                date = input(
                    "Enter new date (DD-MM-YYYY): "
                ).strip()

                if date == "":
                    print("Date cannot be empty.")

                elif not valid_date(date):
                    print("Please enter a valid date.")

                else:
                    break

            # New time
            while True:
                time = input(
                    "Enter new time (HH:MM): "
                ).strip()

                if time == "":
                    print("Time cannot be empty.")

                elif not valid_time(time):
                    print("Please enter a valid time.")

                else:
                    break

            # New reason
            while True:
                reason = input(
                    "Enter new reason: "
                ).strip()

                if reason == "":
                    print("Reason cannot be empty.")

                else:
                    break

            appointment["patient_id"] = patient_id
            appointment["doctor_id"] = doctor_id
            appointment["date"] = date
            appointment["time"] = time
            appointment["reason"] = reason

            print("Appointment updated successfully.")
            return

    print("Appointment not found.")


def cancel_appointment():
    print("\n--- Cancel Appointment ---")

    appointment_id = input(
        "Enter appointment ID to cancel: "
    ).strip()

    if appointment_id == "":
        print("Appointment ID cannot be empty.")
        return

    for appointment in appointments:

        if appointment["id"] == appointment_id:
            appointments.remove(appointment)

            print("Appointment cancelled successfully.")
            return

    print("Appointment not found.")

