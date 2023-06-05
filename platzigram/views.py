'''Platzigram views.'''

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    '''Return a greeting'''
    return HttpResponse("Hello world!!!")


def show_current_time(request):
    '''Return current time'''
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse("Oh, Hi! Current server time is {}".format(str(now)))


def review_objetct_request(request):
    '''testing with pdb module'''
    import pdb; pdb.set_trace()  # para salir, dentro del debugger presiona "c" + Enter
    # print(request)
    return HttpResponse(request.method)


def challenge1(request):
    '''
    Returns an ordered list of numbers using HttpResponse

    Input: http://127.0.0.1:8000/numbers/?numbers=7,5,1,2,3
    
    Output: { "numbers": [1, 2, 3, 5, 7] }
    '''
    print(request.GET)
    print(request.GET['numbers'])
    
    lista_numeros = [int(num) for num in request.GET['numbers'].split(',')]
    json_data = json.dumps({
        'status': 'OK',
        'numbers': sorted(lista_numeros),
        'message': 'Integers sorted sucessfully.'
    }, indent=4)
    # json_data = json.dumps({"numbers": sorted(lista_numeros)})
    return HttpResponse(json_data, content_type='application/json')


def challenge2(request):
    '''
    Returns an ordered list of numbers using JsonResponse

    Input: http://127.0.0.1:8000/numbers-json/?numbers=7,5,1,2,3
    
    Output: { "numbers": [1, 2, 3, 5, 7] }
    '''
    print(request.GET)
    print(request.GET['numbers'])
    
    lista_numeros = [int(num) for num in request.GET['numbers'].split(',')]
    return JsonResponse({"numbers": sorted(lista_numeros)})


def say_hi(request, name, age):
    if age < 12:
        message = "Sorry {}, you are not allowed here".format(name.capitalize())
    else:
        message = "Welcome to Platzigram {}!!!".format(name.capitalize())
    return HttpResponse(message)
