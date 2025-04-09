class Person(object):
    def __init__(self, first_name, last_name, person_id, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.id = person_id
        self.age = age
        self.gender = gender

class Patient(Person):
    def __init__(self, first_name, last_name, person_id, age, gender, disease, doctor):
        super().__init__(first_name, last_name, person_id, age, gender)
        self.disease = disease
        self.doctor = doctor

    def get_patient_details(self):
        return f"Patient Details:\nName: {self.first_name} {self.last_name}\nID: {self.id}\nAge: {self.age}\nGender: {self.gender}\nDisease: {self.disease}\nAssigned Doctor: {self.doctor.first_name} {self.doctor.last_name}"

class Doctor(Person):
    def __init__(self, first_name, last_name, person_id, age, gender, specialization):
        super().__init__(first_name, last_name, person_id, age, gender)
        self.specialization = specialization
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_doctor_details(self):
        patient_names = [f"{p.first_name} {p.last_name}" for p in self.patients]
        return f"Doctor Details:\nName: Dr. {self.first_name} {self.last_name}\nID: {self.id}\nAge: {self.age}\nGender: {self.gender}\nSpecialization: {self.specialization}\nPatients: {', '.join(patient_names)}"

class Nurse(Person):
    def __init__(self, first_name, last_name, person_id, age, gender, department):
        super().__init__(first_name, last_name, person_id, age, gender)
        self.department = department

    def assist_patient(self):
        return f"{self.first_name} {self.last_name} is assisting a patient in {self.department} department."

    def get_nurse_details(self):
        return f"Nurse Details:\nName: {self.first_name} {self.last_name}\nID: {self.id}\nAge: {self.age}\nGender: {self.gender}\nDepartment: {self.department}"

class Appointment(object):
    def __init__(self, patient, doctor, time):
        self.patient = patient
        self.doctor = doctor
        self.time = time
        self.status = "Scheduled"

    def schedule_appointment(self):
        self.status = "Scheduled"

    def cancel_appointment(self):
        self.status = "Canceled"

    def get_appointment_details(self):
        return f"Appointment:\nPatient: {self.patient.first_name} {self.patient.last_name}\nDoctor: Dr. {self.doctor.first_name} {self.doctor.last_name}\nDate and Time: {self.time}\nStatus: {self.status}"

class Hospital(object):
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.nurses = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully.")
        print(patient.get_patient_details())

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print("Doctor added successfully.")
        print(doctor.get_doctor_details())

    def add_nurse(self, nurse):
        self.nurses.append(nurse)
        print("Nurse added successfully.")
        print(nurse.get_nurse_details())

    def get_patient_appointments(self, patient):
        for appo in self.appointments:
            if appo.patient == patient:
                print(appo.get_appointment_details())

    def get_doctor_patients(self, doctor):
        print(f"Patients of Dr. {doctor.first_name} {doctor.last_name}:")
        for patient in doctor.patients:
            print(f"- {patient.first_name} {patient.last_name}")

    def get_all_patients(self):
        for patient in self.patients:
            print(patient.get_patient_details())

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)
        print("Appointment scheduled successfully.")
        print(appointment.get_appointment_details())
