from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from meals_tracker.models import Meals
from django.contrib.auth.mixins import LoginRequiredMixin
from meals_tracker.forms import MealForm
from django.http import JsonResponse
from django.conf import settings
from django.template.defaulttags import register
from django.contrib import messages
from django.urls import reverse
from django.utils.dateformat import DateFormat
from django.utils import timezone


@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)

# Create your views here.
def home(request):
    return render(request, 'meals_tracker/home.html')


def about(request):
    return render(request, 'meals_tracker/about.html')


def calorie_calc(request):
    return render(request, 'meals_tracker/calorie_calc.html')


class MealView(LoginRequiredMixin, View):
    template_name = 'meals_tracker/meal-tracking.html'


    def get(self, request, *args, **kwargs):
        form = MealForm()
        return self.form_invalid(request, form)

    def post(self, request, *args, **kwargs):
        if request.POST.get('_method') == 'delete':
            return self.delete(request, *args, **kwargs)

        form = MealForm(request.POST)
        if form.is_valid():
            new_meal = form.save(commit=False)
            new_meal.user = request.user
            new_meal.calories = request.POST.get('calories', 0)
            new_meal.food_items = request.POST.get('food_items')
            new_meal.save()
            return JsonResponse({'redirect_url': reverse('meals_tracker:meals_list')})

        return self.form_invalid(request, form)


    def form_invalid(self, request, form):
        # Delete meals older than 7 days
        Meals.deleting_meals_older_than_7days(request.user)

        # Query meals for the user ordered by the creation date
        meals = Meals.objects.filter(user=request.user).order_by('-created_at').values('name', 'calories', 'created_at', 'date', 'slug', 'food_items')

        # Initialize a dictionary to store total calories for each date
        calories_by_date = dict()

        # Store meals and the unique meal dates
        meals = list(meals)

        for meal in meals:
            # Get the local time for created_at
            local_created_at = timezone.localtime(meal['created_at'])

            # Extract the day in a readable format
            specific_day = DateFormat(local_created_at).format('d-m-Y')

            # Add the calories for this meal to the corresponding day
            if specific_day not in calories_by_date:
                calories_by_date[specific_day] = 0
            calories_by_date[specific_day] += meal['calories']

            # Format the created_at to be more readable
            meal['created_at'] = DateFormat(local_created_at).format('d-m-Y H:i')
            meal['date'] = DateFormat(meal['date']).format('d-m-Y')

        return render(request, self.template_name, {
            'meals': meals,
            'calories_by_date': calories_by_date,
            'form': form,
            'calorie_ninjas_api_key': settings.CALORIE_NINJAS_API_KEY
        })


    def delete(self, request, *args, **kwargs):
        slug = request.POST.get('meal_slug')
        meal = get_object_or_404(Meals, slug=slug, user=request.user)
        meal.delete()
        messages.success(request, f'The {slug} has been deleted successfully !')
        return redirect('meals_tracker:meals_list')
