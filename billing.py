# Billing Management Module 
# This module handles creating, viewing, searching, 
# updating and deleting hospital bills.


from patient import patients

bills = []


def patient_exists(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return True

    return False


def get_charge(message):
    # Take a valid charge from the user

    while True:
        try:
            amount = float(input(message))

            if amount < 0:
                print("Charge cannot be negative.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid amount.")


def generate_bill():
    print("\n--- Generate Hospital Bill ---")

    # Bill ID
    while True:
        bill_id = input("Enter bill ID: ").strip()

        if bill_id == "":
            print("Bill ID cannot be empty.")
            continue

        # Check duplicate Bill ID
        duplicate = False

        for bill in bills:
            if bill["id"] == bill_id:
                duplicate = True
                break

        if duplicate:
            print("Bill ID already exists. Enter another ID.")
        else:
            break

    # Patient ID
    while True:
        patient_id = input("Enter patient ID: ").strip()

        if patient_id == "":
            print("Patient ID cannot be empty.")

        elif not patient_exists(patient_id):
            print("Patient ID not found. Please add the patient first.")

        else:
            break

    # Charges
    consultation = get_charge(
        "Enter consultation charge: ₹"
    )

    room = get_charge(
        "Enter room charge: ₹"
    )

    medicine = get_charge(
        "Enter medicine charge: ₹"
    )

    other = get_charge(
        "Enter other charges: ₹"
    )

    # Calculate total
    total = consultation + room + medicine + other

    bill = {
        "id": bill_id,
        "patient_id": patient_id,
        "consultation": consultation,
        "room": room,
        "medicine": medicine,
        "other": other,
        "total": total
    }

    bills.append(bill)

    print("\nBill generated successfully.")
    print("Total Amount: ₹", total)


def view_bills():
    print("\n--- Hospital Bills ---")

    if len(bills) == 0:
        print("No bills found.")
        return

    for bill in bills:
        print("\nBill ID       :", bill["id"])
        print("Patient ID    :", bill["patient_id"])
        print("Consultation  : ₹", bill["consultation"])
        print("Room Charges  : ₹", bill["room"])
        print("Medicine      : ₹", bill["medicine"])
        print("Other Charges : ₹", bill["other"])
        print("Total Amount  : ₹", bill["total"])


def search_bill():
    print("\n--- Search Bill ---")

    bill_id = input(
        "Enter bill ID to search: "
    ).strip()

    if bill_id == "":
        print("Bill ID cannot be empty.")
        return

    for bill in bills:

        if bill["id"] == bill_id:
            print("\nBill Found!")
            print("Bill ID       :", bill["id"])
            print("Patient ID    :", bill["patient_id"])
            print("Consultation  : ₹", bill["consultation"])
            print("Room Charges  : ₹", bill["room"])
            print("Medicine      : ₹", bill["medicine"])
            print("Other Charges : ₹", bill["other"])
            print("Total Amount  : ₹", bill["total"])

            return

    print("Bill not found.")


def update_bill():
    print("\n--- Update Bill ---")

    bill_id = input(
        "Enter bill ID to update: "
    ).strip()

    if bill_id == "":
        print("Bill ID cannot be empty.")
        return

    for bill in bills:

        if bill["id"] == bill_id:

            print("\nCurrent bill details:")
            print("Patient ID    :", bill["patient_id"])
            print("Consultation  : ₹", bill["consultation"])
            print("Room Charges  : ₹", bill["room"])
            print("Medicine      : ₹", bill["medicine"])
            print("Other Charges : ₹", bill["other"])
            print("Total Amount  : ₹", bill["total"])

            print("\nEnter new details:")

            # New Patient ID
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

            # New charges
            consultation = get_charge(
                "Enter new consultation charge: ₹"
            )

            room = get_charge(
                "Enter new room charge: ₹"
            )

            medicine = get_charge(
                "Enter new medicine charge: ₹"
            )

            other = get_charge(
                "Enter new other charges: ₹"
            )

            # Update bill
            bill["patient_id"] = patient_id
            bill["consultation"] = consultation
            bill["room"] = room
            bill["medicine"] = medicine
            bill["other"] = other

            # Calculate new total
            bill["total"] = (
                consultation +
                room +
                medicine +
                other
            )

            print("Bill updated successfully.")
            print("New Total Amount: ₹", bill["total"])

            return

    print("Bill not found.")


def delete_bill():
    print("\n--- Delete Bill ---")

    bill_id = input(
        "Enter bill ID to delete: "
    ).strip()

    if bill_id == "":
        print("Bill ID cannot be empty.")
        return

    for bill in bills:

        if bill["id"] == bill_id:
            bills.remove(bill)

            print("Bill deleted successfully.")
            return

    print("Bill not found.")
