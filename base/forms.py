from django.forms.models import ModelForm
from .models import Tarefa


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
        exclude = ['user']