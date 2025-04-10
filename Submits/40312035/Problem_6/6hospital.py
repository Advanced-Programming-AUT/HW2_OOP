class Person:
    def __init__(self , first_name , last_name , id , age , gender):
        self._first_name = first_name
        self._last_name = last_name
        self._id = id
        self._age = age
        self._gender = gender
    def person_identity(self):
        identity = {'f_name' : self._first_name , 'l_name' : self._last_name ,
                    'id' : self._id , 'age' : self._age , 'gender' : self._gender}
        return identity
    def get_name(self):
        return f"{self._first_name} {self._last_name}"
    
    


class Patient(Person):
    def __init__(self , first_name , last_name , id , age , gender , disease , doctor):
        super().__init__(first_name , last_name , id , age , gender)
        self._disease = disease
        self._doctor = doctor
    def change_doctor_for_this_patient(self , doctor):
        self._doctor = doctor
    def get_patient_details(self):
        a = self.person_identity()
        a['desease'] = self._disease
        a['doctor'] = self._doctor.get_name()
        return a
    



class Doctor(Person):
    def __init__(self , first_name , last_name , id , age , gender , specialization):
        super().__init__(first_name , last_name , id , age , gender)
        self.specialization = specialization
        self._patients = []
    def add_patient(self , patient):
        self._patients.append(patient)
        patient.change_doctor_for_this_patient(patient , self)
    def get_doctor_details(self):
        a = self.person_identity()
        a['specialization'] : self.specialization ; a['patients'] : [ i.get_full_name() for i in self._patients ]
        return a
class Nurse (Person):
    def __init__(self , first_name , last_name , id , age , gender , department):
        super().__init__(first_name , last_name , id , age , gender)
        self._department = department
    def assist_patient(self , patient):
        print(f'assisting {patient.person_identity()}')
    def get_nurse_details(self):
        a = self.get_basic_details() ; a['department'] = self._department
        return a
    





class Appointment:
    def __init__(self , patient , doctor , appointment_time , status = 'done'):
        self._patient = patient ; self._doctor = doctor
        self._appointment_time = appointment_time
        self._status = status
    def schedule_appointment(self):
        n=input('time?')
        print(f'{self._patient} had an appointment with {self._doctor} at {n}')
    def cancel(self):
        self._status = 'has been canceled'
    def get_appointment_details(self):
        return {'patient': self._patient.person_identity() , 'doctor': self._doctor.person_identity(),
            'time': self._appointment_time , 'status': self._status }
    





class Hospital:
    def __init__(self):
        self._patients = []
        self._doctors = []
        self._nurses = []
        self._appointments = []
    def add_patient(self , patient):
        self._patients.append(patient)
        print("added")
    def add_doctor(self , doctor):
        self._doctors.append(doctor)
        print("added")
    def add_nurse(self , nurse):
        self._nurses.append(nurse)
        print("added")
    def schedule_appointment(self , patient , doctor , time):
        appointment = Appointment(patient , doctor , time)
        self._appointments.append( appointment)
        print("done")


        print(self.get_appointment_details())
    def get_all_patients(self):
        return [i.get_patient_details() for i in self._patients]








"""hospital = Hospital()
doctor = Doctor("Amir" , "Jalali" , "D001" , 40 , "Male" , "Cardiology")
hospital.add_doctor(doctor)
patient = Patient("Parsa" , "Mohebian" , "P001" , 30 , "Female","Heart Disease")
hospital.add_patient(patient)
doctor.add_patient(patient)
nurse = Nurse("Sarah" , "Mohammadi" , "N001",28,"Female","Cardiology")
hospital.add_nurse(nurse)
"""