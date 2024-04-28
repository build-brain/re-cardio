def get_passport_path(instance, filename):
    user_type = instance.user_type
    passport = instance.passport
    return f"uploads/passports/{user_type}/{passport}/{filename}"

def get_file_path(instance, filename):
    title = instance.title
    return f"uploads/patients/{title}/{filename}"