from datetime import datetime

class Person:
    def __init__(self, firstName, lastName, age, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender
        self.random_field = "nothing"

    def getDetails(self):
        return f"{self.firstName} {self.lastName} is {self.age} years old, Gender: {self.gender}"

class Patient(Person):
    def __init__(self, firstName, lastName, age, gender, patientID, disease, doc=None):
        super().__init__(firstName, lastName, age, gender)
        self.patientID = patientID
        self.disease = disease
        self.doc = doc

    def getDetails(self):
        doc_info = f"Dr. {self.doc.firstName} {self.doc.lastName}" if self.doc else "No doctor"
        return f"{super().getDetails()}, ID: {self.patientID}, Disease: {self.disease}, Doctor: {doc_info}"
class Doctor(Person):
    def __init__(self, fname, lname, age, gender, doc_id, specialty):
        super().__init__(fname, lname, age, gender)
        self.doc_id = doc_id
        self.specialty = specialty
        self.patients_list = {}

    def addPatient(self, patient):
        self.patients_list[patient.patientID] = patient
        patient.doc = self
        return f"Added {patient.firstName} to Dr. {self.firstName}'s list"
    def showMe(self):
        patient_names = ", ".join([p.firstName + " " + p.lastName for p in self.patients_list.values()]) if self.patients_list else "No patients"
        return f"{self.getDetails()}, ID: {self.doc_id}, Specialty: {self.specialty}, Patients: {patient_names}"

class Nurse(Person):
    def __init__(self, fname, lname, age, gender, nurseID, dept):
        super().__init__(fname, lname, age, gender)
        self.nurseID = nurseID
        self.dept = dept

    def helpOut(self, patient):
        return f"Nurse {self.firstName} helping {patient.firstName}"

    def getDetails(self):
        return f"{super().getDetails()}, ID: {self.nurseID}, Department: {self.dept}"

class Appointment:
    def __init__(self, patient, doctor, when):
        self.patient = patient
        self.doctor = doctor
        self.when = when
        self.is_active = True

    def cancelIt(self):
        self.is_active = False
        return f"Canceled appointment for {self.patient.firstName} on {self.when}"

    def __str__(self):
        status = "Active" if self.is_active else "Canceled"
        return f"{self.patient.firstName} with Dr. {self.doctor.firstName} on {self.when} - {status}"
class Hospital:
    def __init__(self):
        self.all_patients = {}
        self.all_doctors = {}
        self.all_nurses = {}
        self.appointments = []
        self.some_unused_list = []

    def add_patient(self, patient):
        self.all_patients[patient.patientID] = patient
        return f"Patient {patient.firstName} added"

    def add_doctor(self, doctor):
        self.all_doctors[doctor.doc_id] = doctor
        return f"Doctor {doctor.firstName} added"

    def add_nurse(self, nurse):
        self.all_nurses[nurse.nurseID] = nurse
        return f"Nurse {nurse.firstName} added"

    def schedule_appointment(self, patient, doctor, when):
        appt = Appointment(patient, doctor, when)
        self.appointments.append(appt)
        return f"Scheduled: {appt}"

    def get_all_patients(self):
        if not self.all_patients:
            return "No patients yet"
        return "\n".join([patient.getDetails() for patient in self.all_patients.values()])

    def get_doctor_patients(self, doctor):
        if not doctor.patients_list:
            return "This doctor has no patients"
        return "\n".join([patient.getDetails() for patient in doctor.patients_list.values()])
    def get_patient_appointments(self, patient):
        appts = [appt for appt in self.appointments if appt.patient == patient]
        if not appts:
            return "No appointments for this patient"
        return "\n".join([str(appt) for appt in appts])

    def findDoctor(self, doc_id):
        return self.all_doctors.get(doc_id)

    def findPatient(self, patient_id):
        return self.all_patients.get(patient_id)

    def findNurse(self, nurse_id):
        return self.all_nurses.get(nurse_id)
    def weirdFunction(self, x):
        return x * 2

def checkGender(gender):
    gender = gender.lower()
    if gender not in ["male", "female"]:
        return "error404"
    return gender.capitalize()

def main():
    hospital = Hospital()
    while True:
        print("\nHospital App")
        print("1 - Add a doctor")
        print("2 - Add a patient ")
        print("3 - Add a nurse")
        print("4 - Assign patient to doctor")
        print("5 - Schedule an appointment")
        print("6 - Cancel an appointment")
        print("7 - View patient info")
        print("8 - View doctor info ")
        print("9 - View nurse info")
        print("10 - List all patients")
        print("11 - List doctor's patients")
        print("12 - List patient's appointments")
        print("13 - List all doctors")
        print("0 - Exit")
        choice = input("Pick an option: ")

        if choice == "1":
            firstName = input("Doctor's first name: ")
            lastName = input("Doctor's last name: ")
            age = int(input("Age: "))
            gender = input("Gender (Male/Female): ")
            gender = checkGender(gender)
            if gender == "error404":
                print(gender)
                continue
            doc_id = input("Doctor ID: ")
            specialty = input("Specialty: ")
            doctor = Doctor(firstName, lastName, age, gender, doc_id, specialty)
            print(hospital.add_doctor(doctor))

        elif choice == "2":
            fname = input("Patient's first name: ")
            lname = input("Last name: ")
            age = int(input("Age: "))
            gender = input("Gender (Male/Female): ")
            gender = checkGender(gender)
            if gender == "error404":
                print(gender)
                continue
            patientID = input("Patient ID: ")
            disease = input("Disease: ")
            patient = Patient(fname, lname, age, gender, patientID, disease)
            print(hospital.add_patient(patient))

        elif choice == "3":
            firstName = input("Nurse's first name: ")
            lastName = input("Last name: ")
            age = int(input("Age: "))
            gender = input("Gender (Male/Female): ")
            gender = checkGender(gender)
            if gender == "error404":
                print(gender)
                continue
            nurseID = input("Nurse ID: ")
            dept = input("Department: ")
            nurse = Nurse(firstName, lastName, age, gender, nurseID, dept)
            print(hospital.add_nurse(nurse))

        elif choice == "4":
            patient_id = input("Patient ID: ")
            doc_id = input("Doctor ID: ")
            patient = hospital.findPatient(patient_id)
            doctor = hospital.findDoctor(doc_id)
            if patient and doctor:
                print(doctor.addPatient(patient))
            else:
                print("Couldn't find patient or doctor")

        elif choice == "5":
            patient_id = input("Patient ID: ")
            doc_id = input("Doctor ID: ")
            when = input("When (e.g., 2025-03-10 18:00): ")
            patient = hospital.findPatient(patient_id)
            doctor = hospital.findDoctor(doc_id)
            if patient and doctor:
                print(hospital.schedule_appointment(patient, doctor, when))
            else:
                print("Patient or doctor not found")

        elif choice == "6":
            patient_id = input("Patient ID: ")
            patient = hospital.findPatient(patient_id)
            if patient:
                appts = [appt for appt in hospital.appointments if appt.patient == patient and appt.is_active]
                if appts:
                    print("Appointments:")
                    for i, appt in enumerate(appts, 1):
                        print(f"{i}. {appt}")
                    appt_num = int(input("Which one to cancel? (number): ")) - 1
                    if 0 <= appt_num < len(appts):
                        print(appts[appt_num].cancelIt())
                    else:
                        print("Invalid number")
                else:
                    print("No active appointments")
            else:
                print("Patient not found")

        elif choice == "7":
            patient_id = input("Patient ID: ")
            patient = hospital.findPatient(patient_id)
            if patient:
                print(patient.getDetails())
            else:
                print("Patient not found")

        elif choice == "8":
            doc_id = input("Doctor ID: ")
            doctor = hospital.findDoctor(doc_id)
            if doctor:
                print(doctor.showMe())
            else:
                print("Doctor not found")

        elif choice == "9":
            nurse_id = input("Nurse ID: ")
            nurse = hospital.findNurse(nurse_id)
            if nurse:
                print(nurse.getDetails())
            else:
                print("Nurse not found")

        elif choice == "10":
            print(hospital.get_all_patients())

        elif choice == "11":
            doc_id = input("Doctor ID: ")
            doctor = hospital.findDoctor(doc_id)
            if doctor:
                print(hospital.get_doctor_patients(doctor))
            else:
                print("Doctor not found")

        elif choice == "12":
            patient_id = input("Patient ID: ")
            patient = hospital.findPatient(patient_id)
            if patient:
                print(hospital.get_patient_appointments(patient))
            else:
                print("Patient not found")

        elif choice == "13":
            if not hospital.all_doctors:
                print("No doctors")
            else:
                print("\n".join([doc.showMe() for doc in hospital.all_doctors.values()]))

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Wrong option, try again")

if __name__ == "__main__":
    main()
#age ye seri chizaye ezafe dare codam ke estefade nashode bekhatere kamboode vaght bood,saay dashtam yekam funesh konam va khalaghiat be kharj bedam ke vaght nemishe