from hospital import HospitalManagementSystemClass
from patient import PatientClassInheritsPerson
from doctor import DoctorClassInheritsPerson
from nurse import NurseClassInheritsPerson

hospital_system_instance = HospitalManagementSystemClass()

while True:
    print("\nHospital Management System")
    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. Add Nurse")
    print("4. Schedule Appointment")
    print("5. View All Patients")
    print("6. View All Doctors")
    print("7. View All Appointments")
    print("8. Exit")

    user_choice_input = input("Enter your choice: ")

    if user_choice_input == "1":
        first_name_doc = input("Doctor first name: ")
        last_name_doc = input("Doctor last name: ")
        id_doc = input("Doctor ID: ")
        age_doc = input("Doctor age: ")
        gender_doc = input("Doctor gender: ")
        specialization_doc = input("Doctor specialization: ")

        new_doctor_object = DoctorClassInheritsPerson(first_name_doc, last_name_doc, id_doc, age_doc, gender_doc,
                                                      specialization_doc)
        hospital_system_instance.add_doctor_method(new_doctor_object)
        print("Doctor added successfully:")
        print(new_doctor_object.get_doctor_details_method())

    elif user_choice_input == "2":
        first_name_pat = input("Patient first name: ")
        last_name_pat = input("Patient last name: ")
        id_pat = input("Patient ID: ")
        age_pat = input("Patient age: ")
        gender_pat = input("Patient gender: ")
        disease_pat = input("Patient disease: ")

        new_patient_object = PatientClassInheritsPerson(first_name_pat, last_name_pat, id_pat, age_pat, gender_pat,
                                                        disease_pat)
        hospital_system_instance.add_patient_method(new_patient_object)
        print("Patient added successfully:")
        print(new_patient_object.get_patient_details_method())

    elif user_choice_input == "3":
        first_name_nur = input("Nurse first name: ")
        last_name_nur = input("Nurse last name: ")
        id_nur = input("Nurse ID: ")
        age_nur = input("Nurse age: ")
        gender_nur = input("Nurse gender: ")
        department_nur = input("Nurse department: ")

        new_nurse_object = NurseClassInheritsPerson(first_name_nur, last_name_nur, id_nur, age_nur, gender_nur,
                                                    department_nur)
        hospital_system_instance.add_nurse_method(new_nurse_object)
        print("Nurse added successfully:")
        print(new_nurse_object.get_nurse_details_method())

    elif user_choice_input == "4":
        patient_id = input("Patient ID: ")
        doctor_id = input("Doctor ID: ")
        appointment_time = input("Appointment time (YYYY-MM-DD HH:MM): ")

        found_patient = None
        for patient_item in hospital_system_instance.all_patients_list:
            if patient_item.id_number_attribute == patient_id:
                found_patient = patient_item
                break

        found_doctor = None
        for doctor_item in hospital_system_instance.all_doctors_list:
            if doctor_item.id_number_attribute == doctor_id:
                found_doctor = doctor_item
                break

        if found_patient and found_doctor:
            new_appointment = hospital_system_instance.schedule_appointment_method(found_patient, found_doctor,
                                                                                   appointment_time)
            print("Appointment scheduled successfully:")
            print(new_appointment.get_appointment_details_method())
        else:
            print("Patient or doctor not found!")

    elif user_choice_input == "5":
        print("\nAll Patients:")
        print(hospital_system_instance.get_all_patients_method())

    elif user_choice_input == "6":
        print("\nAll Doctors:")
        print(hospital_system_instance.get_all_doctors_method())

    elif user_choice_input == "7":
        print("\nAll Appointments:")
        print(hospital_system_instance.get_all_appointments_method())

    elif user_choice_input == "8":
        break

    else:
        print("Invalid choice!")