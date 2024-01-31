from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article, Tour, Category, Tour_Booking

def homepage(request):
    # return render('this is the home page')
    home_categories = Category.objects.filter(home_category=True)[:2]
    home_articles = Article.objects.filter(home_article=True)

    context = {'home_categories': home_categories, 'home_articles':home_articles}
    return render(request, 'homepage.html', context)

def about(request):
    return render(request, 'about.html')
