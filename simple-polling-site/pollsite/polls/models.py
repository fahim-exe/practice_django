from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=300)
    publish_date = models.DateTimeField("date pulished")

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)


    def __str__(self) -> str:
        return f"{self.question_text}"


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"choice:{self.choice_text}, {self.votes}"