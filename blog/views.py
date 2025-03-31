from django.shortcuts import render

posts = [  
    { 
        'id': 0, 
        'location': 'Остров отчаянья', 
        'date': '30 сентября 1659 года', 
        'category': 'travel', 
        'text': '''Наш корабль, застигнутый в открытом море 
                   страшным штормом, потерпел крушение. 
                   Весь экипаж, кроме меня, утонул...''', 
    }, 
    { 
        'id': 1, 
        'location': 'Остров отчаянья', 
        'date': '1 октября 1659 года', 
        'category': 'not-my-day', 
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло 
                   с мели приливом и пригнало гораздо ближе к берегу...''',
    }, 
    { 
        'id': 2, 
        'location': 'Остров отчаянья', 
        'date': '25 октября 1659 года', 
        'category': 'not-my-day', 
        'text': '''Всю ночь и весь день шёл дождь и дул сильный 
                   порывистый ветер. Корабль за ночь разбило в щепки...''',
    }
]

def index(request):
    print("DEBUG: posts =", posts)  
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return render(request, 'blog/404.html', status=404)
    return render(request, 'blog/detail.html', {'post': post})

def category_view(request, category_slug):
    return render(request, 'blog/category.html', {'category': category_slug})

def about(request):
    return render(request, 'blog/about.html')

def rules(request):
    return render(request, 'blog/rules.html')
