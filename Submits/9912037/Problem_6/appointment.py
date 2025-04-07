class AppointmentClassForHospital:
    def __init__(self, patient_object_input, doctor_object_input, appointment_time_input):
        self.patient_attribute = patient_object_input
        self.doctor_attribute = doctor_object_input
        self.time_attribute = appointment_time_input
        self.status_attribute = "Scheduled"

    def cancel_appointment_method(self):
        self.status_attribute = "Canceled"

    def get_appointment_details_method(self):
        details_string = ""
        details_string += "Patient: " + self.patient_attribute.get_full_name_method() + "\n"
        details_string += "Doctor: " + self.doctor_attribute.get_full_name_method() + "\n"
        details_string += "Date and Time: " + self.time_attribute + "\n"
        details_string += "Status: " + self.status_attribute + "\n"
        return details_string