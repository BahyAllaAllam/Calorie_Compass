from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta


class Meals(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_items = models.TextField()
    calories = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, help_text='The date the meal was created.')
    date = models.DateField(default=timezone.now, help_text='The date the meal was consumed.')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.name = self.name.capitalize()
        if isinstance(self.calories, float):
            self.calories = round(self.calories)

        # Check if a meal with the same name exists for the same user and date
        if Meals.objects.filter(Q(user=self.user) & Q(name__iexact=self.name) & Q(date=self.date)).exists():
            raise ValueError("A meal with the same name already exists for this date.")
        
        super(Meals, self).save(*args, **kwargs)

    def __str__(self):
        """Return a string representation of the meals."""
        return self.name

    class Meta:
        """The plural name used in the admin interface for the model."""
        verbose_name_plural = "Meals"
        unique_together = ('name', 'user', 'date')

    def get_absolute_url(self):
        return reverse('meals_tracker:meals_tracking', kwargs={'slug': self.slug})

    @classmethod
    def deleting_meals_older_than_7days(cls, user):
        # Get meals for the user from the last 6 days
        seven_days_ago = timezone.now() - timedelta(days=7)
        Meals.objects.filter(user=user, created_at__lt=seven_days_ago).delete()
