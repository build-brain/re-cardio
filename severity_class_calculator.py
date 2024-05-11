class SeverityClassifier:

    def __init__(self):

        # Словари для классификации с более читаемыми значениями
        self.myocardial_damage = {
            'Мелкоочаговый': 1,
            'Крупноочаговый нетрансмуральный': 2,
            'Трансмуральный или циркулярный субэндокардиальный': 3
        }
        self.coronary_insufficiency = {
            'Стенокардия отсутствует': 1,
            'Стенокардия редкая': 2,
            'Стенокардия умеренная': 3,
            'Стенокардия частая': 4
        }
        self.complications_group = {
            'first_group': [0]*4,
            'second_group': [0]*9,
            'third_group': [0]*16
        }

    def validate_input(self, damage, cad, complications):
        # Проверка корректности ввода
        if damage not in self.myocardial_damage.values():
            raise ValueError("Некорректное значение глубины и обширности поражения миокарда.")
        if cad not in self.coronary_insufficiency.values():
            raise ValueError("Некорректное значение коронарной недостаточности.")
        if not all(isinstance(comp, list) and len(comp) == len(val) for comp, val in zip(complications.values(), self.complications_group.values())):
            raise ValueError("Некорректные данные осложнений.")

        # Проверка на активность только одной группы осложнений
        active_groups = sum(bool(sum(group)) for group in complications.values())
        if active_groups != 1:
            raise ValueError("Одновременно допускается только одна группа осложнений.")

        return True

    def determine_severity_class(self, selected_myocardial_damage, selected_cad, selected_complications):
        if not self.validate_input(selected_myocardial_damage, selected_cad, selected_complications):
            return "Входные данные неполные или некорректны."

        # Подсчет активных осложнений в каждой группе
        first_group_sum = sum(selected_complications['first_group'])
        second_group_sum = sum(selected_complications['second_group'])
        third_group_sum = sum(selected_complications['third_group'])

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

# Пример использования
classifier = SeverityClassifier()

myocardial_damage = 1
cad = 3
complications = {
    'first_group': [0, 1, 0, 0],
    'second_group': [0, 0, 0, 0, 0, 0, 0, 0, 0],
    'third_group': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}

patient_severity_class = classifier.determine_severity_class(myocardial_damage, cad, complications)

print("Реабилитационный класс тяжести пациента:", patient_severity_class)
