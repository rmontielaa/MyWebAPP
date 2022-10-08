from django import forms
from .models import Question, choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__' 
