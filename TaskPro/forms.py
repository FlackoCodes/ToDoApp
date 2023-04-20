from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Task

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', max_length=100, widget = forms.TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder':
        ' Enter Email'}))
    first_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                     'placeholder':
        'Enter First Name'}))
    last_name = forms.CharField(label='',max_length=100, widget= forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder':'Enter Last '
                                                                                                      'Name'}))

    # meta class to specify the model and fields to use
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    # override the constructor to customize field widgets and labels
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # customize the username field widget
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''

        # customize the password1 field widget
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''

        # customize the password2 field widget
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''



class TaskForm(forms.ModelForm):
    title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Title'
    }))
    description = forms.TextInput()

    due_date = forms.DateField(required=True, label='', widget= forms.SelectDateWidget(attrs={
        'class': 'form-control datepicker',
        'placeholder': 'Due date',
        'autocomplete': 'off'
    }))

    class Meta:
        model = Task
        exclude = ['user', 'complete', 'created_at']