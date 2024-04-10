from datetime import datetime

def get_file_path(instance, filename):
    title = instance.title
    current_date = datetime.now()
    return f"uploads/{title}/{current_date.year}/{current_date.month}/{current_date.day}/{filename}"