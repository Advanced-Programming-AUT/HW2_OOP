class Person:
    def __init__(self, first_name, last_name, person_id, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.person_id = person_id
        self.age = age
        self.gender = gender


class Patient(Person):
    def __init__(self, first_name, last_name, person_id, age, gender, disease):
        super().__init__(first_name, last_name, person_id, age, gender)
        self.disease = disease
        self.doctor = None

    def assign_doctor(self, doctor):
        self.doctor = doctor
        doctor.add_patient(self)

    def get_patient_details(self):
        if self.doctor:
            doctor_name = f"{self.doctor.first_name} {self.doctor.last_name}"
        else:
            doctor_name = "Not Assigned"

        return f"Patient: {self.first_name} {self.last_name}\nID: {self.person_id}\nAge: {self.age}\nGender: {self.gender}\nDisease: {self.disease}\nAssigned Doctor: {doctor_name}\n"


class Doctor(Person):
    def __init__(self, first_name, last_name, person_id, age, gender, specialization):
        super().__init__(first_name, last_name, person_id, age, gender)
        self.specialization = specialization
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_doctor_details(self):
        if self.patients:
            patient_list = ", ".join(
                [p.first_name + " " + p.last_name for p in self.patients])
        else:
            patient_list = "No Patients"

        return f"Doctor: {self.first_name} {self.last_name}\nID: {self.person_id}\nAge: {self.age}\nGender: {self.gender}\nSpecialization: {self.specialization}\nPatients: {patient_list}\n"


class Nurse(Person):
    def __init__(self, first_name, last_name, person_id, age, gender, department):
        super().__init__(first_name, last_name, person_id, age, gender)
        self.department = department

    def get_nurse_details(self):
        return f"Name: {self.first_name} {self.last_name}\nID: {self.person_id}\nAge: {self.age}\nGender: {self.gender}\nDepartment: {self.department}\n"


class Appointment:
    def __init__(self, patient, doctor, appointment_time):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time

    def get_appointment_details(self):
        return f"Appointment:\nPatient: {self.patient.first_name} {self.patient.last_name}\nDoctor: {self.doctor.first_name} {self.doctor.last_name}\nTime: {self.appointment_time}\n"


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.nurses = []
        self.appointments = []

    def process_command(self, command):
        parts = command.split()
        if not parts:
            print("Invalid command!")
            return

        action = parts[0].lower()

        if action == "add":
            entity = parts[1].lower()
            first_name = parts[2]
            last_name = parts[3]
            person_id = parts[4]
            age = parts[5]
            gender = parts[6]

            if entity == "doctor" and len(parts) >= 8:
                specialization = parts[7]
                doctor = Doctor(first_name, last_name, person_id,
                                age, gender, specialization)
                self.doctors.append(doctor)

                if len(parts) > 8:
                    patient_ids = parts[8:]
                    for pid in patient_ids:
                        for patient in self.patients:
                            if patient.person_id == pid:
                                doctor.add_patient(patient)

                print("\nDoctor added successfully:\n" +
                      doctor.get_doctor_details())

            elif entity == "patient" and len(parts) >= 8:
                disease = parts[7]
                patient = Patient(first_name, last_name,
                                  person_id, age, gender, disease)
                self.patients.append(patient)

                if len(parts) > 8:
                    doctor_id = parts[8]
                    for doctor in self.doctors:
                        if doctor.person_id == doctor_id:
                            patient.assign_doctor(doctor)

                print("\nPatient added successfully:\n" +
                      patient.get_patient_details())

            elif entity == "nurse" and len(parts) >= 8:
                department = parts[7]
                nurse = Nurse(first_name, last_name, person_id,
                              age, gender, department)
                self.nurses.append(nurse)

                print("\nNurse added successfully:\n" +
                      nurse.get_nurse_details())

        elif action == "schedule":
            if len(parts) < 5:
                print(
                    "Invalid format! Example: schedule appointment p001 d002 2025-04-01 10:00")
                return

            patient_id = parts[2]
            doctor_id = parts[3]
            appointment_time = " ".join(parts[4:])

            patient = None
            doctor = None

            for p in self.patients:
                if p.person_id == patient_id:
                    patient = p
                    break

            for d in self.doctors:
                if d.person_id == doctor_id:
                    doctor = d
                    break

            if not patient:
                print("Patient not found.")
                return
            if not doctor:
                print("Doctor not found.")
                return

            appointment = Appointment(patient, doctor, appointment_time)
            self.appointments.append(appointment)

            print("\nAppointment scheduled successfully:\n" +
                  appointment.get_appointment_details())

        elif action == "cancel":
            if len(parts) < 4:
                print("Invalid format! Example: cancel appointment p001 d002")
                return

            patient_id = parts[2]
            doctor_id = parts[3]

            appointment_to_cancel = None
            for appointment in self.appointments:
                if appointment.patient.person_id == patient_id and appointment.doctor.person_id == doctor_id:
                    appointment_to_cancel = appointment
                    break

            if appointment_to_cancel:
                self.appointments.remove(appointment_to_cancel)
                print(
                    f"Appointment between {appointment_to_cancel.patient.first_name} and {appointment_to_cancel.doctor.first_name} has been cancelled.")
            else:
                print("No matching appointment found.")

        elif action == "view":
            if len(parts) < 2:
                print("Invalid format! Example: view patients")
                return

            entity = parts[1].lower()

            if entity == "patients":
                if self.patients:
                    for p in self.patients:
                        print(
                            f"{p.first_name} {p.last_name} {p.person_id} {p.disease}")
                else:
                    print("No Patients Available")

            elif entity == "doctors":
                if self.doctors:
                    for d in self.doctors:
                        print(
                            f"{d.first_name} {d.last_name} {d.person_id} {d.specialization}")
                else:
                    print("No Doctors Available")

            elif entity == "appointments":
                if self.appointments:
                    for a in self.appointments:
                        print(
                            f"{a.patient.first_name} {a.patient.last_name} - {a.doctor.first_name} {a.doctor.last_name} - {a.appointment_time}")
                else:
                    print("No Appointments Available")

            elif entity == "nurses":
                if self.nurses:
                    for n in self.nurses:
                        print(
                            f"{n.first_name} {n.last_name} {n.person_id} {n.department}")
                else:
                    print("No Nurses Available")

        else:
            print("Invalid command!")


if __name__ == "__main__":
    hospital = Hospital()

    print("Welcome to the Hospital Management System!")
    print("To exit, type: exit")

    while True:
        command = input("\nEnter command: ")
        if command.lower() == "exit":
            break
        hospital.process_command(command)
