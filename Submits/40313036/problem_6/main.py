class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Gender: {self.gender}"

class Patient(Person):
    def __init__(self, first_name, last_name, age, gender, patient_id, illness):
        super().__init__(first_name, last_name, age, gender)
        self.patient_id = patient_id
        self.illness = illness
        self.assigned_doctor = None

    def get_details(self):
        doctor_name = f"Dr. {self.assigned_doctor.first_name} {self.assigned_doctor.last_name}" if self.assigned_doctor else "No doctor assigned"
        return f"{super().get_details()}, ID: {self.patient_id}, Illness: {self.illness}, Doctor: {doctor_name}"

class Doctor(Person):
    def __init__(self, first_name, last_name, age, gender, doctor_id, specialty):
        super().__init__(first_name, last_name, age, gender)
        self.doctor_id = doctor_id
        self.specialty = specialty
        self.patients = {}

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient
        patient.assigned_doctor = self
        return f"Patient {patient.first_name} assigned to Dr. {self.first_name}"

    def get_details(self):
        patient_list = ", ".join([f"{p.first_name} {p.last_name}" for p in self.patients.values()]) or "No patients"
        return f"{super().get_details()}, ID: {self.doctor_id}, Specialty: {self.specialty}, Patients: {patient_list}"

class Nurse(Person):
    def __init__(self, first_name, last_name, age, gender, nurse_id, department):
        super().__init__(first_name, last_name, age, gender)
        self.nurse_id = nurse_id
        self.department = department

    def assist_patient(self, patient):
        return f"Nurse {self.first_name} is assisting {patient.first_name}"

    def get_details(self):
        return f"{super().get_details()}, ID: {self.nurse_id}, Department: {self.department}"

class Appointment:
    def __init__(self, patient, doctor, time):
        self.patient = patient
        self.doctor = doctor
        self.time = time
        self.active = True

    def cancel(self):
        self.active = False
        return f"Appointment with {self.patient.first_name} on {self.time} canceled"

    def __str__(self):
        status = "Active" if self.active else "Canceled"
        return f"{self.patient.first_name} with Dr. {self.doctor.first_name} on {self.time} - {status}"

class Hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.nurses = {}
        self.appointments = []

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient
        return f"Patient {patient.first_name} added"

    def add_doctor(self, doctor):
        self.doctors[doctor.doctor_id] = doctor
        return f"Doctor {doctor.first_name} added"

    def add_nurse(self, nurse):
        self.nurses[nurse.nurse_id] = nurse
        return f"Nurse {nurse.first_name} added"

    def schedule_appointment(self, patient, doctor, time):
        appt = Appointment(patient, doctor, time)
        self.appointments.append(appt)
        return f"Scheduled: {appt}"

    def get_all_patients(self):
        if not self.patients:
            return "No patients"
        return "\n".join([p.get_details() for p in self.patients.values()])

    def get_doctor_patients(self, doctor):
        if not doctor.patients:
            return "No patients assigned"
        return "\n".join([p.get_details() for p in doctor.patients.values()])

    def get_patient_appointments(self, patient):
        appts = [a for a in self.appointments if a.patient == patient]
        if not appts:
            return "No appointments"
        return "\n".join([str(a) for a in appts])

    def find_doctor(self, doctor_id):
        return self.doctors.get(doctor_id)

    def find_patient(self, patient_id):
        return self.patients.get(patient_id)

    def find_nurse(self, nurse_id):
        return self.nurses.get(nurse_id)

def validate_gender(gender):
    gender = gender.lower()
    return gender.capitalize() if gender in ("male", "female") else None

