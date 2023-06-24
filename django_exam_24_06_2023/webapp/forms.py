from django.forms import ModelForm, EmailInput, PasswordInput, TextInput, Textarea
from pyexpat import model

from .models import UserProfile, Fruit


# user profile forms:
class CreateUserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': "",
            'last_name': "",
            'email': "",
            'password': "",
        }
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
        }


class EditUserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'image_url', 'age']
        labels = {
            'first_name': "First Name",
            'last_name': "Last Name",
            'image_url': "Image URL",
            'age': "Age",
        }


# fruit forms:
class CreateFruitForm(ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'name': "",
            'image_url': "",
            'description': "",
            'nutrition': "",
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class BaseFruitForm(ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'name': "Name",
            'image_url': "Image URL",
            'description': "Description",
            'nutrition': "Nutrition",
        }
        widgets = {
            'name': TextInput(),
            'image_url': TextInput(),
            'description': Textarea(),
            'nutrition': Textarea(),
        }


class EditFruitForm(BaseFruitForm):
    pass


class DeleteFruitForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_fields_disabled()

    def __set_fields_disabled(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
