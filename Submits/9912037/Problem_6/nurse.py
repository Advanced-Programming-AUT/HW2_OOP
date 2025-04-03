from person import PersonClassForHospitalSystem

class NurseClassInheritsPerson(PersonClassForHospitalSystem):
    def __init__(self, first_name_nurse, last_name_nurse, id_nurse, age_nurse, gender_nurse, department_input):
        super().__init__(first_name_nurse, last_name_nurse, id_nurse, age_nurse, gender_nurse)
        self.department_attribute = department_input

    def get_nurse_details_method(self):
        details_result = super().get_details_method()
        details_result += "Department: " + self.department_attribute + "\n"
        return details_result