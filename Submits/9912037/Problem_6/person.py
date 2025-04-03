class PersonClassForHospitalSystem:
    def __init__(self, first_name_input, last_name_input, id_number_input, age_input, gender_input):
        self.first_name_attribute = first_name_input
        self.last_name_attribute = last_name_input
        self.id_number_attribute = id_number_input
        self.age_attribute = age_input
        self.gender_attribute = gender_input

    def get_full_name_method(self):
        full_name_result = self.first_name_attribute + " " + self.last_name_attribute
        return full_name_result

    def get_details_method(self):
        details_string = ""
        details_string += "Name: " + self.get_full_name_method() + "\n"
        details_string += "ID: " + self.id_number_attribute + "\n"
        details_string += "Age: " + str(self.age_attribute) + "\n"
        details_string += "Gender: " + self.gender_attribute + "\n"
        return details_string