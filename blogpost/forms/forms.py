# from django.contrib.auth.models import User
# from blogpost.models.models import Profile
from django import forms



MY_CHOICES = (
    ('1', 'Code'),
    ('2', 'Design'),
    ('3', 'Cats'),
)
    
class MyForm(forms.Form):
    my_choice_field = forms.ChoiceField(choices=MY_CHOICES)

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         widgets = {
#                     'username': forms.TextInput(attrs={'class': 'form-control'}),
#                     'email': forms.TextInput(attrs={'class': 'form-control'}),
#                     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#                     'last_name': forms.TextInput(attrs={'class': 'form-control'})
#                 }
#         fields = ('username', 'email', 'password', 'first_name', 'last_name')

# class EditUserForm(forms.ModelForm):

#     class Meta:
#         model = User
#         widgets = {
#                     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#                     'last_name': forms.TextInput(attrs={'class': 'form-control'})
#                 }
#         fields = ('first_name', 'last_name')


