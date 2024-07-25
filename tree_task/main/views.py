from django.shortcuts import render
from main.models import Menu


def main_menu(request):
    """View to display main menu"""

    result = Menu.objects.all()
    return render(request, "main/index.html", {"menus": result})


def tree(request, path):
    """Displays tree"""

    cur_path = path.split("/")
    return render(
        request,
        "main/index.html",
        {"menu_name": cur_path[0], "menu_item": cur_path[-1]},
    )
