class Person:
    def __init__(self, first_name, last_name, id, age, gender):
        self._first_name = first_name
        self._last_name = last_name
        self._id = id
        self._age = age
        self._gender = gender

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def id(self):
        return self._id

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender


class Patient(Person):
    def __init__(self, first_name, last_name, id, age, gender, disease):
        super().__init__(first_name, last_name, id, age, gender)
        self._disease = disease
        self._doctor = None
        self._appointments = []

    @property
    def disease(self):
        return self._disease

    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, value):
        self._doctor = value

    @property
    def appointments(self):
        return self._appointments

    def get_patient_details(self):
        s = (
            f'Patient details:\n'
            f'Name: {self.first_name}\n'
            f'ID: {self.id}\n'
            f'Age: {self.age}\n'
            f'Gender: {self.gender}\n'
            f'Disease: {self.disease}\n'
            f'Assigned Doctor: Dr.{self.doctor.first_name} {self.doctor.last_name}'
        )
        return s


class Doctor(Person):
    def __init__(self, first_name, last_name, id, age, gender, specialization):
        super().__init__(first_name, last_name, id, age, gender)
        self._specialization = specialization
        self._patients = []
        self._appointments = []

    @property
    def specialization(self):
        return self._specialization

    @property
    def patients(self):
        return self._patients

    @property
    def appointments(self):
        return self._appointments

    def add_patient(self, patient):
        self._patients.append(patient)

    def get_patients(self):
        out = f'Doctor {self.first_name} {self.last_name} Patients: '
        for patient in self.patients:
            out += f'{patient.first_name} {patient.last_name}, '
        return out.strip(', ')

    def get_doctor_details(self):
        s = (
            f'Doctor details:\n'
            f'Name: Dr. {self.first_name} {self.last_name}\n'
            f'ID: {self.id}\n'
            f'Age: {self.age}\n'
            f'Gender: {self.gender}\n'
            f'Specialization: {self.specialization}\n'
            f'Patients: {", ".join(f"{patient.first_name} {patient.last_name}" for patient in self.patients)}'
        )
        return s


class Nurse(Person):
    def __init__(self, first_name, last_name, id, age, gender, department):
        super().__init__(first_name, last_name, id, age, gender)
        self._department = department

    @property
    def department(self):
        return self._department

    def get_nurse_details(self):
        s = (
            f'Nurse details:\n'
            f'Name: {self.first_name}\n'
            f'ID: {self.id}\n'
            f'Age: {self.age}\n'
            f'Gender: {self.gender}\n'
            f'Department: {self.department}'
        )
        return s

    def assist_patient(self, patient):
        return f"{self.first_name} is assisting {patient.first_name} {patient.last_name}"


class Appointment:
    _appointments = []

    def __init__(self, patient, doctor, appointment_time=None, status='waiting'):
        self._patient = patient
        self._doctor = doctor
        self._appointment_time = appointment_time
        self._status = status
        patient.appointments.append(self)
        doctor.appointments.append(self)
        Appointment._appointments.append(self)

    @property
    def patient(self):
        return self._patient

    @property
    def doctor(self):
        return self._doctor

    @property
    def appointment_time(self):
        return self._appointment_time

    @property
    def status(self):
        return self._status

    def schedule_appointment(self, appointment_time):
        self._appointment_time = appointment_time
        self._status = 'confirmed'
        Appointment._appointments.append(self)

    def cancel_appointment(self):
        self._status = 'canceled'

    def get_appointment_details(self):
        return (
            f'Appointment details: \n'
            f'Patient: {self.patient.first_name} {self.patient.last_name}\n'
            f'Doctor: {self.doctor.first_name} {self.doctor.last_name}\n'
            f'Date: {self.appointment_time}\n'
            f'Status: {self.status}'
        )


