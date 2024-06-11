from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import ConditionAssessmentSheet
from .utils import calculate_grace_score, calculate_grace, calculate_patient_severity_class


# @receiver(post_save, sender=ConditionAssessmentSheet)
# def save_er_card(sender, instance, created, **kwargs):
#     instance.er_card.save()


@receiver(post_save, sender=ConditionAssessmentSheet)
def patient_severity_class(sender, created, instance, ** kwargs) :
    if created:
        instance.grace_score = calculate_grace_score(instance=instance)
        instance.lethality_hospital, instance.risk_hospital = calculate_grace(score=instance.grace_score, stemi=instance.stemi, hospital=True)
        instance.lethality_six_months, instance.risk_six_months = calculate_grace(score=instance.grace_score, stemi=instance.stemi)
        instance.patient_severity_class = calculate_patient_severity_class(instance=instance)
        instance.save(update_fields=['grace_score', 'lethality_hospital', 'risk_hospital', 'lethality_six_months', 'risk_six_months', 'patient_severity_class'])
        