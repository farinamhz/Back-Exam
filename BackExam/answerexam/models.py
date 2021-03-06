from django.db import models
from django.dispatch import receiver
from designexam.models import MultipleQuestion, DescriptiveQuestion
from result.utility.auto_correction import AutoCorrection
from account.models import User


class MultipleAnswer(models.Model):  # Students
    multiple_questionID = models.ForeignKey(MultipleQuestion, on_delete=models.CASCADE, blank=False)
    studentID = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)  # CharField(max_length=200)
    answer_choice = models.CharField(max_length=10)  # string of 0 & 1 that 0 is for False and 1 is for True
    created_date = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        index_together = [
            ["multiple_questionID_id"],
        ]


@receiver(models.signals.post_save, sender=MultipleAnswer)
def auto_delete_mult_answer(sender, instance, created, **kwargs):
    if created:
        auto_c = AutoCorrection(instance, "Multiple")
        auto_c.save()


class DescriptiveAnswer(models.Model):  # Students
    descriptive_questionID = models.ForeignKey(DescriptiveQuestion, on_delete=models.CASCADE, blank=False)
    studentID = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)  # CharField(max_length=200)
    file_id =models.PositiveIntegerField(default=None, null=True)  # if teacher allow them
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        index_together = [
            ["descriptive_questionID_id"],
        ]

