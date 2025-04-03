from person import PersonClassForHospitalSystem

class DoctorClassInheritsPerson(PersonClassForHospitalSystem):
    def __init__(self, first_name_doctor, last_name_doctor, id_doctor, age_doctor, gender_doctor, specialization_input):
        super().__init__(first_name_doctor, last_name_doctor, id_doctor, age_doctor, gender_doctor)
        self.specialization_attribute = specialization_input
        self.patients_list_attribute = []

    def add_patient_method(self, patient_object):
        self.patients_list_attribute.append(patient_object)
        patient_object.assign_doctor_method(self)

    def get_doctor_details_method(self):
        details_result = super().get_details_method()
        details_result += "Specialization: " + self.specialization_attribute + "\n"
        if len(self.patients_list_attribute) > 0:
            details_result += "Patients:\n"
            for patient_item in self.patients_list_attribute:
                details_result += "    - " + patient_item.get_full_name_method() + "\n"
        return details_result