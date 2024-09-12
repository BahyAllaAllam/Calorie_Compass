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
        meals = Meals.objects.filter(user=request.user)
        selected_meal = None
        slug = request.GET.get('slug')

        if slug:
            selected_meal = get_object_or_404(Meals, slug=slug, user=request.user)

        return render(request, self.template_name, {
            'meals': meals,
            'selected_meal': selected_meal,
            'form': form,
            'calorie_ninjas_api_key': settings.CALORIE_NINJAS_API_KEY
        })


    def delete(self, request, *args, **kwargs):
        slug = request.POST.get('meal_slug')
        meal = get_object_or_404(Meals, slug=slug, user=request.user)
        meal.delete()
        messages.success(request, f'The {slug} has been deleted successfully !')
        return redirect('meals_tracker:meals_list')
