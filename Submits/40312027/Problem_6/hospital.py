from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, person_id, name, phone, address):
        self.person_id = person_id
        self.name = name
        self.phone = phone
        self.address = address

    @abstractmethod
    def get_info(self):
        pass

class Patient(Person):
    def __init__(self, person_id, name, phone, address, age, gender):
        super().__init__(person_id, name, phone, address)
        self.age = age
        self.gender = gender
        self.medical_history = []
        self.balance = 0

    def add_medical_record(self, record):
        self.medical_history.append(record)

    def make_payment(self, amount):
        self.balance -= amount

    def get_info(self):
        return f"Patient {self.name}, Age: {self.age}, Gender: {self.gender}, Balance: ${self.balance}"

class Doctor(Person):
    def __init__(self, person_id, name, phone, address, specialty, available_times):
        super().__init__(person_id, name, phone, address)
        self.specialty = specialty
        self.available_times = available_times

    def get_info(self):
        return f"Dr. {self.name}, Specialty: {self.specialty}"

class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.is_cancelled = False

    def cancel_appointment(self):
        self.is_cancelled = True

    def get_info(self):
        status = "Cancelled" if self.is_cancelled else "Scheduled"
        return f"Appointment for {self.patient.name} with {self.doctor.name} on {self.date} at {self.time} - Status: {status}"

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, patient, doctor, date, time):
        if time in doctor.available_times:
            appointment = Appointment(patient, doctor, date, time)
            self.appointments.append(appointment)
            return appointment
        return None

    def get_person_by_id(self, person_id):
        for person in self.patients + self.doctors:
            if person.person_id == person_id:
                return person
        return None


def get_input(prompt):
    return input(prompt)


hospital = Hospital()
while True:
    print("\nHospital Management System")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Schedule Appointment")
    print("4. View Appointments")
    print("5. Exit")
    request = get_input("Enter your request please : ")

    if request == "1":
        p = Patient(get_input("ID: "), get_input("Name: "), get_input("Phone: "), get_input("Address: "), get_input("Age: "), get_input("Gender: "))
        hospital.add_patient(p)
        print("Patient  is added successfully.")
    elif request == "2":
        d = Doctor(get_input("ID: "), get_input("Name: "), get_input("Phone: "), get_input("Address: "), get_input("Specialty: "), get_input("Available Times (comma separated): ").split(','))
        hospital.add_doctor(d)
        print("Doctor  is added successfully.")
    elif request == "3":
        patient = hospital.get_person_by_id(get_input("Patient ID: "))
        doctor = hospital.get_person_by_id(get_input("Doctor ID: "))
        if patient and doctor:
            appt = hospital.schedule_appointment(patient, doctor, get_input("Date: "), get_input("Time: "))
            print(appt.get_info() if appt else "Doctor  is not available.")
        else:
            print(" patient or doctor_id is not available,try again please...   ")
    elif request == "4":
        for appt in hospital.appointments:
            print(appt.get_info())
    elif request == "5":
        break
    else:
        print("  please try again...")


