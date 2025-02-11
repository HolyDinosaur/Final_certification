from django import forms
from .models import Recipe, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'cooking_time', 'image', 'categories']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True
        self.fields['preparation_steps'].widget.attrs.update({'placeholder': 'Введите ингредиенты, разделяя их запятыми'})
    def clean_preparation_steps(self):
        preparation_steps = self.cleaned_data.get('preparation_steps')
        steps_list = [step.strip() for step in preparation_steps.split(',') if step.strip()]
        if len(steps_list) < 2:
            raise forms.ValidationError("Пожалуйста, введите минимум два ингредиентa, разделенных запятыми.")
        return preparation_steps
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
