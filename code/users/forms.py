from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")


class EditProfile(forms.ModelForm):
    email = forms.EmailField(required=True, label="E-mail")
    first_name = forms.CharField(required=False, label="Имя")
    last_name = forms.CharField(required=False, label="Фамилия")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(username=email).exclude(id=self.instance.id).count():
            raise forms.ValidationError(f'Указанный вами e-mail уже зарегестрирован!')
        return email
