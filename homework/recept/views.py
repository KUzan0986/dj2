from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def food(request, op1, op2=None):
    dish = DATA.get(op1, None)
    if not dish:
        stri = "Я не знаю такого блюда =("
    else:
        if not op2:
            mil = 1
        else:
            mil = int(op2)
        stri = f"{op1}<br></br>"
        for a in dish:
            stri += f"{a}: {dish.get(a)*mil}<br></br>"
    return HttpResponse(stri)
# Create your views here.
