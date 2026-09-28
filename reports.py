# Reports and Analytics Module 
# This module generates simple reports using 
# patient, doctor, appointment and billing data.

from patient import patients
from doctor import doctors
from appointment import appointments
from billing import bills


def hospital_summary():
    print("\n========== HOSPITAL SUMMARY ==========")

    try:
        total_patients = len(patients)
        total_doctors = len(doctors)
        total_appointments = len(appointments)
        total_bills = len(bills)

        total_revenue = 0

        for bill in bills:
            total_revenue = total_revenue + bill["total"]

        print("Total Patients      :", total_patients)
        print("Total Doctors       :", total_doctors)
        print("Total Appointments  :", total_appointments)
        print("Total Bills         :", total_bills)
        print("Total Revenue       : ₹", total_revenue)

    except (KeyError, TypeError):
        print("Unable to generate hospital summary.")


def patient_report():
    print("\n========== PATIENT REPORT ==========")

    if len(patients) == 0:
        print("No patient records available.")
        return

    try:
        for patient in patients:
            print(
                patient["id"],
                "|",
                patient["name"],
                "| Age:", patient["age"],
                "| Gender:", patient["gender"],
                "| Disease:", patient["disease"]
            )

    except KeyError:
        print("Unable to display patient report.")


def doctor_report():
    print("\n========== DOCTOR REPORT ==========")

    if len(doctors) == 0:
        print("No doctor records available.")
        return

    try:
        for doctor in doctors:
            print(
                doctor["id"],
                "|",
                doctor["name"],
                "|",
                doctor["specialization"],
                "| Department:", doctor["department"],
                "| Experience:",
                doctor["experience"],
                "years"
            )

    except KeyError:
        print("Unable to display doctor report.")


def appointment_report():
    print("\n========== APPOINTMENT REPORT ==========")

    if len(appointments) == 0:
        print("No appointment records available.")
        return

    try:
        for appointment in appointments:
            print(
                appointment["id"],
                "| Patient:", appointment["patient_id"],
                "| Doctor:", appointment["doctor_id"],
                "| Date:", appointment["date"],
                "| Time:", appointment["time"]
            )

    except KeyError:
        print("Unable to display appointment report.")


def billing_report():
    print("\n========== BILLING REPORT ==========")

    if len(bills) == 0:
        print("No billing records available.")
        return

    try:
        total_revenue = 0

        for bill in bills:
            print(
                bill["id"],
                "| Patient:", bill["patient_id"],
                "| Total: ₹", bill["total"]
            )

            total_revenue = total_revenue + bill["total"]

        print("\nTotal Revenue: ₹", total_revenue)

    except (KeyError, TypeError):
        print("Unable to generate billing report.")

