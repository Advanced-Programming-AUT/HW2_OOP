

class Person:
    def __init__(self, first_name, last_name, person_id, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.person_id = person_id
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.first_name} {self.last_name}, ID: {self.person_id}, Age: {self.age}, Gender: {self.gender}"


class Patient(Person):
    def __init__(self, first_name, last_name, person_id, age, gender, disease, doctor):
        super().__init__(first_name, last_name, person_id, age, gender)
        self.disease = disease
        self.doctor = doctor

    def get_patient_details(self):
        return f"{self.get_details()}, Disease: {self.disease}, Assigned Doctor: {self.doctor}"


class Doctor(Person):
    def __init__(self, first_name, last_name, person_id, age, gender, specialization):
        super().__init__(first_name, last_name, person_id, age, gender)
        self.specialization = specialization
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_doctor_details(self):
        patients_list = ", ".join([patient.first_name for patient in self.patients]) or "None"
        return f"{self.get_details()}, Specialization: {self.specialization}, Patients: {patients_list}"


class Nurse(Person):
    def __init__(self, first_name, last_name, person_id, age, gender, department):
        super().__init__(first_name, last_name, person_id, age, gender)
        self.department = department

    def assist_patient(self, patient):
        print(f"Nurse {self.first_name} is assisting patient {patient.first_name}.")

    def get_nurse_details(self):
        return f"{self.get_details()}, Department: {self.department}"


class Appointment:
    def __init__(self, patient, doctor, appointment_time, status="Scheduled"):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.status = status

    def schedule_appointment(self):
        self.status = "Scheduled"
        print(f"Appointment scheduled successfully: Patient: {self.patient.first_name}, Doctor: {self.doctor.first_name}, Time: {self.appointment_time}, Status: {self.status}")

    def cancel_appointment(self):
        self.status = "Canceled"
        print(f"Appointment canceled successfully: Patient: {self.patient.first_name}, Doctor: {self.doctor.first_name}, Time: {self.appointment_time}, Status: {self.status}")

    def get_appointment_details(self):
        return f"Patient: {self.patient.first_name}, Doctor: {self.doctor.first_name}, Time: {self.appointment_time}, Status: {self.status}"


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.nurses = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient added successfully: {patient.get_patient_details()}")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor added successfully: {doctor.get_doctor_details()}")

    def add_nurse(self, nurse):
        self.nurses.append(nurse)
        print(f"Nurse added successfully: {nurse.get_nurse_details()}")

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)
        appointment.schedule_appointment()

    def get_all_patients(self):
        for patient in self.patients:
            print(patient.get_patient_details())

    def get_doctor_patients(self, doctor_id):
        for doctor in self.doctors:
            if doctor.person_id == doctor_id:
                print(doctor.get_doctor_details())
                return
        print("Doctor not found.")

    def get_patient_appointments(self, patient_id):
        for appointment in self.appointments:
            if appointment.patient.person_id == patient_id:
                print(appointment.get_appointment_details())


def main_menu():
    hospital = Hospital()

    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Add Nurse")
        print("4. Schedule Appointment")
        print("5. Cancel Appointment")
        print("6. Display Patient Details")
        print("7. Display Doctor Details")
        print("8. Display All Patients")
        print("9. Display All Doctors")
        print("10. Display All Appointments")
        print("11. Exit")

        choice = input("Select an option (1-11): ")

        if choice == "1":
            first_name = input("Enter doctor's first name: ")
            last_name = input("Enter doctor's last name: ")
            doctor_id = input("Enter doctor's ID: ")
            age = int(input("Enter doctor's age: "))
            gender = input("Enter doctor's gender (Male/Female): ")
            specialization = input("Enter doctor's specialization: ")
            doctor = Doctor(first_name, last_name, doctor_id, age, gender, specialization)
            hospital.add_doctor(doctor)

        elif choice == "2":
            first_name = input("Enter patient's first name: ")
            last_name = input("Enter patient's last name: ")
            patient_id = input("Enter patient's ID: ")
            age = int(input("Enter patient's age: "))
            gender = input("Enter patient's gender (Male/Female): ")
            disease = input("Enter patient's disease: ")
            assigned_doctor = input("Enter assigned doctor's name: ")
            patient = Patient(first_name, last_name, patient_id, age, gender, disease, assigned_doctor)
            hospital.add_patient(patient)

        elif choice == "3":
            first_name = input("Enter nurse's first name: ")
            last_name = input("Enter nurse's last name: ")
            nurse_id = input("Enter nurse's ID: ")
            age = int(input("Enter nurse's age: "))
            gender = input("Enter nurse's gender (Male/Female): ")
            department = input("Enter nurse's department: ")
            nurse = Nurse(first_name, last_name, nurse_id, age, gender, department)
            hospital.add_nurse(nurse)

        elif choice == "4":
            patient_id = input("Enter patient's ID for the appointment: ")
            doctor_id = input("Enter doctor's ID for the appointment: ")
            appointment_time = input("Enter date and time of appointment (YYYY-MM-DD HH:MM): ")
            patient = next((p for p in hospital.patients if p.person_id == patient_id), None)
            doctor = next((d for d in hospital.doctors if d.person_id == doctor_id), None)
            if patient and doctor:
                appointment = Appointment(patient, doctor, appointment_time)
                hospital.schedule_appointment(appointment)
            else:
                print("Invalid patient or doctor ID.")

        elif choice == "5":
            patient_id = input("Enter patient's ID for the appointment: ")
            doctor_id = input("Enter doctor's ID for the appointment: ")
            appointment = next((a for a in hospital.appointments if
                                a.patient.person_id == patient_id and a.doctor.person_id == doctor_id), None)
            if appointment:
                appointment.cancel_appointment()
            else:
                print("Appointment not found.")

        elif choice == "6":
            patient_id = input("Enter patient's ID: ")
            patient = next((p for p in hospital.patients if p.person_id == patient_id), None)
            if patient:
                print(patient.get_patient_details())
            else:
                print("Patient not found.")

        elif choice == "7":
            doctor_id = input("Enter doctor's ID: ")
            doctor = next((d for d in hospital.doctors if d.person_id == doctor_id), None)
            if doctor:
                print(doctor.get_doctor_details())
            else:
                print("Doctor not found.")

        elif choice == "8":
            hospital.get_all_patients()

        elif choice == "9":
            for doctor in hospital.doctors:
                print(doctor.get_doctor_details())

        elif choice == "10":
            for appointment in hospital.appointments:
                print(appointment.get_appointment_details())

        elif choice == "11":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")





if __name__ == '__main__':
    main_menu()


