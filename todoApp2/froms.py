from django import forms
from todoApp2.models import Task


class SearchForm(forms.Form):
    # query = forms.CharField(label="Search", required=False)
    query = forms.CharField()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # ki ki fild rakbo sata bollam
        fields = ['title', 'description', 'completed']

        