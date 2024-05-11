from django.utils.translation import gettext_lazy as _
    
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.decorators import action

from src.er_card.models import ElectronicRehabilitationCard 

from .models import HealthDiaryRecord
from .serializers import (
    HealthDiaryRecordSerializer,
    BodyTemperatureSerializer,
    ArterialPressureSerializer,
    PulseRateSerializer,
    BloodSaturationSerializer,
    RespiratoryRateSerializer,
    RespiratoryConditionSerializer,
    DyspneaSerializer,
    FatiueSerializer,
    HeartPainSerializer,
    PhysicalActivitySerializer
)


class HealthDiaryRecordViewSet(viewsets.ReadOnlyModelViewSet):
    """Health diary record model view set"""
    
    queryset = HealthDiaryRecord.objects.all()
    serializer_class = HealthDiaryRecordSerializer
    
    def get_er_card(self):
        
        # Проверяем пользователя
        user = self.request.user
        if user.is_anonymous or user.user_type != "PATIENT":
            raise serializers.ValidationError({"error": _("User is not a patient.")})
        
        # Достаем электронную карту реабилитации
        try:
            er_card = user.er_cards.filter(is_active=True).latest('created_at')
        except ElectronicRehabilitationCard.DoesNotExist:
            raise serializers.ValidationError({"error": _("Patient does not have Electronic Rehabilitation Card.")})
        
        return er_card

    @action(detail=False, methods=['post'], serializer_class=BodyTemperatureSerializer)
    def add_body_temperature(self, request):
        
        """Add body temperature record action"""
        
        # Передаем данные в сериализатор и валидируем
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Получаем валидированные данные из сериализатора
        body_temperature = serializer.validated_data['body_temperature']
        creation_date = serializer.validated_data['creation_date']
        
        # Достаем электронную карту реабилитации
        er_card = self.get_er_card()
        
        # Определяем параметры для поиска записи в базе данных
        search_params = {
            'er_card': er_card, 
            'creation_date': creation_date
        }
        
        # Поля, которые нужно обновить или создать
        update_fields = {'body_temperature': body_temperature}
        
        # Обновляем или создаем запись в дневнике здоровья
        health_diary_record, created = HealthDiaryRecord.objects.update_or_create(
            defaults=update_fields,
            **search_params
        )
        
        # Возвращаем созданный объект или его данные в ответе
        return Response(HealthDiaryRecordSerializer(health_diary_record).data)

    @action(detail=False, methods=['post'], serializer_class=ArterialPressureSerializer)
    def add_arterial_pressure(self, request):
        
        """Add arterial pressure record action"""
        
        # Передаем данные в сериализатор и валидируем
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Получаем валидированные данные из сериализатора
        systolic_pressure = serializer.validated_data['systolic_pressure']
        diastolic_pressure = serializer.validated_data['diastolic_pressure']
        creation_date = serializer.validated_data['creation_date']
        
        # Достаем электронную карту реабилитации
        er_card = self.get_er_card()
        
        # Определяем параметры для поиска записи в базе данных
        search_params = {
            'er_card': er_card, 
            'creation_date': creation_date
        }
        
        # Поля, которые нужно обновить или создать
        update_fields = {
            'systolic_pressure': systolic_pressure,
            'diastolic_pressure': diastolic_pressure,
        }
        
        # Обновляем или создаем запись в дневнике здоровья
        health_diary_record, created = HealthDiaryRecord.objects.update_or_create(
            defaults=update_fields,
            **search_params
        )
        
        # Возвращаем созданный объект или его данные в ответе
        return Response(HealthDiaryRecordSerializer(health_diary_record).data)

    @action(detail=False, methods=['post'], serializer_class=PulseRateSerializer)
    def add_pulse_rate(self, request):
        
        """Add pulse rate record action"""
        
        # Передаем данные в сериализатор и валидируем
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Получаем валидированные данные из сериализатора
        pulse_rate = serializer.validated_data['pulse_rate']
        pulse_on_exertion = serializer.validated_data['pulse_on_exertion']
        creation_date = serializer.validated_data['creation_date']
        
        # Достаем электронную карту реабилитации
        er_card = self.get_er_card()
        
        # Определяем параметры для поиска записи в базе данных
        search_params = {
            'er_card': er_card, 
            'creation_date': creation_date
        }
        
        # Поля, которые нужно обновить или создать
        update_fields = {
            'pulse_rate': pulse_rate,
            'pulse_on_exertion': pulse_on_exertion,
        }
        
        # Обновляем или создаем запись в дневнике здоровья
        health_diary_record, created = HealthDiaryRecord.objects.update_or_create(
            defaults=update_fields,
            **search_params
        )
        
        # Возвращаем созданный объект или его данные в ответе
        return Response(HealthDiaryRecordSerializer(health_diary_record).data)

    @action(detail=False, methods=['post'], serializer_class=BloodSaturationSerializer)
    def add_blood_saturation(self, request):
        
        """Add blood saturation record action"""
        
        # Передаем данные в сериализатор и валидируем
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Получаем валидированные данные из сериализатора
        blood_saturation = serializer.validated_data['blood_saturation']
        creation_date = serializer.validated_data['creation_date']
        
        # Достаем электронную карту реабилитации
        er_card = self.get_er_card()
        
        # Определяем параметры для поиска записи в базе данных
        search_params = {
            'er_card': er_card, 
            'creation_date': creation_date
        }
        
        # Поля, которые нужно обновить или создать
        update_fields = {
            'blood_saturation': blood_saturation
        }
        
        # Обновляем или создаем запись в дневнике здоровья
        health_diary_record, created = HealthDiaryRecord.objects.update_or_create(
            defaults=update_fields,
            **search_params
        )
        
        # Возвращаем созданный объект или его данные в ответе
        return Response(HealthDiaryRecordSerializer(health_diary_record).data)

    @action(detail=False, methods=['post'], serializer_class=RespiratoryRateSerializer)
    def add_respiratory_rate(self, request):
        
        """Add respiratory rate record action"""
        
        # Передаем данные в сериализатор и валидируем
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Получаем валидированные данные из сериализатора
        respiratory_rate = serializer.validated_data['respiratory_rate']
        breathing_rhythm = serializer.validated_data['breathing_rhythm']
        creation_date = serializer.validated_data['creation_date']
        
        # Достаем электронную карту реабилитации
        er_card = self.get_er_card()
        
        # Определяем параметры для поиска записи в базе данных
        search_params = {
            'er_card': er_card, 
            'creation_date': creation_date
        }
        
        # Поля, которые нужно обновить или создать
        update_fields = {
            'respiratory_rate': respiratory_rate,
            'breathing_rhythm': breathing_rhythm,
        }
        
        # Обновляем или создаем запись в дневнике здоровья
        health_diary_record, created = HealthDiaryRecord.objects.update_or_create(
            defaults=update_fields,
            **search_params
        )
        
        # Возвращаем созданный объект или его данные в ответе
        return Response(HealthDiaryRecordSerializer(health_diary_record).data)

    @action(detail=False, methods=['post'], serializer_class=RespiratoryConditionSerializer)
    def add_respiratory_condition(self, request):
        
        """Add respiratory rate record action"""
        
        # Передаем данные в сериализатор и валидируем
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Получаем валидированные данные из сериализатора
        moist_rales = serializer.validated_data['moist_rales']
        peripheral_edema = serializer.validated_data['peripheral_edema']
        creation_date = serializer.validated_data['creation_date']
        
        # Достаем электронную карту реабилитации
        er_card = self.get_er_card()
        
        # Определяем параметры для поиска записи в базе данных
        search_params = {
            'er_card': er_card, 
            'creation_date': creation_date
        }
        
        # Поля, которые нужно обновить или создать
        update_fields = {
            'moist_rales': moist_rales,
            'peripheral_edema': peripheral_edema,
        }
        
        # Обновляем или создаем запись в дневнике здоровья
        health_diary_record, created = HealthDiaryRecord.objects.update_or_create(
            defaults=update_fields,
            **search_params
        )
        
        # Возвращаем созданный объект или его данные в ответе
        return Response(HealthDiaryRecordSerializer(health_diary_record).data)

    @action(detail=False, methods=['post'], serializer_class=DyspneaSerializer)
    def add_dyspnea(self, request):
        
        """Add dyspnea record action"""
        
        # Передаем данные в сериализатор и валидируем
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Получаем валидированные данные из сериализатора
        dyspnea = serializer.validated_data['dyspnea']
        dyspnea_type = serializer.validated_data['dyspnea_type']
        creation_date = serializer.validated_data['creation_date']
        
        # Достаем электронную карту реабилитации
        er_card = self.get_er_card()
        
        # Определяем параметры для поиска записи в базе данных
        search_params = {
            'er_card': er_card, 
            'creation_date': creation_date
        }
        
        # Поля, которые нужно обновить или создать
        update_fields = {
            'dyspnea': dyspnea,
            'dyspnea_type': dyspnea_type,
        }
        
        # Обновляем или создаем запись в дневнике здоровья
        health_diary_record, created = HealthDiaryRecord.objects.update_or_create(
            defaults=update_fields,
            **search_params
        )
        
        # Возвращаем созданный объект или его данные в ответе
        return Response(HealthDiaryRecordSerializer(health_diary_record).data)

    @action(detail=False, methods=['post'], serializer_class=FatiueSerializer)
    def add_fatigue(self, request):
        
        """Add fatigue record action"""
        
        # Передаем данные в сериализатор и валидируем
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Получаем валидированные данные из сериализатора
        fatigue = serializer.validated_data['fatigue']
        fatigue_type = serializer.validated_data['fatigue_type']
        creation_date = serializer.validated_data['creation_date']
        
        # Достаем электронную карту реабилитации
        er_card = self.get_er_card()
        
        # Определяем параметры для поиска записи в базе данных
        search_params = {
            'er_card': er_card, 
            'creation_date': creation_date
        }
        
        # Поля, которые нужно обновить или создать
        update_fields = {
            'fatigue': fatigue,
            'fatigue_type': fatigue_type,
        }
        
        # Обновляем или создаем запись в дневнике здоровья
        health_diary_record, created = HealthDiaryRecord.objects.update_or_create(
            defaults=update_fields,
            **search_params
        )
        
        # Возвращаем созданный объект или его данные в ответе
        return Response(HealthDiaryRecordSerializer(health_diary_record).data)

    @action(detail=False, methods=['post'], serializer_class=HeartPainSerializer)
    def add_heart_pain(self, request):
        
        """Add fatigue record action"""
        
        # Передаем данные в сериализатор и валидируем
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Получаем валидированные данные из сериализатора
        heart_pain = serializer.validated_data['heart_pain']
        heart_pain_type = serializer.validated_data['heart_pain_type']
        creation_date = serializer.validated_data['creation_date']
        
        # Достаем электронную карту реабилитации
        er_card = self.get_er_card()
        
        # Определяем параметры для поиска записи в базе данных
        search_params = {
            'er_card': er_card, 
            'creation_date': creation_date
        }
        
        # Поля, которые нужно обновить или создать
        update_fields = {
            'heart_pain': heart_pain,
            'heart_pain_type': heart_pain_type,
        }
        
        # Обновляем или создаем запись в дневнике здоровья
        health_diary_record, created = HealthDiaryRecord.objects.update_or_create(
            defaults=update_fields,
            **search_params
        )
        
        # Возвращаем созданный объект или его данные в ответе
        return Response(HealthDiaryRecordSerializer(health_diary_record).data)

    @action(detail=False, methods=['post'], serializer_class=PhysicalActivitySerializer)
    def add_physical_activity(self, request):
        
        """Add fatigue record action"""
        
        # Передаем данные в сериализатор и валидируем
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Получаем валидированные данные из сериализатора
        walking_speed = serializer.validated_data['walking_speed']
        walking_duration = serializer.validated_data['walking_duration']
        distance_covered = serializer.validated_data['distance_covered']
        step_count = serializer.validated_data['step_count']
        borg_scale = serializer.validated_data['borg_scale']
        creation_date = serializer.validated_data['creation_date']
        
        # Достаем электронную карту реабилитации
        er_card = self.get_er_card()
        
        # Определяем параметры для поиска записи в базе данных
        search_params = {
            'er_card': er_card, 
            'creation_date': creation_date
        }
        
        # Поля, которые нужно обновить или создать
        update_fields = {
            'walking_speed': walking_speed,
            'walking_duration': walking_duration,
            'distance_covered': distance_covered,
            'step_count': step_count,
            'borg_scale': borg_scale,
        }
        
        # Обновляем или создаем запись в дневнике здоровья
        health_diary_record, created = HealthDiaryRecord.objects.update_or_create(
            defaults=update_fields,
            **search_params
        )
        
        # Возвращаем созданный объект или его данные в ответе
        return Response(HealthDiaryRecordSerializer(health_diary_record).data)
    
    


