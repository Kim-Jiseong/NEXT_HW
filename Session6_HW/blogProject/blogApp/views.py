from django.shortcuts import render,redirect
from .models import Article

# Create your views here.
def index(request):
    drama = Article.objects.filter(choice = 'drama').count()
    movie = Article.objects.filter(choice = 'movie').count()
    programming = Article.objects.filter(choice = 'programming').count()
    return render(request, 'index.html', {'drama': drama, 'movie':movie, 'programming':programming})

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article': article})

def  new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            choice = request.POST['choice'],
        )
        return redirect('detail', article_pk=new_article.pk)

    return render(request, 'new.html')

def drama(request):
    dramas = Article.objects.filter(choice = 'drama')
    return render(request, 'drama.html', {'dramas':dramas}) 

def movie(request):
    movies = Article.objects.filter(choice = 'movie')
    return render(request, 'movie.html', {'movies':movies})

def programming(request):
    programmings = Article.objects.filter(choice = 'programming')
    return render(request, 'programming.html', {'programmings':programmings})
