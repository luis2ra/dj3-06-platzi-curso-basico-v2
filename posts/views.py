'''Posts views.'''
# Django
from django.shortcuts import render
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Mont Black',
        'user': 'Luis Altuve',
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Mountain',
        'user': 'Luis Alfonso',
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'picture': 'https://picsum.photos/200/200/?image=1000'
    },
    {
        'name': 'Sea',
        'user': 'Pedro Perez',
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'picture': 'https://picsum.photos/200/200/?image=700'
    },
]

# Create your views here.
def list_posts(request):
    '''List existing posts.'''
    content = []
    for post in posts:
        content.append('''
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        '''.format(**post))
    return HttpResponse('<br>'.join(content))
