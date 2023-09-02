from django.shortcuts import render

from .scripts.catan_board_generator import create_board

tile_sizes = [
        "left:34.99655%;top:24.45%",
        "left:50%;top:24.45%",
        "left:65.00345%;top:24.45%",
        "left:27.494825000000002%;top:37.225%",
        "left:42.498275%;top:37.225%",
        "left:57.501725%;top:37.225%",
        "left:72.505175%;top:37.225%",
        "left:19.993100000000002%;top:50%",
        "left:34.99655%;top:50%",
        "left:50%;top:50%",
        "left:65.00345%;top:50%",
        "left:80.0069%;top:50%",
        "left:27.494825000000002%;top:62.775%",
        "left:42.498275%;top:62.775%",
        "left:57.501725%;top:62.775%",
        "left:72.505175%;top:62.775%",
        "left:34.99655%;top:75.55%",
        "left:50%;top:75.55%",
        "left:65.00345%;top:75.55%"
        ]

def map_generator(request):
    generated_board = create_board()
    for i in range(len(generated_board)):
        generated_board[i].append(tile_sizes[i])

    context = {"tile_data": generated_board}
    return render(request, "map_gen/map_generator2.html", context)
