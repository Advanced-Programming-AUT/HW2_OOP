class Person:
    def __init__(self,first_name,last_name,idd,age,gender):
        self.first=first_name
        self.last=last_name
        self.idd = idd
        self.age=age
        self.gender=gender

class Doctor(Person):
    def __init__(self, first_name, last_name, idd, age, gender,specialization,patients:list,appointments:list):
        super().__init__(first_name, last_name, idd, age, gender)
        self.spec=specialization
        self.patient_l=patients
        self.appointments=appointments
        H.add_doctor(first_name, last_name, idd, age, gender,specialization,patients,appointments)
    def add_patient_to_dr(self,first_n,last_n,ID,age,gender,malady):
        self.patient_l.append(Patient(first_n,last_n,ID,age,gender,malady,self))

    def get_doctor_details(self):
        print(f'name = {self.first} {self.last} / {self.gender} with id: {self.idd} and age {self.age}')
        print(f"the doctor's specialized in {self.spec} and is treating the following patients:")
        for item in self.patient_l:
            print(f'{item.first} {item.last}')


class Patient(Person):
    def __init__(self, first_name, last_name, idd, age, gender,disease,doctor:Doctor):
        super().__init__(first_name, last_name, idd, age, gender)
        self.disease=disease
        self.doctor=doctor
        H.add_patient(first_name, last_name, idd, age, gender,disease,doctor)
        doctor.add_patient_to_dr(first_name,last_name, idd, age, gender,disease)
    def get_patient_details(self):
        print(f'name = {self.first} {self.last} / {self.gender} with id: {self.idd} and age {self.age}' )
        print(f'affected by disease : {self.disease} and is being treated by: {self.doctor.first} {self.doctor.last}')

class Nurse(Person):
    def __init__(self, first_name, last_name, idd, age, gender,department):
        super().__init__(first_name, last_name, idd, age, gender)
        self.depart=department
        self.assist_patient=[]
        H.add_nurse(first_name, last_name, idd, age, gender,department)
    def assist_patient(self,p:Patient):
        flag=0
        for item in H.patients:
            if item == p:
                self.assist_patient.append(item)
                flag = 1
        if flag==0:
            print('Invalid patients')

    def get_nurse_details(self):
        print(f'name = {self.first} {self.last} / {self.gender} with id: {self.idd} and age {self.age}')
        print(f'is nursing at department: {self.depart}')

class Appointment:
    def __init__(self,patient:Patient,dr:Doctor,appointment_time):
        self.patient=patient
        self.doctor=dr
        self.time = appointment_time
        self.status=''
    @property
    def doctor(self):
        return self._doctor
    @doctor.setter
    def doctor(self, dr):
        if self.patient.doctor == dr:
            self._doctor = dr
        else:
            print('making an appointment with a doctor who is not treating this patient')
            self._doctor = dr

    def schedule_appointment(self):
        flag = 1
        for item in self.doctor.appointments:
            if item == self.time:
                print('the specified time is already assigned to other appointments')
                flag = 0
                self.status='Not successful'
        if flag != 0:
            self.doctor.appointments.append((self.patient,self.time))
            print(f'Scheduled appointment at {self.time}')
            self.status='Scheduled successfully'
            H.add_appointment(self.patient,self.doctor,self.time,self.status)
    def cancel_appointment(self):
        for item in self.doctor.appointments:
            if item[1] == self.time and item[0] == self.patient:
                self.doctor.appointments.remove((self.patient,self.time))
                H.appointments.remove(self)
                print(f'appointment at {self.time} with dr {self.doctor.last}/ patient {self.patient.last} is cancelled')

    def get_appointment_details(self):
        print(f'name = patient: {self.patient.first}{self.patient.last}, doctor: {self.doctor.first} / {self.doctor.last} at: {self.time} with status: {self.status}')

class Hospital:
    def __init__(self):
        self.patients=[]
        self.doctors=[]
        self.nurses=[]
        self.appointments=[]
    def add_patient(self,first,last,idd,age,gender,illness,doctor):
        self.patients.append(Patient(first,last,idd,age,gender,illness,doctor))
    def add_doctor(self,first,last,idd,age,gender,spec,patients,appointments):
        self.doctors.append(Doctor(first,last,idd,age,gender,spec,patients,appointments))
    def add_nurse(self,first,last,idd,age,gender,department,assisting):
        self.nurses.append(Nurse(first,last,idd,age,gender,department,assisting))
    def add_appointment(self,patient,doctor,appointment_time,status):
        self.appointments.append(Appointment(patient,doctor,appointment_time,status))
    def schedule_appointment(self,p:Patient,dr:Doctor,time):
        if ~(p in self.patients and dr in self.doctors):
            print('no such doctor/patient defined')
        x = Appointment(p, dr, time)
        self.appointments.append(x)
        x.schedule_appointment()
        print(f'Done : {x.status}')

    def get_patient_appointments(self,p:Patient):
        for item in self.appointments:
            if item.patient == p:
                print(f'doctor :{item.doctor.first} {item.doctor.last} / time: {item.time}')

    def get_doctor_patients(self):
        for item in self.doctors:
            print(f"{item.first} {item.last} is treating the following patients: ",end='')
            for t in item.patient_l:
                print(f'{t.first} {t.last}',sep=' ')

    def get_all_patients(self):
        for item in self.patients:
            item.get_patient_details()

H=Hospital()
