from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
Api_Key="c4704c91a8d14871925651546267afdd"

# Create your views here.
@csrf_exempt
def get_news(request):
    
    category = request.GET.get('category')
    
    
    if category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={Api_Key}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    context = {
            'articles' : articles
    }

    return render(request, 'home.html', context)