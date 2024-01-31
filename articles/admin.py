from django.contrib import admin
from .models import Article, Category, Tour, Tour_Booking, Excursion, ExcusionBooking

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tour)
admin.site.register(Tour_Booking)
admin.site.register(Excursion)
admin.site.register(ExcusionBooking)