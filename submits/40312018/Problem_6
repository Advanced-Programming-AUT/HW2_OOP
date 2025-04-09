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

    def get_details(self):
        return super().get_details() + f"\nDisease: {self.disease}\nAssigned Doctor: {self.doctor.first_name} {self.doctor.last_name}"


class Doctor(Person):
    def __init__(self, first_name, last_name, id, age, gender, specialization):
        super().__init__(first_name, last_name, id, age, gender)
        self.specialization = specialization
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_details(self):
        patient_names = ', '.join([f"{p.first_name} {p.last_name}" for p in self.patients])
        return super().get_details() + f"\nSpecialization: {self.specialization}\nPatients:\n   - {patient_names}"

    def all_doctors(self):
        return f"{self.first_name} {self.last_name}, ID: {self.id}, Specialization: {self.specialization}"


class Nurse(Person):
    def __init__(self, first_name, last_name, id, age, gender, department):
        super().__init__(first_name, last_name, id, age, gender)
        self.department = department

    def assist_patient(self, patient):
        print(f"{self.first_name} {self.last_name} is assisting patient {patient.first_name} {patient.last_name}.")

    def get_details(self):
        return super().get_details() + f"\nDepartment: {self.department}"


class Appointment:
    def __init__(self, patient, doctor, appointment_time, status="Scheduled"):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.status = status

    def schedule_appointment(self):
        self.status = "Scheduled"

    def cancel_appointment(self):
        self.status = "Canceled"

    def get_appointment_details(self):
        return f"Patient: {self.patient.first_name} {self.patient.last_name}\nDoctor: {self.doctor.first_name} {self.doctor.last_name}\nDate and Time: {self.appointment_time}\nStatus: {self.status}"

    def all_appointments(self):
        return f"Patient: {self.patient.first_name} {self.patient.last_name}, Doctor: {self.doctor.first_name} {self.doctor.last_name}. Date: {self.appointment_time}"
class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.nurses = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient added successfully:\n{patient.get_details()}")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor added successfully:\n{doctor.get_details()}")

    def add_nurse(self, nurse):
        self.nurses.append(nurse)
        print(f"Nurse added successfully:\n{nurse.get_details()}")

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)
        appointment.schedule_appointment()
        print(f"Appointment scheduled successfully:\n{appointment.get_appointment_details()}")

    def get_all_patients(self):
        for patient in self.patients:
            print(patient.get_details())

    def get_doctor_patients(self, doctor):
        for patient in doctor.patients:
            print(patient.get_details())

    def get_patient_appointments(self, patient):
        for appointment in self.appointments:
            if appointment.patient == patient:
                print(appointment.get_appointment_details())


def main():
    hospital = Hospital()

    first_name = input()
    last_name = input()
    id = input()
    age = int(input())
    gender = input()
    specialization = input()
    doctor = Doctor(first_name, last_name, id, age, gender, specialization)
    hospital.add_doctor(doctor)

    first_name = input()
    last_name = input()
    id = input()
    age = int(input())
    gender = input()
    disease = input()
    patient = Patient(first_name, last_name, id, age, gender, disease, doctor)
    hospital.add_patient(patient)
    doctor.add_patient(patient)

    first_name = input()
    last_name = input()
    id = input()
    age = int(input())
    gender = input()
    department = input()
    nurse = Nurse(first_name, last_name, id, age, gender, department)
    hospital.add_nurse(nurse)

    appointment_time = input()
    appointment = Appointment(patient, doctor, appointment_time)
    hospital.schedule_appointment(appointment)

    print("\nPatient Details:")
    print(patient.get_details())

    print("\nDoctor Details:")
    print(doctor.get_details())

    print("\nAppointment cancelled successfully:")
    appointment.cancel_appointment()
    print(appointment.get_appointment_details())

    print("\nAll Appointments:")
    print(appointment.all_appointments())

    print("\nAll Doctors:")
    print(doctor.all_doctors())


if __name__ == "__main__":
    main()
