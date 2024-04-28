def get_file_path_er_card(instance, filename):
    title = instance.title
    return f"uploads/admission_data/{title}/{filename}"


def get_file_path_ca_sheet(instance, filename):
    patient = instance.ca_sheet.patient
    title = instance.title
    return f"uploads/{title}/{patient.username}/{filename}"
