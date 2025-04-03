from patient import PatientClassInheritsPerson
from doctor import DoctorClassInheritsPerson
from nurse import NurseClassInheritsPerson
from appointment import AppointmentClassForHospital

class HospitalManagementSystemClass:
    def __init__(self):
        self.all_patients_list = []
        self.all_doctors_list = []
        self.all_nurses_list = []
        self.all_appointments_list = []

    def add_patient_method(self, patient_object):
        self.all_patients_list.append(patient_object)

    def add_doctor_method(self, doctor_object):
        self.all_doctors_list.append(doctor_object)

    def add_nurse_method(self, nurse_object):
        self.all_nurses_list.append(nurse_object)

    def schedule_appointment_method(self, patient_object, doctor_object, appointment_time):
        new_appointment = AppointmentClassForHospital(patient_object, doctor_object, appointment_time)
        self.all_appointments_list.append(new_appointment)
        doctor_object.add_patient_method(patient_object)
        return new_appointment

    def get_all_patients_method(self):
        result_string = ""
        for patient_item in self.all_patients_list:
            result_string += patient_item.get_patient_details_method() + "\n"
        return result_string

    def get_all_doctors_method(self):
        result_string = ""
        for doctor_item in self.all_doctors_list:
            result_string += doctor_item.get_doctor_details_method() + "\n"
        return result_string

    def get_all_appointments_method(self):
        result_string = ""
        for appointment_item in self.all_appointments_list:
            result_string += appointment_item.get_appointment_details_method() + "\n"
        return result_string