# class PhysicalIndicatorsViewSet(viewsets.ModelViewSet):
#     queryset = PhysicalIndicators.objects.all()
#     serializer_class = PhysicalIndicatorsSerializer
#     filterset_class = PhysicalIndicatorsFilter
    
#     def perform_create(self, serializer):
#         user = self.request.user
#         if user.user_type != "PATIENT":
#             raise serializers.ValidationError({"error": _("User is not a patient.")})

#         try:
#             er_card = user.er_cards.filter(is_active=True).latest('created_at')
#             record, created = HealthDiaryRecord.objects.get_or_create(
#                 creation_date=date.today(),
#                 er_card=er_card
#             )
#             serializer.save(record=record)
#         except ElectronicRehabilitationCard.DoesNotExist:
#             raise serializers.ValidationError({"error": _("Patient does not have Electronic Rehabilitation Card.")})
#         except IntegrityError as e:
#             raise serializers.ValidationError({"error": e.args[0]})
#         except AttributeError as e:
#             raise serializers.ValidationError({"error": e.args[0]})

#     def create(self, request, *args, **kwargs):
#         try:
#             return super().create(request, *args, **kwargs)
#         except serializers.ValidationError as e:
#             return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        
        
# class PhysicalActivityViewSet(viewsets.ModelViewSet):
#     queryset = PhysicalActivity.objects.all()
#     serializer_class = PhysicalActivitySerializer
#     filterset_class = PhysicalActivityFilter
    
#     def perform_create(self, serializer):
#         user = self.request.user
#         if user.user_type != "PATIENT":
#             raise serializers.ValidationError({"error": _("User is not a patient.")})

#         try:
#             er_card = user.er_cards.filter(is_active=True).latest('created_at')
#             record, created = HealthDiaryRecord.objects.get_or_create(
#                 creation_date=date.today(),
#                 er_card=er_card
#             )
#             serializer.save(record=record)
#         except ElectronicRehabilitationCard.DoesNotExist:
#             raise serializers.ValidationError({"error": _("Patient does not have Electronic Rehabilitation Card.")})
#         except IntegrityError as e:
#             raise serializers.ValidationError({"error": e.args[0]})
#         except AttributeError as e:
#             raise serializers.ValidationError({"error": e.args[0]})

#     def create(self, request, *args, **kwargs):
#         try:
#             return super().create(request, *args, **kwargs)
#         except serializers.ValidationError as e:
#             return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)