from django.urls import path
from meals_tracker.views import about, home, calorie_calc, MealView

app_name = 'meals_tracker'

urlpatterns = [
    path('', home, name = "home_page"),
    path('about/', about, name="about_page"),
    path('calorie_calculation/', calorie_calc, name="calorie_calc"),
    path('meals/', MealView.as_view(), name="meals_list"),
]