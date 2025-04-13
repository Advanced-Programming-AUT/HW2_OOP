class Person:
    def __init__(self, first_name, last_name, id, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.first_name} {self.last_name}\nID: {self.id}\nAge: {self.age}\nGender: {self.gender}"


class Patient(Person):
    def __init__(self, first_name, last_name, id, age, gender, disease, doctor):
        super().__init__(first_name, last_name, id, age, gender)
        self.disease = disease
        self.doctor = doctor

    def get_patient_details(self):
        return f"{self.get_details()}\nDisease: {self.disease}\nAssigned Doctor: {self.doctor.first_name} {self.doctor.last_name}"


class Doctor(Person):
    def __init__(self, first_name, last_name, id, age, gender, specialization):
        super().__init__(first_name, last_name, id, age, gender)
        self.specialization = specialization
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_doctor_details(self):
        patient_names = "\n    - ".join([p.first_name + " " + p.last_name for p in self.patients])
        return f"{self.get_details()}\nSpecialization: {self.specialization}\nPatients:\n    - {patient_names if patient_names else 'No patients'}"


class Nurse(Person):
    def __init__(self, first_name, last_name, id, age, gender, department):
        super().__init__(first_name, last_name, id, age, gender)
        self.department = department

    def get_nurse_details(self):
        return f"{self.get_details()}\nDepartment: {self.department}"


class Appointment:
    def __init__(self, patient, doctor, appointment_time, status="Scheduled"):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.status = status

    def cancel_appointment(self):
        self.status = "Canceled"

    def get_appointment_details(self):
        return f"Patient: {self.patient.first_name} {self.patient.last_name}\nDoctor: {self.doctor.first_name} {self.doctor.last_name}\nDate and Time: {self.appointment_time}\nStatus: {self.status}"


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.nurses = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_nurse(self, nurse):
        self.nurses.append(nurse)

    def schedule_appointment(self, patient, doctor, appointment_time):
        appointment = Appointment(patient, doctor, appointment_time)
        self.appointments.append(appointment)
        doctor.add_patient(patient)
        return "Appointment scheduled successfully."

    def get_all_patients(self):
        return "\n".join([p.get_patient_details() for p in self.patients])

    def get_doctor_patients(self, doctor):
        return doctor.get_doctor_details()

    def get_patient_appointments(self, patient):
        return "\n".join([a.get_appointment_details() for a in self.appointments if a.patient == patient])


# Test Cases
hospital = Hospital()

doctor1 = Doctor("Amir", "Jalali", "D001", 40, "Male", "Cardiology")
hospital.add_doctor(doctor1)

patient1 = Patient("Parsa", "Mohebian", "P001", 30, "Female", "Heart Disease", doctor1)
hospital.add_patient(patient1)
doctor1.add_patient(patient1)

nurse1 = Nurse("Sarah", "Mohammadi", "N001", 28, "Female", "Cardiology")
hospital.add_nurse(nurse1)

hospital.schedule_appointment(patient1, doctor1, "2025-03-10 10:00")

print("Doctor Details:")
print(doctor1.get_doctor_details())
print("\nPatient Details:")
print(patient1.get_patient_details())
print("\nNurse Details:")
print(nurse1.get_nurse_details())
print("\nAppointments:")
print(hospital.get_patient_appointments(patient1))
