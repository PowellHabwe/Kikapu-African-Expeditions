from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Tour, Category, Tour_Booking, Excursion, ExcusionBooking
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from . import forms

from .forms import BookingForm, ExcursionBookingForm


def category_list(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    return render(request, 'articles/category_list.html', {'categories': categories})

def tour_by_category(request, pk):
    category = get_object_or_404(Category, id=pk)  # Change slug to id
    tours_in_category = Tour.objects.filter(category=category)
    return render(request, 'articles/tour_by_category.html', {'category': category, 'tours': tours_in_category})

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles })

def article_detail(request, pk):  # Change slug to id
    article = Article.objects.get(id=pk)  # Change slug to id
    return render(request, 'articles/article_detail.html', {'article': article })

def gallery(request):  # Change slug to id
    return render(request, 'articles/gallery.html')

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form })

def tours_list(request):
    mytours = Tour.objects.all().order_by('date')
    return render(request, 'articles/tours_list.html', {'mytours': mytours })


def tour_detail(request, pk):
    tour = get_object_or_404(Tour, id=pk)

    if request.method == 'POST':
        form = BookingForm(tour_id=tour.id, data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tour = tour
            booking.category_name = tour.category.category_name if tour.category else None  # Save category name
            booking.save()
            
            first_name = booking.first_name
            last_name = booking.last_name
            category_name = booking.category_name
            booked_tour = booking.tour
            selected_pax = booking.selected_pax
            travel_date = booking.travel_date
            number_of_people = booking.number_of_people
            email = booking.email

            # Format the email body
            email_subject = 'New Booking'
            email_body = f"{first_name} {last_name} booked a tour on {travel_date}.\n\n"
            email_body += f"Details:\n"
            email_body += f"Tour: {booked_tour}\n"
            email_body += f"Category Name: {category_name}\n"
            email_body += f"Selected Pax: {selected_pax}\n"
            email_body += f"Number of People: {number_of_people}\n"
            email_body += f"Contact Email: {email}\n"

            # Send the email
            send_mail(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,
                # ['powellhabwe@gmail.com'],  # Add more recipients as needed
                ['kikapuafricanexpeditions@gmail.com'],  # Add more recipients as needed
                fail_silently=False
            )

            return redirect('articles:booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm(tour_id=tour.id)  # Make sure to pass the tour_id

    context = {'tour': tour, 'form': form}
    return render(request, 'articles/tour_detail.html', context)


@login_required(login_url="/accounts/login/")
def tour_create(request):
    if request.method == 'POST':
        form = forms.CreateTour(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('articles:tours_list')
    else:
        form = forms.CreateTour()
    return render(request, 'articles/tour_create.html', {'form': form })


def about_us(request):
    return render(request, 'articles/about.html')


def contact_us(request):
    if request.method == 'POST':
        message = request.POST['message']
        sender_email = request.POST['email']
        email_body = f"Sender's Email: {sender_email}\n\n{message}"
        send_mail(
            'Contact Form',
            email_body,
            settings.EMAIL_HOST_USER,
            ['kikapuafricanexpeditions@gmail.com'],
            # ['powellhabwe@gmail.com'],
            fail_silently=False
        )
    return render(request, 'articles/contact-form.html')



def excursion_list(request):
    excursions = Excursion.objects.all().order_by('date')
    return render(request, 'articles/excursion_list.html', {'excursions': excursions })

def excursion_detail(request, pk):  # Change slug to id
    excursion = Excursion.objects.get(id=pk)  # Change slug to id
    return render(request, 'articles/excursion_detail.html', {'excursion': excursion })

def excursion_detail(request, pk):
    excursion = get_object_or_404(Excursion, id=pk)

    if request.method == 'POST':
        form = ExcursionBookingForm(excursion_id=excursion.id, data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.excursion = excursion
            booking.save()
            
            first_name = booking.first_name
            last_name = booking.last_name
            booked_excursion = booking.excursion
            travel_date = booking.travel_date
            number_of_people = booking.number_of_people
            email = booking.email

            # Format the email body
            email_subject = 'New Booking'
            email_body = f"{first_name} {last_name} booked a tour on {travel_date}.\n\n"
            email_body += f"Details:\n"
            email_body += f"Excursion: {booked_excursion}\n"
            email_body += f"Number of People: {number_of_people}\n"
            email_body += f"Contact Email: {email}\n"

            # Send the email
            send_mail(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,
                # ['powellhabwe@gmail.com'],  # Add more recipients as needed
                ['kikapuafricanexpeditions@gmail.com'],  # Add more recipients as needed
                fail_silently=False
            )

            return redirect('articles:excursion_booking_confirmation', booking_id=booking.id)
    else:
        form = ExcursionBookingForm(excursion_id=excursion.id)  # Make sure to pass the tour_id

    context = {'excursion': excursion, 'form': form}
    return render(request, 'articles/excursion_detail.html', context)


@login_required(login_url="/accounts/login/")
def excursion_create(request):
    if request.method == 'POST':
        form = forms.CreateExcursion(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('excursions:excursion_list')
    else:
        form = forms.CreateExcursion()
    return render(request, 'articles/excursion_create.html', {'form': form })



def booking_confirmation(request, booking_id):
    print("Booking ID:", booking_id)
    booking = get_object_or_404(Tour_Booking, id=booking_id)
    # print("Booking Object:", booking)
    context = {'booking': booking}
    return render(request, 'articles/booking_confirmation.html', context)

def excursion_booking_confirmation(request, booking_id):
    print("Booking ID:", booking_id)
    booking = get_object_or_404(ExcusionBooking, id=booking_id)
    # print("Booking Object:", booking)
    context = {'booking': booking}
    return render(request, 'articles/excursion_booking_confirmation.html', context)

