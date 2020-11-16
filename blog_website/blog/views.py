from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# posts = [
#      {
#         'author' : 'Kartik',
#         'title' : 'Post 1',
#         'content' : 'Hi! I am Kartik',
#         'date' : '13 November 2020'
#      },
#      {
#         'author' : 'Nikita',
#         'title' : 'Post 2',
#         'content' : 'Hi! I am Nikita',
#         'date' : '14 November 2020'
#      }
# ]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }

    return render(request, 'blog/home.html', context) 

def about(request):
    return render(request, 'blog/about.html')

