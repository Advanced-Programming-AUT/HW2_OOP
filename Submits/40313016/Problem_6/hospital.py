import pickle
from abc import ABC, abstractclassmethod
class Person:
    def __init__(self, name, id, age, gender):
        self.__name = name
        self.__id = id
        self.__age = age
        self.__gender = gender
    
        
class GetDetails(ABC):
    @abstractclassmethod
    def get_details(self):
        pass
    def get_name(self):
        pass
    
list_of_patients = []
list_of_doctors = []
class Patient(Person, GetDetails):
    def __init__(self, name,  id, age, gender, disease, doctor):
        self.__name = name
        self.__id = id
        self.__age = age
        self.__gender = gender
        self.__disease = disease
        self.__doctor = doctor
        for doctor in list_of_doctors:
            if doctor.get_name() == self.__doctor:
                doctor.add_patients(self)
        list_of_patients.append(self)
    def get_details(self):
        print(f"Patient Details:\nName: {self.__name}\nID: {self.__id}\nAge: {self.__age}\nGender: {self.__gender}\nDisease: {self.__disease}\nAssigned Doctor: {self.__doctor}\n")
    def get_name(self):
        return self.__name
    
class Doctor(Person, GetDetails):
    def __init__(self, name, id, age, gender, specialization):
        self.__name = name
        self.__id = id
        self.__age = age
        self.__gender = gender
        self.__specialization = specialization
        self.__list_of_patients = []
        list_of_doctors.append(self)
    def add_patients(self, patient):
        self.__list_of_patients.append(patient)
    def get_name(self):
        return self.__name
    
    def get_details(self):
        print(f"Doctor Details:\nName: {self.__name}\nID: {self.__id}\nAge: {self.__age}\nGender: {self.__gender}\nSpecialization: {self.__specialization}\nPatients:")
        for patient in self.__list_of_patients:
            print(f"  - {patient.get_name()}")
    def get_patients(self):
        for patient in  self.__list_of_patients:
            patient.get_details()
          
list_of_nurses = []      
class Nurse(Person, GetDetails):
    def __init__(self, name, id, age, gender, department):
        self.__name = name
        self.__id = id
        self.__age = age
        self.__gender = gender
        self.__department = department
        list_of_nurses.append(self)
    def get_name(self):
        return self.__name
    def get_details(self):
        print(f"Nurse Details:\nName: {self.__name}\nID: {self.__id}\nAge: {self.__age}\nGender: {self.__gender}\nDepartment: {self.__department}\n")
    def asssis_patient(self):
        pass
    
list_of_appoinments = []

class Appoinment(GetDetails):
    def __init__(self, doctor, patient, appoinment_time, number, status):
        self.__doctor = doctor
        self.__patient = patient
        self.__appoinment_time = appoinment_time
        self.__number = number
        self.__status = status
        list_of_appoinments.append(self)
    def schedule_appoinment(self, patient, doctor, data_time):
        print("Appoinment scheduled successfully:")
        print(f"Patient: {patient.get_name()}")
        print(f"Doctor: {doctor.get_name()}")
        print(f"Data and Time: {data_time}")
        print(f"Number of Appinment: {self.__number}")
        print("Status: Scheduled\n")
    def get_details(self):
        print(f"Patient: {self.__patient.get_name()}")
        print(f"Doctor: {self.__doctor.get_name()}")
        print(f"Data and Time: {self.__appoinment_time}")
        print(f"Status: {self.__status}")
        print(f"Number: {self.__number}\n")
    def canceled_appoinment(self):
        self.__status = "Canceled"
        print("Canceled appoinment successfully!\n")
    def get_appoinment(self):
        print(f"Patient: {self.__patient.get_name()}, Doctor: {self.__doctor.get_name()}, Data: {self.__appoinment_time}, Status: {self.__status}")
    def show_patient(self):
        return self.__patient
    def show_number(self):
        return self.__number
    
