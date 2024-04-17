def get_file_path(instance, filename):
    patient = instance.ca_sheet.patient
    title = instance.title
    return f"uploads/{title}/{patient.username}/{filename}"
