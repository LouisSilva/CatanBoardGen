from django.shortcuts import render

from .scripts.catan_board_generator import create_board

def map_generator(request):
    context = {"context": create_board()}
    return render(request, "map_gen/map_generator.html", context)
