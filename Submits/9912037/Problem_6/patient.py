from person import PersonClassForHospitalSystem

class PatientClassInheritsPerson(PersonClassForHospitalSystem):
    def __init__(self, first_name_patient, last_name_patient, id_patient, age_patient, gender_patient, disease_input):
        super().__init__(first_name_patient, last_name_patient, id_patient, age_patient, gender_patient)
        self.disease_attribute = disease_input
        self.doctor_assigned_attribute = None

    def assign_doctor_method(self, doctor_object):
        self.doctor_assigned_attribute = doctor_object

    def get_patient_details_method(self):
        details_result = super().get_details_method()
        details_result += "Disease: " + self.disease_attribute + "\n"
        if self.doctor_assigned_attribute:
            details_result += "Assigned Doctor: " + self.doctor_assigned_attribute.get_full_name_method() + "\n"
        return details_result