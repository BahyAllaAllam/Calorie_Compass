from django import forms
from meals_tracker.models import Meals


class MealForm(forms.ModelForm):

    class Meta:
        model = Meals
        fields = ['name', 'food_items']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['food_items'].widget.attrs.update({'placeholder': 'Enter your food items with only one type of separator (commaspace, space, or plus sign) to separate food items'})
