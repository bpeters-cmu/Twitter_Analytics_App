from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    topic = forms.CharField(max_length=128)

    class Meta:
        model = Topic
        fields = ('topic',)
