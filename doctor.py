# Doctor Management Module 
# This module handles adding, viewing, searching, 
# updating and deleting doctor records.

doctors = []


def add_doctor():
    print("\n--- Add New Doctor ---")

    # Doctor ID
    while True:
        doctor_id = input("Enter doctor ID: ").strip()

        if doctor_id == "":
            print("Doctor ID cannot be empty.")
            continue

        # Check duplicate ID
        duplicate = False

        for doctor in doctors:
            if doctor["id"] == doctor_id:
                duplicate = True
                break

        if duplicate:
            print("Doctor ID already exists. Enter another ID.")
        else:
            break

    # Doctor name
    while True:
        name = input("Enter doctor name: ").strip()

        if name == "":
            print("Doctor name cannot be empty.")

        elif not name.replace(" ", "").isalpha():
            print("Name should contain only letters.")

        else:
            break

    # Specialization
    while True:
        specialization = input("Enter specialization: ").strip()

        if specialization == "":
            print("Specialization cannot be empty.")

        else:
            break

    # Department
    while True:
        department = input("Enter department: ").strip()

        if department == "":
            print("Department cannot be empty.")

        else:
            break

    # Experience
    while True:
        try:
            experience = int(
                input("Enter years of experience: ")
            )

            if experience >= 0:
                break
            else:
                print("Experience cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")

    doctor = {
        "id": doctor_id,
        "name": name,
        "specialization": specialization,
        "department": department,
        "experience": experience
    }

    doctors.append(doctor)

    print("Doctor added successfully.")


def view_doctors():
    print("\n--- Doctor Records ---")

    if len(doctors) == 0:
        print("No doctor records found.")
        return

    for doctor in doctors:
        print("\nDoctor ID     :", doctor["id"])
        print("Name          :", doctor["name"])
        print("Specialization:", doctor["specialization"])
        print("Department    :", doctor["department"])
        print("Experience    :", doctor["experience"], "years")


def search_doctor():
    print("\n--- Search Doctor ---")

    doctor_id = input("Enter doctor ID to search: ").strip()

    if doctor_id == "":
        print("Doctor ID cannot be empty.")
        return

    for doctor in doctors:

        if doctor["id"] == doctor_id:
            print("\nDoctor Found!")
            print("Doctor ID     :", doctor["id"])
            print("Name          :", doctor["name"])
            print("Specialization:", doctor["specialization"])
            print("Department    :", doctor["department"])
            print("Experience    :", doctor["experience"], "years")
            return

    print("Doctor not found.")


def update_doctor():
    print("\n--- Update Doctor ---")

    doctor_id = input("Enter doctor ID to update: ").strip()

    if doctor_id == "":
        print("Doctor ID cannot be empty.")
        return

    for doctor in doctors:

        if doctor["id"] == doctor_id:

            print("\nCurrent doctor details:")
            print("Name          :", doctor["name"])
            print("Specialization:", doctor["specialization"])
            print("Department    :", doctor["department"])
            print("Experience    :", doctor["experience"], "years")

            print("\nEnter new details:")

            # New name
            while True:
                name = input("Enter new name: ").strip()

                if name == "":
                    print("Name cannot be empty.")

                elif not name.replace(" ", "").isalpha():
                    print("Name should contain only letters.")

                else:
                    doctor["name"] = name
                    break

            # New specialization
            while True:
                specialization = input(
                    "Enter new specialization: "
                ).strip()

                if specialization == "":
                    print("Specialization cannot be empty.")

                else:
                    doctor["specialization"] = specialization
                    break

            # New department
            while True:
                department = input(
                    "Enter new department: "
                ).strip()

                if department == "":
                    print("Department cannot be empty.")

                else:
                    doctor["department"] = department
                    break

            # New experience
            while True:
                try:
                    experience = int(
                        input("Enter new years of experience: ")
                    )

                    if experience >= 0:
                        doctor["experience"] = experience
                        break
                    else:
                        print("Experience cannot be negative.")

                except ValueError:
                    print("Please enter a valid number.")

            print("Doctor details updated successfully.")
            return

    print("Doctor not found.")


def delete_doctor():
    print("\n--- Delete Doctor ---")

    doctor_id = input("Enter doctor ID to delete: ").strip()

    if doctor_id == "":
        print("Doctor ID cannot be empty.")
        return

    for doctor in doctors:

        if doctor["id"] == doctor_id:
            doctors.remove(doctor)

            print("Doctor deleted successfully.")
            return

    print("Doctor not found.")