class Hospital:
    _patients = []
    _doctors = []
    _nurses = []
    _appointments = []

    @classmethod
    def add_patient(cls, patient, doctor):
        cls._patients.append(patient)
        patient.doctor = doctor
        doctor.add_patient(patient)
        return (
            f'Patient added successfully\n'
            f'{patient.get_patient_details()}'
        )

    @classmethod
    def add_doctor(cls, doctor):
        cls._doctors.append(doctor)
        return (
            f'Doctor added successfully\n'
            f'{doctor.get_doctor_details()}'
        )

    @classmethod
    def add_nurse(cls, nurse):
        cls._nurses.append(nurse)
        return (
            f'Nurse added successfully\n'
            f'{nurse.get_nurse_details()}'
        )

    @classmethod
    def schedule_appointment(cls, appointment, time):
        cls._appointments.append(appointment)
        appointment.schedule_appointment(time)
        return (
            f'Appointment added successfully\n'
            f'{appointment.get_appointment_details()}'
        )

    @classmethod
    def get_all_patients(cls):
        out = 'Patients: \n'
        counter = 1
        for patient in cls._patients:
            out += f'{counter} {patient.get_patient_details()}\n'
            counter += 1
        return out.strip()

    @classmethod
    def get_all_doctors(cls):
        out = 'Doctors: \n'
        counter = 1
        for doctor in cls._doctors:
            out += f'{counter} {doctor.get_doctor_details()}\n'
            counter += 1
        return out.strip()

    @classmethod
    def get_all_nurses(cls):
        out = 'Nurses: \n'
        counter = 1
        for nurse in cls._nurses:
            out += f'{counter} {nurse.get_nurse_details()}\n'
            counter += 1
        return out.strip()

    @classmethod
    def get_all_appointments(cls):
        out = 'Appointments: \n'
        counter = 1
        for appointment in cls._appointments:
            out += f'{counter} {appointment.get_appointment_details()}\n'
            counter += 1
        return out.strip()

    @classmethod
    def get_doctor_patient(cls, doctor_name):
        doctor_first_name, doctor_last_name = doctor_name.split()
        for doctor in cls._doctors:
            if doctor.first_name == doctor_first_name and doctor.last_name == doctor_last_name:
                return doctor.get_patients()

    @classmethod
    def get_patient_appointments(cls, patient_name):
        patient_first_name, patient_last_name = patient_name.split()
        out = f'{patient_name} Appointments: \n'
        for patient in cls._patients:
            if patient.first_name == patient_first_name and patient.last_name == patient_last_name:
                for appointment in patient.appointments:
                    out += f"{appointment.get_appointment_details()}\n"
        return out.strip()


if __name__ == '__main__':
    mamad = Doctor('mamad', 'mohamadi', '123456789', 35, 'M', 'Cardiology')
    sara = Doctor('sara', 'ahmadi', '987654321', 28, 'F', 'Neurology')
    arash = Patient('arash', 'manouchehri', '123456789', 20, 'M', 'heart attack')
    mohsen = Patient('mohsen', 'rezaie', '258741369', 43, 'M', 'Brain attack')
    zahra = Nurse('zahra', 'moradi', '569874123', 25, 'F', 'Neurology Department')
    a1 = Appointment(arash, mamad)
    a2 = Appointment(mohsen, sara)

    print(Hospital.add_doctor(mamad))
    print(Hospital.add_doctor(sara))
    print(Hospital.add_nurse(zahra))
    print(Hospital.add_patient(arash, mamad))
    print(Hospital.add_patient(mohsen, sara))

    print(Hospital.schedule_appointment(a1, '1404/1/22 10:00 AM'))
    print(Hospital.schedule_appointment(a2, '1403/2/1 2:00 PM'))

    print(Hospital.get_patient_appointments('arash manouchehri'))
    print(Hospital.get_doctor_patient('sara ahmadi'))
    print(Hospital.get_all_doctors())
    print(Hospital.get_all_nurses())
    print(Hospital.get_all_appointments())
    print(Hospital.get_all_patients())





