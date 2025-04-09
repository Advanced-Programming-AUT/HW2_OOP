from abc import ABC
class Person(ABC):
    def __init__(self,first_name,last_name,ID,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.age = age
        self.gender= gender

class Patient(Person):
    def __init__(self,first_name,last_name,ID,age,gender,disease,doctor):
        super().__init__(first_name,last_name,ID,age,gender)
        self.disease = disease
        self.doctor = doctor
    def get_patient_details(self):
        print(f"Patient deatels\n\
        Name: {self.first_name}{self.last_name}\n\
        ID: {self.ID}\n\
        Age: {self.age}\n\
        Gender: {self.gender}\n\
        Disease: {self.disease}\n\
        Assigned Doctor: Dr.{self.doctor.firstname} {self.doctor.lastname}")

class Doctor(Person):
    def __init__(self,first_name,last_name,ID,age,gender,specialization):
        super().__init__(first_name,last_name,ID,age,gender)
        self.specialization = specialization
        self.patients = []
    
    def add_patient(self,patient):
        self.patients.append(patient)

    def get_doctor_details(self):
        print(f"Doctor deatels:\n\
        Name: Dr.{self.first_name}{self.last_name}\n\
        ID: {self.ID}\n\
        Age: {self.age}\n\
        Gender: {self.gender}\n\
        Specialization: {self.specialization}")       
        print("Patients:")
        for patient in self.patients:
            print(f" -{patient.first_name}{patient.last_name}")

class Nurse(Person):
    def __init__(self,first_name,last_name,ID,age,gender,department):
        super().__init__(first_name,last_name,ID,age,gender)
        self.department = department
        
    def assist_patient(self):pass#dar doc task moshkhasi nadarad!

    def get_nurse_details(self):
        print(f"Nurse deatels:\n\
        Name: {self.first_name}{self.last_name}\n\
        ID: {self.ID}\n\
        Age: {self.age}\n\
        Gender: {self.gender}\n\
        Department: {self.department}")


class Appointment():
    def __init__(self,patient,doctor,status,ID):
        self.patient = patient
        self.doctor = doctor
        self.status = status
        self.ID = ID
    
    def appointment_schedule(self,time_appointment):
        self.time_appointment = time_appointment


    def appointment_cancel(self):
        self.status = "Canceled"
        print(f"Appointment Canceled:(ID:{self.ID})\n\
        Patient: {self.patient.first_name} {self.patient.last_name}\n\
        Doctor: Dr.{self.doctor.first_name} {self.doctor.last_name}\n\
        Date and Time: {self.time_appointment}\n\
        Status: {self.status}")
    def get_appointment_details(self):
        print(f"Appointment deatels:(ID:{self.ID})\n\
        Patient: {self.patient.first_name} {self.patient.last_name}\n\
        Doctor: Dr.{self.doctor.first_name} {self.doctor.last_name}\n\
        Date and Time: {self.time_appointment}\n\
        Status: {self.status}")


class Hospital():
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.nurses = []
        self.appointments =[]
    
    def add_patient(self,new_patient):
        self.patients.append(new_patient)
        new_doctor.doctor.add_patient(new_patient)
        print(f"Patient added successfully:\n\
        Name: {new_patient.first_name}{new_patient.last_name}\n\
        ID: {new_patient.ID}\n\
        Age: {new_patient.age}\n\
        Gender: {new_patient.gender}\n\
        Disease: {new_patient.disease}\n\
        Assigned Doctor: Dr.{new_patient.doctor.firstname} {new_patient.doctor.lastname}")
    def add_doctor(self,new_doctor):
        self.doctors.append(new_doctor)
        print(f"Doctor added successfully:\n\
        Name: Dr.{new_doctor.first_name}{new_doctor.last_name}\n\
        ID: {new_doctor.ID}\n\
        Age: {new_doctor.age}\n\
        Gender: {new_doctor.gender}\n\
        Specialization: {new_doctor.specialization}")

    def add_nurse(self,new_nurse):
        self.nurses.append(new_nurse)
        print(f"Nurse added successfully:\n\
        Name: {new_nurse.first_name}{new_nurse.last_name}\n\
        ID: {new_nurse.ID}\n\
        Age: {new_nurse.age}\n\
        Gender: {new_nurse.gender}\n\
        Department: {new_nurse.department}")
    def appointment_schedule(self,appointment):
        self.appointments.append(appointment)
        print(f"Appointment scheduled successfully:(ID:{appointment.ID})\n\
        Patient: {appointment.patient.first_name} {appointment.patient.last_name}\n\
        Doctor: Dr.{appointment.doctor.first_name} {appointment.doctor.last_name}\n\
        Date and Time: {appointment.time_appointment}\n\
        Status: {appointment.status}")

    def get_all_appointments(self):
        print("All Appointments:")
        for appointment in self.appointments:
            print(f"Patient: {appointment.patient.first_name} {appointment.patient.last_name}, Doctor: Dr.{appointment.doctor.first_name} {appointment.doctor.last_name}, Date: {appointment.date}, Status: {appointment.status}")

    def get_all_doctors(self):
        print("All Doctors:")
        for doctor in self.docotrs:
            print(f"Dr.{doctor.first_name}{doctor.last_name}, ID: {doctor.ID}, Specialization: {doctor.specialization}")


    def get_all_patients(self):
        print("All Patiens:")
        for patient in self.patients:
            print(f"Dr.{patient.first_name}{patient.last_name}, ID: {patient.ID}, Doctor: {patient.doctor.first_name} {patient.doctor.last_name}")

    def get_doctor_patients(self,doctor_id):
        for doctor in self.doctors:
            if doctor.ID == doctor_id:
                print("Patients:")
                for patient in doctor.patients:
                    print(f" -{patient.first_name}{patient.last_name}")

    def get_patient_appointments(self,patient):
        for appointment in self.appointments:
            if appointment.patient == patient:
                appointment.get_appointment_details()



    
while(True):
    hospital = Hospital()
    command = input().split()
    match command[0]:
        case "ADD_DOCTOR":
            new_doctor = Doctor(command[1],command[2],command[3],command[4],command[5],command[6])
            hospital.add_doctor(new_doctor)
        case "ADD_PATIENT":
            for doctor in hospital.doctors:
                if doctor.first_name == command[6] and doctor.last_name == command[7]:
                    doctor_p = doctor
                new_patient = Patient(command[1],command[2],command[3],command[4],command[5],doctor_p)
                hospital.add_patient(new_patient)

        case "ADD_NURSE":
                new_nurse = Patient(command[1],command[2],command[3],command[4],command[5],command[6])
                hospital.add_nurse(new_nurse)            

        case "ADD_Appointment":
            for patient in hospital.patients:
                if patient.first_name == command[1] and patient.last_name == command[2]:
                    patient_p = patient
            for doctor in hospital.doctors:
                if doctor.first_name == command[3] and doctor.last_name == command[4]:
                    doctor_p = doctor
            new_appointment = Appointment(patient_p,doctor_p ,"Scheduled")
            new_appointment.appointment_schedule(" ".join(command[3],command[4]))
            hospital.appointment_schedule(new_appointment)

        case "GET_DOCTOR":
            for doctor in hospital.doctors:
                if doctor.ID == command[1]:
                    doctor.get_doctor_details()

        case "GET_PATIENT":
            for patient in hospital.patients:
                if patient.ID == command[1]:
                    patient.get_patient_details()


        case "Cancel_Appointment":
            for appointment in hospital.appointments:
                if appointment.ID == command[1]:
                    appointment.appointment_cancel()

        case "ALL_APPOINTMENTS":
            hospital.get_all_appointments()

        case "ALL_DOCTORS":
            hospital.get_all_doctors()

