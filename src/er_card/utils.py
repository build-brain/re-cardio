from datetime import datetime

def get_file_path(instance, filename):
    title = instance.title
    return f"uploads/admission_data/{title}/{filename}"