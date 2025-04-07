import numpy as np


class Person:
    def __init__(self, first_name, last_name, id, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.age = age
        self.gender = gender


class Patient(Person):
    def __init__(self, first_name, last_name, id, age, gender, disease, doctor):
        super().__init__(first_name, last_name, id, age, gender)
        self.disease = disease
        self.doctor = doctor

    def get_patient_details(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"ID: {self.id}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Disease: {self.disease}")
        print(f"Doctor: {self.doctor}")


class Doctor(Person):
    def __init__(self, first_name, last_name, id, age, gender, specialization, patients):
        super().__init__(first_name, last_name, id, age, gender)
        self.specialization = specialization
        self.patients = patients

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_doctor_details(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"ID: {self.id}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Specialization: {self.specialization}")


class Nurse(Person):
    def __init__(self, first_name, last_name, id, age, gender, department):
        super().__init__(first_name, last_name, id, age, gender)
        self.department = department

    def assist_patient(self, patient):
        pass

    def get_nurse_details(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"ID: {self.id}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Department: {self.department}")


class Appointment:
    def __init__(self, patient, doctor, appointment_time, status):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.status = status

    def schedule_appointment(self):
        return (f"Appointment scheduled for {self.patient.first_name} with"
                f"{self.doctor.first_name} on {self.appointment_time}")

    def cancel_appointment(self):
        self.status = "Canceled"
        return f"Appointment canceled for {self.patient.first_name}"

    def get_appointment_details(self):
        return (f"Appointment Details: Patient: {self.patient.first_name}, Doctor: {self.doctor.first_name},"
                f"Time: {self.appointment_time}, Status: {self.status}")


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.nurses = []
        self.appointments = []
        self.appointment_schedule = [[None for _ in range(7)] for _ in range(7)]
        for i in range(7):
            for j in range(7):
                self.appointment_schedule[i][j] = "Empty"
        self.appointment_schedule[0][0] = ""
        self.appointment_schedule[0][1] = "7 - 8"
        self.appointment_schedule[0][2] = "8 - 9"
        self.appointment_schedule[0][3] = "9 - 10"
        self.appointment_schedule[0][4] = "10 - 11"
        self.appointment_schedule[0][5] = "11 - 12"
        self.appointment_schedule[0][6] = "12 - 13"
        self.appointment_schedule[1][0] = "Saturday"
        self.appointment_schedule[2][0] = "Sunday"
        self.appointment_schedule[3][0] = "Monday"
        self.appointment_schedule[4][0] = "Tuesday"
        self.appointment_schedule[5][0] = "Wednesday"
        self.appointment_schedule[6][0] = "Thursday"

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_nurse(self, nurse):
        self.nurses.append(nurse)

    def show_schedule(self):
        for i in range(7):
            for j in range(7):
                print(self.appointment_schedule[i][j].center(15), end="  ")
            print()

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)

    def get_all_patients(self):
        return [patient.first_name for patient in self.patients]

    def get_doctor_patients(self, doctor):
        return [patient.first_name for patient in doctor.patients]

    def get_patient_appointments(self, patient):
        return [appointment.get_appointment_details() for appointment
                in self.appointments if appointment.patient == patient]


def menu():
    hospital = Hospital()

    print("Welcome to Hospital")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Add Nurse")
    print("4. Show Information")
    print("5. Show Appointments Schedule")
    print("6. Schedule Appointment")
    print("7. Cancel Appointment")

    choice = int(input())

    if choice == 1:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        id = input("ID: ")
        age = input("Age: ")
        gender = input("Gender: ")
        disease = input("Disease: ")
        doctor = input("Doctor: ")
        hospital.add_patient(Patient(first_name, last_name, id, age, gender, disease, doctor))
        print("Patient details added.")
        menu()

    if choice == 2:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        id = input("ID: ")
        age = input("Age: ")
        gender = input("Gender: ")
        specialization = input("Specialization: ")
        patients_number = int(input("Number of patients: "))
        patients = []
        for i in range(patients_number):
            patient_first_name = input("First name: ")
            patient_last_name = input("Last name: ")
            patient_id = input("ID: ")
            patient_age = input("Age: ")
            patient_gender = input("Gender: ")
            patient_disease = input("Disease: ")
            patients.append(Patient(patient_first_name, patient_last_name, patient_id, patient_age, patient_gender, patient_disease, last_name))
        hospital.add_doctor(Doctor(first_name, last_name, id, age, gender, specialization, patients))
        menu()

    if choice == 3:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        id = input("ID: ")
        age = input("Age: ")
        gender = input("Gender: ")
        department = input("Department: ")
        hospital.add_nurse(Nurse(first_name, last_name, id, age, gender, department))
        menu()

    if choice == 4:
        print("1. Doctors")
        print("2. Nurses")
        print("3. Patients")

        ch = int(input())

        if ch == 1:
            for doctor in hospital.doctors:
                print(doctor.get_doctor_details())
            menu()
        if ch == 2:
            for patient in hospital.patients:
                print(patient.get_patient_details(patient))
            menu()
        if ch == 3:
            for nurse in hospital.nurses:
                print(nurse.get_nurse_details(nurse))
            menu()

    if choice == 5:
        print(hospital.show_schedule())

    if choice == 6:
        flag = False
        for i in range(1, 7):
            for j in range(1, 7):
                if hospital.appointment_schedule[i][j] == "Empty":
                    appointment_time = f"{hospital.appointment_schedule[i][0]} at {hospital.appointment_schedule[0][j]}"
                    print(appointment_time)
                    flag = True
                    break
            if flag == True:
                break
        doctor = input("Doctor: ")
        patient = input("Patient: ")
        appointment = Appointment(patient, doctor, appointment_time)

    if choice == 7:
        i = 0
        for appointment in hospital.appointments:
            print(f"{i}. {appointment.get_appointment_details()}")
            i += 1
        ch = int(input())
        hospital.appointments[ch - 1].cancle_appointment()


menu()
