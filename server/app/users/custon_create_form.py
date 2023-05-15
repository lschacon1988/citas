# from django import forms
# from .models import UserProfile
# from django.contrib.auth.models import User


# class CustomUserCreationForm(forms.ModelForm):
#     # full_name = forms.CharField(max_length=255)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password', 'first_name', 'last_name')

#     def save(self, commit=True):
#         print('estoy en el formulario')
#         user = super(CustomUserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         user.username = self.cleaned_data["username"]
#         user.first_name = self.cleaned_data["first_name"]
#         user.last_name = self.cleaned_data["last_name"]
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user