
#         self.fields['password2'].widget.attrs['class'] = 'form-control'
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Event



class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	phone_number = forms.CharField(max_length=12, widget=forms.NumberInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('username',  'phone_number','email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('title', 'date', 'location',  'description','attendees')
		labels = {
			'title': 'Title',
			'date': 'YYYY-MM-DD',
			'location': 'Location',
			'description': 'Description',
            'attendees': 'Attendees',
            'owner':"Owner"
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
			'date': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Date of Event'}),
			'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
            'owner': forms.Select(attrs={'class':'form-select', 'placeholder':'Owner'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
		}