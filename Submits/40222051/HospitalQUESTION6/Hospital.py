class Person:
    def __init__(self, first_name, last_name, id_, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.id_ = id_
        self.age = age
        self.gender = gender

class Patient(Person):
    def __init__(self, disease, doctor, first_name, last_name, id_, age, gender):
        super().__init__(first_name, last_name, id_, age, gender)
        self.disease = disease
        self.doctor = doctor

    def get_patient_details(self):
        print("Patient Details:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"ID: {self.id_} Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Disease: {self.disease}")
        print(f"Assigned Doctor: {self.doctor.first_name} {self.doctor.last_name}")

class Doctor(Person):
    def __init__(self, specialization, first_name, last_name, id_, age, gender):
        super().__init__(first_name, last_name, id_, age, gender)
        self.specialization = specialization
        self.patients = [] #for storing patients of each doctor

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully:")
        print(f"Name: {patient.first_name} {patient.last_name}")
        print(f"ID: {patient.id_} Age: {patient.age}")
        print(f"Gender: {patient.gender}")
        print(f"Disease: {patient.disease}")
        print(f"Assigned Doctor: {self.first_name} {self.last_name}")

    def get_doctor_details(self):
        print("Doctor Details:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"ID: {self.id_} Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Specialization: {self.specialization}")
        print("Patients:")
        for patient in self.patients: # showing the patients of doctor
            print(f"- {patient.first_name} {patient.last_name}")

class Nurse(Person):
    def __init__(self, department, first_name, last_name, id_, age, gender):
        super().__init__(first_name, last_name, id_, age, gender)
        self.department = department

    def assist_patient(self, patient):
        print(f"Nurse {self.first_name} {self.last_name} is assisting patient {patient.first_name} {patient.last_name}")

    def get_nurse_details(self):
        print("Nurse Details:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"ID: {self.id_} Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Department: {self.department}")

class Appointment:
    def __init__(self, patient, doctor, appointment_time, status="Scheduled"):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.status = status #whether it is canceled or not

    def schedule_appointment(self):
        self.status = "Scheduled"
        print("Appointment scheduled successfully:")
        print(f"Patient: {self.patient.first_name} {self.patient.last_name}")
        print(f"Doctor: {self.doctor.first_name} {self.doctor.last_name}")
        print(f"Date and Time: {self.appointment_time}")
        print(f"Status: {self.status}")

    def cancel_appointment(self):
        self.status = "Canceled"
        print("Appointment canceled successfully:")
        print(f"Patient: {self.patient.first_name} {self.patient.last_name}")
        print(f"Doctor: {self.doctor.first_name} {self.doctor.last_name}")
        print(f"Date and Time: {self.appointment_time}")
        print(f"Status: {self.status}")

    def get_appointment_details(self):
        print("Appointment Details:")
        print(f"Patient: {self.patient.first_name} {self.patient.last_name}")
        print(f"Doctor: {self.doctor.first_name} {self.doctor.last_name}")
        print(f"Date and Time: {self.appointment_time}")
        print(f"Status: {self.status}")

class Hospital:
    def __init__(self): #lists for storing staff and patients and appointments in the hospital each seperately
        self.patients = []
        self.doctors = []
        self.nurses = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)
        patient.doctor.add_patient(patient)  # Add patient to doctor's list
        print(f"Patient {patient.first_name} {patient.last_name} added to hospital")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor {doctor.first_name} {doctor.last_name} added to hospital")

    def add_nurse(self, nurse):
        self.nurses.append(nurse)
        print(f"Nurse {nurse.first_name} {nurse.last_name} added to hospital")

    def schedule_appointment(self, patient, doctor, appointment_time):
        appointment = Appointment(patient, doctor, appointment_time)
        self.appointments.append(appointment)
        # only add patient to doctor's list if not already there
        if patient not in doctor.patients:
            doctor.add_patient(patient)
        patient.doctor = doctor
        appointment.schedule_appointment()
        return appointment

    def get_all_patients(self):
        print("All Patients:")
        for patient in self.patients:
            patient.get_patient_details()
            print("---")

    def get_doctor_patients(self):
        print("Doctors and their Patients:")
        for doctor in self.doctors:
            doctor.get_doctor_details()
            print("---")

    def get_patient_appointments(self):
        print("All Appointments:")
        for appointment in self.appointments:
            appointment.get_appointment_details()
            print("---")


def process():
    hospital = Hospital()

    while True:
        print("\nHospital Management System")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Add Nurse")
        print("4. Schedule Appointment")
        print("5. View All Patients")
        print("6. View Doctors and Patients")
        print("7. View All Appointments")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1": # adding Doctor
            first_name = input("Enter doctor's first name: ")
            last_name = input("Enter doctor's last name: ")
            id_ = input("Enter doctor's ID: ")
            age = int(input("Enter doctor's age: "))
            gender = input("Enter doctor's gender: ")
            specialization = input("Enter doctor's specialization: ")
            doctor = Doctor(specialization, first_name, last_name, id_, age, gender)
            hospital.add_doctor(doctor)

        elif choice == "2":# adding patient
            if not hospital.doctors:
                print("Please add a doctor first!")# checking if doctors exist before adding a patient
                continue
            first_name = input("Enter patient's first name: ")
            last_name = input("Enter patient's last_name: ")
            id_ = input("Enter patient's ID: ")
            age = int(input("Enter patient's age: "))
            gender = input("Enter patient's gender: ")
            disease = input("Enter patient's disease: ")
            print("Available doctors:")
            for i, doc in enumerate(hospital.doctors, 1): #displaying all doctors
                print(f"{i}. {doc.first_name} {doc.last_name} - {doc.specialization}")
            doc_choice = int(input("Select doctor number: ")) - 1
            if 0 <= doc_choice < len(hospital.doctors):#ensuring valid doctor selection
                doctor = hospital.doctors[doc_choice]
                patient = Patient(disease, doctor, first_name, last_name, id_, age, gender)
                hospital.add_patient(patient)
            else:
                print("Invalid doctor selection!")
        # adding Nurse
        elif choice == "3":
            first_name = input("Enter nurse's first name: ")
            last_name = input("Enter nurse's last name: ")
            id_ = input("Enter nurse's ID: ")
            age = int(input("Enter nurse's age: "))
            gender = input("Enter nurse's gender: ")
            department = input("Enter nurse's department: ")
            nurse = Nurse(department, first_name, last_name, id_, age, gender)
            hospital.add_nurse(nurse)
        # scheduling appointment
        elif choice == "4":
            if not hospital.patients or not hospital.doctors:# ensuring both patients and doctors are available
                print("Please add both patients and doctors first!")
                continue
            print("Available patients:")
            for i, patient in enumerate(hospital.patients, 1): # displaying all patients
                print(f"{i}. {patient.first_name} {patient.last_name}")
            patient_choice = int(input("Select patient number: ")) - 1
            print("Available doctors:")
            for i, doc in enumerate(hospital.doctors, 1):
                print(f"{i}. {doc.first_name} {doc.last_name}")
            doc_choice = int(input("Select doctor number: ")) - 1
            if (0 <= patient_choice < len(hospital.patients) and
                    0 <= doc_choice < len(hospital.doctors)):
                patient = hospital.patients[patient_choice]
                doctor = hospital.doctors[doc_choice]
                appointment_time = input("Enter appointment date and time (e.g., 2025-03-10 10:00): ")
                hospital.schedule_appointment(patient, doctor, appointment_time)
            else:
                print("Invalid selection!")
        # viewing all patients
        elif choice == "5":
            hospital.get_all_patients()
        ## viewing doctors and patients
        elif choice == "6":
            hospital.get_doctor_patients()
        # viewing all appointments
        elif choice == "7":
            hospital.get_patient_appointments()
        ## exiting system
        elif choice == "8":
            print("Exiting system...")
            break

        else:
            print("Invalid choice! Please try again.")

process()



