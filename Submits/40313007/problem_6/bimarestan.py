


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
        doctor_name = self.doctor.first_name + " " + self.doctor.last_name
        return f"{super().get_details()}, Disease: {self.disease}, Assigned Doctor: {doctor_name}"

class Doctor(Person):
    def __init__(self, first_name, last_name, person_id, age, gender, specialization):
        super().__init__(first_name, last_name, person_id, age, gender)
        self.specialization = specialization
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_doctor_details(self):
        patients_list = ', '.join([p.first_name + " " + p.last_name for p in self.patients])
        return f"{super().get_details()}, Specialization: {self.specialization}, Patients: [{patients_list}]"

# Nurse class inheriting from Person
class Nurse(Person):
    def __init__(self, first_name, last_name, person_id, age, gender, department):
        super().__init__(first_name, last_name, person_id, age, gender)
        self.department = department

    def assist_patient(self, patient):
        return f"Nurse {self.first_name} is assisting patient {patient.first_name}."

    def get_nurse_details(self):
        return f"{super().get_details()}, Department: {self.department}"

class Appointment:
    def __init__(self, patient, doctor, appointment_time):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.status = "Scheduled"

    def cancel_appointment(self):
        self.status = "Canceled"

    def get_appointment_details(self):
        return f"Patient: {self.patient.first_name} {self.patient.last_name}, Doctor: {self.doctor.first_name} {self.doctor.last_name}, Date and Time: {self.appointment_time}, Status: {self.status}"

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.nurses = []
        self.appointments = []

    def add_patient(self, first_name, last_name, person_id, age, gender, disease, doctor):
        new_patient = Patient(first_name, last_name, person_id, age, gender, disease, doctor)
        self.patients.append(new_patient)
        doctor.add_patient(new_patient)
        print("Patient added successfully:")
        print(new_patient.get_patient_details())

    def add_doctor(self, first_name, last_name, person_id, age, gender, specialization):
        new_doctor = Doctor(first_name, last_name, person_id, age, gender, specialization)
        self.doctors.append(new_doctor)
        print("Doctor added successfully:")
        print(new_doctor.get_doctor_details())

    def add_nurse(self, first_name, last_name, person_id, age, gender, department):
        new_nurse = Nurse(first_name, last_name, person_id, age, gender, department)
        self.nurses.append(new_nurse)
        print("Nurse added successfully:")
        print(new_nurse.get_nurse_details())

    def schedule_appointment(self, patient, doctor, appointment_time):
        new_appointment = Appointment(patient, doctor, appointment_time)
        self.appointments.append(new_appointment)
        print("Appointment scheduled successfully:")
        print(new_appointment.get_appointment_details())

    def cancel_appointment(self, appointment):
        appointment.cancel_appointment()
        print("Appointment canceled successfully:")
        print(appointment.get_appointment_details())

    def get_all_patients(self):
        if not self.patients:
            print("No patients found.")
        for patient in self.patients:
            print(patient.get_patient_details())

    def get_doctor_patients(self, doctor):
        if not doctor.patients:
            print(f"No patients found for doctor {doctor.first_name} {doctor.last_name}.")
        for patient in doctor.patients:
            print(patient.get_patient_details())

    def get_patient_appointments(self, patient):
        if not any(appointment.patient == patient for appointment in self.appointments):
            print("No appointments found for this patient.")
        for appointment in self.appointments:
            if appointment.patient == patient:
                print(appointment.get_appointment_details())

    def get_all_appointments(self):
        if not self.appointments:
            print("No appointments found.")
            return
        for appointment in self.appointments:
            print(appointment.get_appointment_details())

    def get_all_doctors(self):
        if not self.doctors:
            print("No doctors found.")
        for doctor in self.doctors:
            print(doctor.get_doctor_details())

def main():
    hospital = Hospital()

    while True:
        print("\nMenu:")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Add Nurse")
        print("4. Schedule Appointment")
        print("5. Cancel Appointment")
        print("6. Get All Patients")
        print("7. Get Patients of a Doctor")
        print("8. Get Appointments of a Patient")
        print("9. Get All Appointments")
        print("10. Get All Doctors")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            person_id = input("Enter ID: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            specialization = input("Enter specialization: ")
            hospital.add_doctor(first_name, last_name, person_id, age, gender, specialization)

        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            person_id = input("Enter ID: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            disease = input("Enter disease: ")
            doctor_id = input("Enter doctor's ID for the patient: ")
            doctor = next((doc for doc in hospital.doctors if doc.person_id == doctor_id), None)
            if doctor:
                hospital.add_patient(first_name, last_name, person_id, age, gender, disease, doctor)
            else:
                print("Doctor not found.")

        elif choice == '3':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            person_id = input("Enter ID: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            department = input("Enter department: ")
            hospital.add_nurse(first_name, last_name, person_id, age, gender, department)

        elif choice == '4':
            patient_id = input("Enter patient's ID: ")
            doctor_id = input("Enter doctor's ID: ")
            appointment_time = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
            patient = next((p for p in hospital.patients if p.person_id == patient_id), None)
            doctor = next((d for d in hospital.doctors if d.person_id == doctor_id), None)
            if patient and doctor:
                hospital.schedule_appointment(patient, doctor, appointment_time)
            else:
                print("Patient or Doctor not found.")

        elif choice == '5':
            appointment_id = int(input("Enter appointment index to cancel: ")) - 1
            if 0 <= appointment_id < len(hospital.appointments):
                hospital.cancel_appointment(hospital.appointments[appointment_id])
            else:
                print("Invalid appointment index.")

        elif choice == '6':
            hospital.get_all_patients()

        elif choice == '7':
            doctor_id = input("Enter doctor's ID: ")
            doctor = next((doc for doc in hospital.doctors if doc.person_id == doctor_id), None)
            if doctor:
                hospital.get_doctor_patients(doctor)
            else:
                print("Doctor not found.")

        elif choice == '8':
            patient_id = input("Enter patient's ID: ")
            patient = next((p for p in hospital.patients if p.person_id == patient_id), None)
            if patient:
                hospital.get_patient_appointments(patient)
            else:
                print("Patient not found.")

        elif choice == '9':
            hospital.get_all_appointments()

        elif choice == '10':
            hospital.get_all_doctors()

        elif choice == '11':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()