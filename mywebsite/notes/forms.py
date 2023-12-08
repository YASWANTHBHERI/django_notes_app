from django import forms
from .models import notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ('title','text')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control title-inp my-2'}),
            'text':forms.Textarea(attrs={'class':'form-control text-inp  my-2'}),
        }
        labels = {
            'text':'Write your thoughts'
        }

    