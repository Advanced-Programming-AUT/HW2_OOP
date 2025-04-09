import sys, os

original_stdout = sys.stdout

os.remove('output.txt')

file1 = open('input.txt', 'r')
file2 = open('output.txt', 'a')

sys.stdout = file2

# ---------- Main Code ----------

class Person:
    def __init__(self, first_name, last_name, id, age, gender):
        self._first_name = first_name
        self._last_name = last_name
        self._id = id
        self._age = age
        self._gender = gender

    def get_details(self):
        pass

    def __str__(self):
        return f'{self._first_name} {self._last_name}'

class Patient(Person):
    ID = 0

    def __init__(self, first_name, last_name, age, gender, disease, doctor):
        Patient.ID += 1
        super().__init__(first_name, last_name, 'P' + str(Patient.ID).zfill(3), age, gender)
        self._disease = disease
        self._doctor = doctor
        self._doctor.add_patient(self)
        self._appointments = list()
        self.get_details('Patient added successfully:')

    def get_details(self, title = 'Patient Details:'):
        print(title)
        print('Name:', self._first_name, self._last_name)
        print('ID:', self._id)
        print('Age:', self._age)
        print('Gender:', self._gender)
        print('Disease:', self._disease)
        print('Assigned Doctor:', self._doctor)
        print()

    def add_appointment(self, appointment):
        self._appointments.append(appointment)

    def get_appointments(self):
        print(f'{str(self)} Appointments:')
        for appointment in self._appointments:
            appointment.get_details('')

class Doctor(Person):
    ID = 0

    def __init__(self, first_name, last_name, age, gender, specialization):
        Doctor.ID += 1
        super().__init__(first_name, last_name, 'D' + str(Doctor.ID).zfill(3), age, gender)
        self._specialization = specialization
        self._patients = list()
        self.get_details('Doctor added successfully:')

    def get_patients(self):
        if len(self._patients):
            print(f'{str(self)} Patients:')
            for patient in self._patients:
                print(f'\t- {patient}')
        print()

    def get_details(self, title = 'Doctor Details:'):
        print(title)
        print('Name: Dr.', self._first_name, self._last_name)
        print('ID:', self._id)
        print('Age:', self._age)
        print('Gender:', self._gender)
        print('Specialization:', self._specialization)
        self.get_patients()

    def add_patient(self, patient):
        print(f'{patient} assigned doctor is {str(self)} now.\n')
        self._patients.append(patient)

    def __str__(self):
        return f'Dr. {self._first_name} {self._last_name}'

class Nurse(Person):
    ID = 0

    def __init__(self, first_name, last_name, age, gender, department):
        Nurse.ID += 1
        super().__init__(first_name, last_name, 'N' + str(Nurse.ID).zfill(3), age, gender)
        self._department = department
        self.get_details('Nurse added successfully:')

    def get_details(self, title = 'Nurse Details:'):
        print(title)
        print('Name:', self._first_name, self._last_name)
        print('ID:', self._id)
        print('Age:', self._age)
        print('Gender:', self._gender)
        print('Department:', self._department)
        print()

    def assist_patient(self, patient):
        print(f'Nurse {str(self)} is helping {str(patient)} in {self._department} department now!\n')

class Appointment:
    def __init__(self, doctor, patient, time, status = 'In queue...'):
        # status is on of ['Scheduled', 'In queue...', 'Canceled']

        self._doctor = doctor
        self._patient = patient
        self._time = time
        self._status = status

        self._patient.add_appointment(self)

        self.get_details('Appointment added successfully:')

    def get_details(self, title = 'Appointment scheduled successfully:'):
        print(title)
        print('Patient:', self._patient)
        print('Doctor:', self._doctor)
        print('Date and Time:', self._time)
        print('Status:', self._status)
        print()

    def schedule(self, time):
        self._time = time
        self._status = 'Scheduled'
        self.get_details()

    def cancel(self):
        self._status = 'Canceled'
        self.get_details('Appointment canceled successfully:')

class Hospital:
    def __init__(self):
        self._patients, self._doctors, self._nurses, self._appointments = list(), list(), list(), list()

    def add_doctor(self, doctor):
        self._doctors.append(doctor)

    def get_doctor(self, doctor_id):
        doctor_id -= 1
        if doctor_id >= len(self._doctors) or doctor_id < 0:
            print('Doctor ID is incorrect!')
            return

        return self._doctors[doctor_id]

    def add_patient(self, patient):
        self._patients.append(patient)

    def get_patient(self, patient_id):
        patient_id -= 1
        if patient_id >= len(self._patients) or patient_id < 0:
            print('Patient ID is incorrect!')
            return

        return self._patients[patient_id]

    def add_nurse(self, nurse):
        self._nurses.append(nurse)

    def schedule_appointment(self, appointment):
        self._appointments.append(appointment)

    def get_all_patients(self):
        print('Patients:')
        for patient in self._patients:
            patient.get_details('')

    def get_doctor_patients(self, doctor_id):
        doctor_id -= 1

        self._doctors[doctor_id].get_patients()

    def get_patient_appointments(self, patient_id):
        patient_id -= 1

        self._patients[patient_id].get_appointments()

if __name__ == '__main__':
    '''
    sample of inputs:
    
    ADD_DOCTOR <first_name> <last_name> <age> <gender> <specialization>
    ADD_PATIENT <first_name> <last_name> <age> <gender> <disease> <doctor_id>
    ADD_NURSE <first_name> <last_name> <age> <gender> <department>
    SCHEDULE_APPOINTMENT <doctor_id> <patient_id> <appointment_date> <appointment_time>
    GET_ALL_PATIENTS
    GET_DOCTOR_PATIENTS <doctor_id>
    GET_PATIENT_APPOINTMENTS <patient_id>
    '''
    hospital = Hospital()
    while 1:
        command = file1.readline().strip()
        command = [line.strip() for line in list(command.split(' ')) if line.strip()]

        if len(command) == 0:
            break

        if command[0] == 'ADD_PATIENT':
            hospital.add_patient(Patient(command[1], command[2], int(command[3]), command[4], command[5], hospital.get_doctor(int(command[6][1:]))))
        elif command[0] == 'ADD_DOCTOR':
            hospital.add_doctor(Doctor(command[1], command[2], int(command[3]), command[4], command[5]))
        elif command[0] == 'ADD_NURSE':
            hospital.add_nurse(Nurse(command[1], command[2], int(command[3]), command[4], command[5]))
        elif command[0] == 'SCHEDULE_APPOINTMENT':
            hospital.schedule_appointment(Appointment(hospital.get_doctor(int(command[1][1:])), hospital.get_patient(int(command[2][1:])), command[3] + ' ' + command[4]))
        elif command[0] == 'GET_ALL_PATIENTS':
            hospital.get_all_patients()
        elif command[0] == 'GET_DOCTOR_PATIENTS':
            hospital.get_doctor_patients(int(command[1][1:]))
        else:
            hospital.get_patient_appointments(int(command[1][1:]))

# ---------- End of Main Code ----------

sys.stdout = original_stdout

file1.close()
file2.close()