class Hospital:
    def __init__(self):
        self.__doctors = list_of_doctors
        self.__patients = list_of_patients
        self.__nurses = list_of_nurses
        self.__appoinments = list_of_appoinments
    def add_patient(self):
        name = input("Name: ")
        id = input("ID: ")
        age = input("Age: ")
        gender = input("Gender: ")
        disease = input("Disease: ")
        assigned_doctor = input("Assigned Doctor: ")
        patient = Patient(name, id, age, gender, disease, assigned_doctor)
        print("Patient added successfully:")
        print(f"Name: {name}\nID: {id}\nAge: {age}\nGender: {gender}\nDisease: {disease}\nAssigned doctor: {assigned_doctor}")
    def add_doctor(self):
        name = input("Name: ")
        id = input("ID: ")
        age = input("Age: ")
        gender = input("Gender: ")
        specialization = input("Specialization: ")
        doctor = Doctor(name, id, age, gender, specialization)
        print("Doctor added successfully:")
        print(f"Name: {name}\nID: {id}\nAge: {age}\nGender: {gender}\nSpecialization: {specialization}")
    def add_nurse(self):
        name = input("Name: ")
        id = input("ID: ")
        age = input("Age: ")
        gender = input("Gender: ")
        department = input("Department: ")
        nurse = Nurse(name, id, age, gender, department)
        print("Nurse added successfully:")
        print(f"Name: {name}\nID: {id}\nAge: {age}\nGender: {gender}\nDepartment: {department}")
    def schedule_appoinment(self):
        patient = input("Patient's Name: ")
        count1 = 1
        for patient1 in self.__patients:
            if patient1.get_name() == patient:
                patient = patient1
                count1 = 0
                break
        if count1:
            print("The patient not exists\n")
        else:
            doctor = input("Doctor's Name: ")
            count2 = 1
            for doctor1 in self.__doctors:
                if doctor1.get_name() == doctor:
                    doctor = doctor1
                    count2 = 0
                    break
            if count2:
                 print("The doctor not exists\n")
            else:
                appoinment_time = input("Data and time: ")
                appoinment_number = input("Number: ")
                appoinment = Appoinment(doctor1, patient1, appoinment_time, appoinment_number, "scheduled")
                print("Appoinment Added successfully:")
                appoinment.get_details()
    def get_all_patients(self):
        print("All patients:")
        for patient in self.__patients:
            patient.get_details()
    def get_all_doctors(self):
        print("All doctors:")
        for doctor in self.__doctors:
            doctor.get_details()
            print("\n")
    def get_all_nurses(self):
        print("All nurses:")
        for nurse in self.__nurses:
            nurse.get_details()
    def get_doctor_patients(self):
        for doctor in self.__doctors:
            print(f" - Dr {doctor.get_name()}:")
            doctor.get_patients()
    def get_patient_appoinment(self):
        name = input("Name of patient:")
        count_ = 1
        for patient in self.__patients:
            if patient.get_name() == name:
                count_ = 0
                patient =  patient
                break
        if count_:
            print("The Patient not exists\n")
        else:
            for appoinment in self.__appoinments:
                if appoinment.show_patient().get_name() == patient.get_name():
                    appoinment.get_details()
    def cancele_appoinment(self):
        number = input("Number of Appoinmet: ")
        for appoinment in self.__appoinments:
            if appoinment.show_number() == number:
                appoinment.canceled_appoinment()
                print("Appoinment canceled successfully:")
                appoinment.get_details()
    def get_appoinments(self):
        print("All appoinments:")
        for appoinment in list_of_appoinments:
            appoinment.get_appoinment()
            
print("Welcoum to Hospital!")
order = ""
hospital = Hospital()
while order != "12":
    print("\n1 > Add Doctor\n2 > Add Patient\n3 > Add Nurse\n4 > Schedule Appoinment\n5 > Patient Info\n6 > Doctor Info\n7 > Nurse Info\n8 > Doctor's Patient Info\n9 > Patient's Appoinment Info\n10 > Cancele Appoinment\n11 > Show aLL Appoinmnets\n12 > Exit\n")
    order = input()
    if order == "1":
        hospital.add_doctor()
    if order == "2":
        hospital.add_patient()
    if order == "3":
        hospital.add_nurse()
    if order == "4":
        hospital.schedule_appoinment()
    if order == "5":
        hospital.get_all_patients()
    if order == "6":
        hospital.get_all_doctors()
    if order == "7":
        hospital.get_all_nurses()
    if order == "8":
        hospital.get_doctor_patients()
    if order == "9":
        hospital.get_patient_appoinment()
    if order == "10":
        hospital.cancele_appoinment()
    if order == "11":
        hospital.get_appoinments()
    
    
    
    
    
    
    
    
    