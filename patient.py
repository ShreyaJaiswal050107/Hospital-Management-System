# Patient Management Module 
# This module handles adding, viewing, searching, 
# updating and deleting patient records.

patients = []


def add_patient():
    print("\n--- Add New Patient ---")

    # Patient ID
    while True:
        patient_id = input("Enter patient ID: ").strip()

        if patient_id == "":
            print("Patient ID cannot be empty.")
            continue

        # Check duplicate ID
        duplicate = False

        for patient in patients:
            if patient["id"] == patient_id:
                duplicate = True
                break

        if duplicate:
            print("Patient ID already exists. Enter another ID.")
        else:
            break

    # Patient name
    while True:
        name = input("Enter patient name: ").strip()

        if name == "":
            print("Patient name cannot be empty.")

        elif not name.replace(" ", "").isalpha():
            print("Name should contain only letters.")

        else:
            break

    # Patient age
    while True:
        try:
            age = int(input("Enter patient age: "))

            if age > 0:
                break
            else:
                print("Age must be greater than 0.")

        except ValueError:
            print("Please enter a valid number for age.")

    # Gender
    while True:
        gender = input("Enter gender: ").strip()

        if gender == "":
            print("Gender cannot be empty.")

        elif gender.lower() not in ["male", "female", "other"]:
            print("Please enter Male, Female or Other.")

        else:
            break

    # Disease / problem
    while True:
        disease = input("Enter disease/problem: ").strip()

        if disease == "":
            print("Disease/problem cannot be empty.")

        else:
            break

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease
    }

    patients.append(patient)

    print("Patient added successfully.")


def view_patients():
    print("\n--- Patient Records ---")

    if len(patients) == 0:
        print("No patient records found.")
        return

    for patient in patients:
        print("\nPatient ID :", patient["id"])
        print("Name       :", patient["name"])
        print("Age        :", patient["age"])
        print("Gender     :", patient["gender"])
        print("Disease    :", patient["disease"])


def search_patient():
    print("\n--- Search Patient ---")

    patient_id = input("Enter patient ID to search: ").strip()

    if patient_id == "":
        print("Patient ID cannot be empty.")
        return

    for patient in patients:

        if patient["id"] == patient_id:
            print("\nPatient Found!")
            print("Patient ID :", patient["id"])
            print("Name       :", patient["name"])
            print("Age        :", patient["age"])
            print("Gender     :", patient["gender"])
            print("Disease    :", patient["disease"])
            return

    print("Patient not found.")


def update_patient():
    print("\n--- Update Patient ---")

    patient_id = input("Enter patient ID to update: ").strip()

    if patient_id == "":
        print("Patient ID cannot be empty.")
        return

    for patient in patients:

        if patient["id"] == patient_id:

            print("\nCurrent patient details:")
            print("Name    :", patient["name"])
            print("Age     :", patient["age"])
            print("Gender  :", patient["gender"])
            print("Disease :", patient["disease"])

            print("\nEnter new details:")

            # New name
            while True:
                name = input("Enter new name: ").strip()

                if name == "":
                    print("Name cannot be empty.")

                elif not name.replace(" ", "").isalpha():
                    print("Name should contain only letters.")

                else:
                    patient["name"] = name
                    break

            # New age
            while True:
                try:
                    age = int(input("Enter new age: "))

                    if age > 0:
                        patient["age"] = age
                        break
                    else:
                        print("Age must be greater than 0.")

                except ValueError:
                    print("Please enter a valid number for age.")

            # New gender
            while True:
                gender = input("Enter new gender: ").strip()

                if gender == "":
                    print("Gender cannot be empty.")

                elif gender.lower() not in ["male", "female", "other"]:
                    print("Please enter Male, Female or Other.")

                else:
                    patient["gender"] = gender
                    break

            # New disease
            while True:
                disease = input("Enter new disease/problem: ").strip()

                if disease == "":
                    print("Disease/problem cannot be empty.")

                else:
                    patient["disease"] = disease
                    break

            print("Patient details updated successfully.")
            return

    print("Patient not found.")


def delete_patient():
    print("\n--- Delete Patient ---")

    patient_id = input("Enter patient ID to delete: ").strip()

    if patient_id == "":
        print("Patient ID cannot be empty.")
        return

    for patient in patients:

        if patient["id"] == patient_id:
            patients.remove(patient)

            print("Patient deleted successfully.")
            return

    print("Patient not found.")

