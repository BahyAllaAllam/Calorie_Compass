from django.urls import path
from meals_tracker.views import about, home, calorie_calc, MealView
from meals_tracker.api_views import MealViewSet


app_name = 'meals_tracker'

urlpatterns = [
    path('', home, name = "home_page"),
    path('about/', about, name="about_page"),
    path('calorie_calculation/', calorie_calc, name="calorie_calc"),
    path('meals/', MealView.as_view(), name="meals_list"),
    path('meals/api/meals/', MealViewSet.as_view({'get': 'list', 'post':'create'}), name='rest_meal_list'),
    path('meals/api/meal/<int:pk>/', MealViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete':'destroy'}), name='rest_meal_detail'),
]