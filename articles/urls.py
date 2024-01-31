
from django.urls import path
from . import views

app_name = 'articles'


urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('contact/', views.contact_us, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),
    path('about/', views.about_us, name='about'),

    path('excursions/', views.excursion_list, name='excursion_list'),
    path('excursions_create/', views.excursion_create, name='excursion_create'),
    path('excursion_detail/<int:pk>/', views.excursion_detail, name='excursion_detail'),
    path('excursion_booking_confirmation/<int:booking_id>/', views.excursion_booking_confirmation, name='excursion_booking_confirmation'),



    path('tours/', views.tours_list, name='tours_list'),
    path('tour_create/', views.tour_create, name='tour_create'),
    path('categories/', views.category_list, name='category_list'),
    path('tour_detail/<int:pk>/', views.tour_detail, name='tour_detail'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),

    path('category/<int:pk>/', views.tour_by_category, name='tour_by_category'),
    path('<str:pk>/', views.article_detail, name='detail'),

]
