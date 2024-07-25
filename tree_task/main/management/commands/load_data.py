from django.core.management.base import BaseCommand
from django.db import IntegrityError
from main.models import Menu, MenuBullet

ID_LENGTH = 4


class Command(BaseCommand):
    _class = Menu
    name = "MENU"
    current_id = ["A"] * ID_LENGTH
    menu_size: int = 4
    menu_depth: int = 4

    def handle(self, *args, **kwargs):
        """Основная точка входа команды. Создает несколько меню с заданными именами."""

        menu_names = ["first menu", "second menu", "third menu", "forth menu"]
        for menu_name in menu_names:
            self.create_menu(menu_name)

    def create_menu(self, menu_name: str) -> None:
        """Создает меню с заданным именем и добавляет к нему пункты меню"""

        menu = self.create_menu_object(menu_name)
        self.create_menu_bullets(level_name=menu.name, menu=menu, depth=2)

    def create_menu_object(self, menu_name: str) -> Menu:
        """Создает объект меню."""

        return Menu.objects.create(name=menu_name)

    def create_menu_bullets(self, level_name: str, menu: Menu, parent: MenuBullet = None, depth: int = 0) -> None:
        """Рекурсивно создает пункты меню и вложенные пункты меню до заданной глубины."""

        if depth >= self.menu_depth:
            self.create_leaf_bullet(menu, parent)
        else:
            for i in range(self.menu_size):
                menu_bullet = self.create_menu_bullet(level_name, menu, parent, depth, i)
                self.create_menu_bullets(level_name, menu, menu_bullet, depth + 1)

    def create_leaf_bullet(self, menu: Menu, parent: MenuBullet) -> None:
        """Создает конечный пункт меню (leaf bullet) с ссылкой"""

        try:
            menu_bullet = MenuBullet.objects.create(
                name="Menu булет",
                menu=menu,
                parent=parent,
            )
            MenuBullet.objects.create(
                name="Ссылочка",
                menu=menu,
                parent=menu_bullet,
                url=self.generate_link(),
            )
        except IntegrityError:
            pass

    def create_menu_bullet(self, level_name: str, menu: Menu, parent: MenuBullet, depth: int, index: int) -> MenuBullet:
        """Создает булет"""

        unique_id = self.generate_next_id()
        menu_bullet_name = f"{unique_id} {index+1} булета на глубине {depth+1} {level_name}"
        return MenuBullet.objects.create(
            name=menu_bullet_name,
            menu=menu,
            parent=parent,
        )

    def generate_next_id(self, id_length: int = ID_LENGTH) -> str:
        """Генерирует следующий уникальный id"""

        for i in range(id_length - 1, -1, -1):
            if self.current_id[i] == 'Z':
                self.current_id[i] = 'A'
            else:
                self.current_id[i] = chr(ord(self.current_id[i]) + 1)
                break
        return "".join(self.current_id)

    def generate_link(self) -> str:
        """Генерирует ссылку для пункта меню"""

        return "https://nl.pinterest.com/search/pins/?q=kittens"