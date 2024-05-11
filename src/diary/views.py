from django.utils.translation import gettext_lazy as _
    
from rest_framework import viewsets
from rest_framework.decorators import action

from src.diary.models import HealthDiaryRecord

from .serializers import HealthDiaryRecordSerializer


class HealthDiaryRecordViewSet(viewsets.ModelViewSet):

    """Health diary record model view set"""
    
    queryset = HealthDiaryRecord.objects.all()
    serializer_class = HealthDiaryRecordSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    


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