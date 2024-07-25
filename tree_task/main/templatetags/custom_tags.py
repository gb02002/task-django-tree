from main.models import MenuBullet
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('main/menu.html')
def draw_menu(menu_name: str = None, menu_item: str = None):

    def get_menu(menu_item: str = None, submenu: list = None):
        print("We do smth in tag")
        menu = list(items.filter(parent=None)) if menu_item is None \
            else list(items.filter(parent__name=menu_item))
        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (IndexError, TypeError):
            pass
        try:
            return get_menu(items.get(name=menu_item).parent.name, menu)
        except AttributeError:
            return get_menu(submenu=menu)
        except ObjectDoesNotExist:
            return menu

    items = MenuBullet.objects.filter(menu__name=menu_name)
    return {'menu': get_menu()} if menu_name == menu_item \
        else {'menu': get_menu(menu_item)}


@register.filter()
def lower(value):  # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()