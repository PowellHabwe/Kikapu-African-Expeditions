from django.db import models
from django.urls import reverse
from slugify import slugify  # Import slugify from the python-slugify package

# Create your models here.

class Category(models.Model):
    thumb = models.ImageField(default='default.png', blank=False)
    category_name = models.CharField(max_length=1000, unique=True)
    body = models.TextField(blank = True)
    home_category = models.BooleanField(default=False) 


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('tour_by_category', args=[self.id])

    def __str__(self):
        return self.category_name
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    home_article = models.BooleanField(default=False) 



    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
    
class Excursion(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    home_excursion = models.BooleanField(default=False) 



    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
    

class Tour(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField( blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    place = models.CharField(max_length= 100,  blank=False)
    duration = models.CharField(max_length= 100,  blank=False)
    thumb = models.ImageField(default='default.png', blank=False)
    pax1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pax2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pax3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    is_special = models.BooleanField(default=False)  
    home_tour = models.BooleanField(default=False) 

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + '...'

class ExcusionBooking(models.Model):
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE)
    
    number_of_people = models.IntegerField(blank=False)
    travel_date = models.DateField(blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.excursion.title}'


class Tour_Booking(models.Model):
    Seasons = (
        ('pax1', 'Pax 1'),
        ('pax2', 'Pax 2'),
        ('pax3', 'Pax 3'),
    )
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    selected_pax = models.DecimalField(max_digits=100000, decimal_places=2, blank=True, null=True)
    number_of_people = models.IntegerField(blank=False)    
    travel_date = models.DateField(blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.tour.title}'
