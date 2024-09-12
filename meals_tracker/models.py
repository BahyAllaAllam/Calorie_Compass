from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Meals(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_items = models.TextField()
    calories = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if isinstance(self.calories, float):
            self.calories = round(self.calories)
        super(Meals, self).save(*args, **kwargs)

    def __str__(self):
        """Return a string representation of the meals."""
        return self.name

    class Meta:
        """The plural name used in the admin interface for the model."""
        verbose_name_plural = "Meals"

    def get_absolute_url(self):
        return reverse('meals_tracker:meals_tracking', kwargs={'slug': self.slug})
