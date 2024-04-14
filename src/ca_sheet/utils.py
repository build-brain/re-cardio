from datetime import datetime

def get_file_path(instance, filename):
    patient = instance.ca_sheet.patient
    title = instance.title
    return f"uploads/{title}/{patient.username}/{filename}"


def calculate_grace_score(age, heart_rate, systolic_bp, creatinine, cardiac_arrest, st_segment_abnormality, elevated_cardiac_markers, killip_class):
    score = 0
    
    # Возраст
    if age >= 18 and age < 40:
        score += 0
    elif age >= 40 and age < 50:
        score += 7
    elif age >= 50 and age < 60:
        score += 13
    elif age >= 60 and age < 70:
        score += 20
    elif age >= 70 and age < 80:
        score += 24
    elif age >= 80:
        score += 27
    
    # Сердечный ритм
    if heart_rate < 40:
        score += 11
    elif heart_rate >= 40 and heart_rate < 55:
        score += 4
    elif heart_rate >= 55 and heart_rate < 100:
        score += 0
    elif heart_rate >= 100 and heart_rate < 110:
        score += 2
    elif heart_rate >= 110 and heart_rate < 140:
        score += 4
    elif heart_rate >= 140:
        score += 5
    
    # Систолическое давление
    if systolic_bp < 80:
        score += 24
    elif systolic_bp >= 80 and systolic_bp < 100:
        score += 11
    elif systolic_bp >= 100 and systolic_bp < 120:
        score += 6
    elif systolic_bp >= 120 and systolic_bp < 140:
        score += 2
    elif systolic_bp >= 140 and systolic_bp < 160:
        score += 0
    elif systolic_bp >= 160:
        score += 2
    
    # Креатинин
    if creatinine < 2:
        score += 0
    elif creatinine >= 2 and creatinine < 3.5:
        score += 2
    elif creatinine >= 3.5 and creatinine < 5:
        score += 3
    elif creatinine >= 5 and creatinine < 7:
        score += 4
    elif creatinine >= 7:
        score += 5
    
    # Остановка сердца
    if cardiac_arrest:
        score += 10
    
    # Смещение сегмента ST, инверсия зубца Т
    if st_segment_abnormality:
        score += 8
    
    # Повышенный уровень маркеров некроза миокарда в крови
    if elevated_cardiac_markers:
        score += 30
    
    # Класс сердечной недостаточности (по классификации Killip)
    if killip_class == 1:
        score += 0
    elif killip_class == 2:
        score += 10
    elif killip_class == 3:
        score += 20
    elif killip_class == 4:
        score += 35
    
    return score