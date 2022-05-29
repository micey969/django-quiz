from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from quiz import models


class QuestionsForm(ModelForm):
    class Meta:
        model = models.Questions
        fields = "__all__"