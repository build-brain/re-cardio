def get_file_path(instance, filename) -> str:

    """Generates file path"""
    
    title = instance.title
    return f"uploads/er_card/{title}/{filename}"

def calculate_grace_score(instance) -> int:
    
    """Calculates grace score"""
    
    score = 0
    age = instance.er_card.patient.age
    pulse_rate = instance.pulse_rate
    systolic_pressure = instance.systolic_pressure
    creatinine = instance.creatinine
    troponin = instance.troponin
    heart_stopped = instance.er_card.admission_data.heart_stopped
    st_elevation = instance.st_segment_elevation
    t_inversion = instance.t_wave_inversion
    killip = instance.killip
    
    # Возраст (лет)
    if (age < 30):
        score += 0
    elif (30 <= age <= 39):
        score += 8
    elif (40 <= age <= 49):
        score += 25
    elif (50 <= age <= 59):
        score += 41
    elif (60 <= age <= 69):
        score += 58
    elif (70 <= age <= 79):
        score += 75
    elif (80 <= age <= 89):
        score += 91
    elif (age >= 90):
        score += 100
    
    # Частота сердечных сокращений (уд. / мин.)
    if (pulse_rate < 50):
        score += 0
    elif (50 <= pulse_rate <= 69):
        score += 3
    elif (70 <= pulse_rate <= 89):
        score += 9
    elif (90 <= pulse_rate <= 109):
        score += 15
    elif (110 <= pulse_rate <= 149):
        score += 24
    elif (150 <= pulse_rate <= 199):
        score += 38
    elif (pulse_rate >= 200):
        score += 46
        
    # Систолическое АД (мм.рт.ст.)
    if (systolic_pressure < 80):
        score += 58
    elif (80 <= systolic_pressure <= 99):
        score += 53
    elif (100 <= systolic_pressure <= 119):
        score += 43
    elif (120 <= systolic_pressure <= 139):
        score += 34
    elif (140 <= systolic_pressure <= 159):
        score += 24
    elif (160 <= systolic_pressure <= 199):
        score += 10
    elif (systolic_pressure >= 200):
        score += 0

    # Креатинин крови (мкмоль/л)
    if (creatinine < 35.36):
        score += 1
    elif (35.36 <= creatinine <= 70.71):
        score += 4
    elif (70.72 <= creatinine <= 106.07):
        score += 7
    elif (106.08 <= creatinine <= 141.43):
        score += 10
    elif (141.43 <= creatinine <= 176.7):
        score += 13
    elif (176.8 <= creatinine <= 353):
        score += 21
    elif (creatinine >= 354):
        score += 28
        
    # Остановка сердца (на момент поступления пациента)
    if heart_stopped:
        score += 39
    else:
        score += 0
        
    # Отклонение сегмента ST
    if (st_elevation and t_inversion):
        score += 28
    else:
        score += 0
        
    # Повышенный уровень кардиоспецифических ферментов
    if (troponin >= 0.2):
        score += 14
    else:
        score += 0
        
    # Класс сердечной недостаточности по Killip
    if (killip == 1):
        score += 0
    elif (killip == 2):
        score += 20
    elif (killip == 3):
        score += 39
    elif (killip == 4):
        score += 59

    return score

    
def calculate_grace(score: int, stemi: bool, hospital: bool = False) -> tuple:
    if stemi:
        if hospital:
            if (score < 126):
                return "< 2%", "low"
            elif (125 < score < 155):
                return "2-5%", "medium"
            elif (score > 154):
                return "> 5%", "high"
        else:
            if (score < 100):
                return "< 4.5%", "low"
            elif (99 < score < 128):
                return "4.5-11%", "medium"
            elif (score > 127):
                return "> 11%", "high"
    else:
        if hospital:
            if (score < 109):
                return "< 1%", "low"
            elif (108 < score < 141):
                return "1-3%", "medium"
            elif (score > 140):
                return "> 3%", "high"
        else:
            if (score < 89):
                return "< 3%", "low"
            elif (88 < score < 119):
                return "3-8%", "medium"
            elif (score > 118):
                return "> 8%", "high"


def calculate_patient_severity_class(instance):
    
    """Calculates patient severity class"""

    selected_cad = instance.coronary_insufficiency       
    selected_myocardial_damage = instance.myocardium_damage
    complications = instance.complications.all()
    complications_group = complications.first().group

    # Подсчет активных осложнений в каждой группе
    first_group_sum = 0
    second_group_sum = 0
    third_group_sum = 0

    match complications_group:
        case 1:
            for _ in complications:
                first_group_sum += 1
        case 2:
            for _ in complications:
                second_group_sum += 1
        case 3:
            for _ in complications:
                third_group_sum += 1

    # Определение класса тяжести на основе входных данных
    if third_group_sum > 0 or second_group_sum >= 3:
        return 4  # Класс IV
    elif second_group_sum > 0:
        if selected_myocardial_damage > 1:
            if selected_cad >= 3:
                return 4  # Класс IV
            elif selected_cad < 3:
                return 3  # Класс III
        elif selected_myocardial_damage == 1:
            if selected_cad < 3:
                return 2  # Класс II
            elif selected_cad >= 3:
                return 3  # Класс III
    elif first_group_sum > 0:
        if selected_myocardial_damage == 1:
            if selected_cad <= 2:
                return 1  # Класс I
            elif selected_cad == 3:
                return 2  # Класс II
            return 3  # Класс III
        elif selected_myocardial_damage == 2:
            if selected_cad < 3:
                return 2  # Класс II
            elif selected_cad == 3:
                return 3  # Класс III
            return 4  # Класс IV
        elif selected_myocardial_damage == 3:
            if selected_cad < 4:
                return 3  # Класс III
            return 4  # Класс IV

        return None  # Если класс не может быть определен
        