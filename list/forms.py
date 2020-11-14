from django import forms 
from .models import TodoList

class TodoListForm(forms.ModelForm):
	class Meta:
		model = TodoList 
		fields = ('title', 'complete',)

		widget={
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'complete': forms.Select(attrs={'class':'form-check'}),
		}