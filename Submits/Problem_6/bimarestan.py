class Person:
    def __init__(self, first_name, last_name, person_id, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.person_id = person_id
        self.age = age
        self.gender = gender

    def get_person_detail(self):
        return f"Name: {self.first_name} {self.last_name}\nID: {self.person_id}\nAge: {self.age}\nGender: {self.gender}"


class Patient(Person):
    patients_id = 1

    def __init__(self, first_name, last_name, age, gender, disease, doctor):
        super().__init__(first_name, last_name, f"P{Patient.patients_id:0=3}", age, gender)
        self.disease = disease
        self.doctor = doctor
        Patient.patients_id += 1
        print(f"Patient added successfully:\n{self.get_person_detail()}\nDisease: {self.disease}\n"
              f"Assigned Doctor: {self.doctor}")

    def get_patient_details(self):
        print(f"Patient details:\n{self.get_person_detail()}\nDisease: {self.disease}\nAssigned Doctor: {self.doctor}")


class Doctor(Person):
    doctors_id = 1

    def __init__(self, first_name, last_name, age, gender, specialization):
        super().__init__(f"Dr. {first_name}", last_name, f"D{Doctor.doctors_id:0=3}", age, gender)
        self.specialization = specialization
        self.patients = []
        Doctor.doctors_id += 1
        print(f"Doctor added successfully:\n{self.get_person_detail()}\nSpecialization: {self.specialization}")

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_doctor_details(self):
        print(f"Doctor Details:\n{self.get_person_detail()}\nSpecialization: {self.specialization}\nPatients:")
        for patient in self.patients:
            print(f"    - {patient.first_name} {patient.last_name}")

    def get_patients_details(self):
        print("Doctor Patients:")
        for patient in self.patients:
            print(f"    - {patient.get_patient_details()}")


class Nurse(Person):
    nurses_id = 1

    def __init__(self, first_name, last_name, age, gender, department):
        super().__init__(first_name, last_name, f"N{Nurse.nurses_id:0=3}", age, gender)
        self.department = department
        Nurse.nurses_id += 1
        print(f"Nurse added successfully:\n{self.get_person_detail()}\nDepartment: {self.department}")

    def assist_patient(self):
        pass

    def get_nurse_details(self):
        print(f"Nurse Details:\n{self.get_person_detail()}\nDepartment: {self.department}:")


class Appointment:
    def __init__(self, patient, doctor, appointment_time):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.status = "Scheduled"
        print(f"Appointment scheduled successfully:\n{self.get_appointment_details()}")

    def schedule_appointment(self):
        pass

    def cancel_appointment(self):
        self.status = "Canceled"
        print(f"Appointment canceled successfully:\n{self.get_appointment_details()}")

    def get_appointment_details(self):
        print(f"Patient: {self.patient.first_name} {self.patient.last_name}\n"
              f"Doctor: {self.doctor.first_name} {self.doctor.last_name}\nDate and Time: {self.appointment_time}\n"
              f"Status: {self.status}")


class Hospital:
    patients_key = 1
    doctors_key = 1
    nurses_key = 1
    appointments_key = 1

    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.nurses = {}
        self.appointments = {}

    def add_patient(self, patient):
        self.patients[Hospital.patients_key] = patient
        Hospital.patients_key += 1

    def add_doctor(self, doctor):
        self.doctors[Hospital.doctors_key] = doctor
        Hospital.doctors_key += 1

    def add_nurse(self, nurse):
        self.nurses[Hospital.nurses_key] = nurse
        Hospital.nurses_key += 1

    def schedule_appointment(self, appointment):
        self.appointments[Hospital.appointments_key] = appointment
        Hospital.appointments_key += 1

    def get_all_patients(self):
        print("All Patients:" if self.patients else "No Patient yet")
        for num, patient in self.patients.items():
            print(f"{num}- {patient.first_name} {patient.last_name}, person_id: {patient.person_id},"
                  f"Disease:{patient.disease}")

    def get_all_nurse(self):
        print("All Nurses:" if self.nurses else "No Nurse yet")
        for num, nurse in self.nurses.items():
            print(f"{num}- {nurse.first_name} {nurse.last_name}, person_id: {nurse.person_id},"
                  f"Department:{nurse.disease}")

    def get_all_doctors(self):
        print("All Doctors:" if self.doctors else "No Doctor yet")
        for num, doctor in self.doctors.items():
            print(
                f"{num}- {doctor.first_name} {doctor.last_name}, person_id: {doctor.person_id}, "
                f"Specialization: {doctor.specialization}")

    def get_doctor_patients(self):
        for doctor in self.doctors:
            print(doctor.get_patients_details())

    def get_patient_appointments(self):
        for num, appointment in self.appointments.items():
            print(f"{num}- Patient: {appointment.patient.first_name} {appointment.patient.last_name}, "
                  f"Doctor: {appointment.doctor.first_name} {appointment.doctor.last_name}, "
                  f"Date and Time: {appointment.appointment_time}, "
                  f"Status: {appointment.status}")


# patient = Patient("ali", "aliiii", 40, "Male", "heart disease", "mahmodi")

def main():
    hospital = Hospital()
    print("welcome to hospital management system")
    while True:
        print("choose one:\n"
              "1. add doctor\n2. add patient\n3. add nurse\n"
              "4. schedule appointment\n5. cancel appointment\n6. doctor details\n7. patient details\n8. nurse details\n"
              "9. all appointment\n10. all doctors\n11. all patients\n12. all nurse\n13. all appointments\n14. Exit")
        command = input(">> ")
        match command:
            case "1":
                first_name = input("first name: ")
                last_name = input("last name: ")
                age = int(input("age: "))
                gender = input("gender: ")
                specialization = input("specialization: ")
                doctor = Doctor(first_name, last_name, age, gender, specialization)
                hospital.add_doctor(doctor)
            case "2":
                first_name = input("first name: ")
                last_name = input("last name: ")
                age = int(input("age: "))
                gender = input("gender: ")
                disease = input("disease: ")
                doctor = input("doctor: ")
                patient = Patient(first_name, last_name, age, gender, disease, doctor)
                hospital.add_patient(patient)
            case "3":
                first_name = input("first name: ")
                last_name = input("last name: ")
                age = int(input("age: "))
                gender = input("gender: ")
                department = input("department: ")
                nurse = Nurse(first_name, last_name, age, gender, department)
                hospital.add_nurse(nurse)
            case "4":
                hospital.get_all_patients()
                print("choose the patient for appointment")
                key = int(input(">> "))
                patient = hospital.patients[key]
                hospital.get_all_doctors()
                print("choose the doctor for appointment")
                key = int(input(">> "))
                doctor = hospital.doctors[key]
                print("enter the appointment time in following format (yyyy-mm-dd hh:mm)")
                date_time = input(">> ")
                appointment = Appointment(patient, doctor, date_time)
                hospital.schedule_appointment(appointment)
            case "5":
                hospital.get_patient_appointments()
                print("choose the appointment for cancle")
                key = int(input(">> "))
                appointment = hospital.appointments[key]
                appointment.cancel_appointment()
            case "6":
                print("choose the doctor")
                key = int(input(">> "))
                doctor = hospital.doctors[key]
                doctor.get_doctor_details()

            case "7":
                print("choose the patient")
                key = int(input(">> "))
                patient = hospital.patients[key]
                patient.get_patient_details()
                hospital.get_all_patients()

            case "8":
                print("choose the nurse")
                key = int(input(">> "))
                nurse = hospital.nurses[key]
                nurse.get_nurse_details()
            case "9":
                hospital.get_patient_appointments()
            case "10":
                hospital.get_all_doctors()
            case "11":
                hospital.get_all_patients()
            case "12":
                hospital.get_all_nurse()
            case "13":
                hospital.get_patient_appointments()
            case "14":
                return


if __name__ == "__main__":
    main()
