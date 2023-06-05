'''Posts views.'''
# Django
from django.shortcuts import render
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Black',
        'user': {
            'name': 'Luis Altuve',
            'age': 27
        },
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'photo': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'title': 'Mountain',
        'user': {
            'name': 'Luis Alfonso',
            'age': 16
        },
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'photo': 'https://picsum.photos/200/200/?image=1000'
    },
    {
        'title': 'Sea',
        'user': {
            'name': 'Pedro Perez',
            'age': 22
        },
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'photo': 'https://picsum.photos/200/200/?image=700'
    },
]

# Create your views here.
def list_posts(request):
    '''List existing posts.'''
    content = []
    for post in posts:
        content.append('''
            <p><strong>{title}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{photo}"/></figure>
        '''.format(**post))
    return HttpResponse('<br>'.join(content))


def list_posts_with_templates(request):
    '''List existing posts using templates.'''
    return render(request, 'feed.html', context={'posts': posts})
