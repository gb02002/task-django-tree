from django.db import models
from django.db.models import Manager


# Create your models here.


class Menu(models.Model):
    """Модель для меню"""

    menu_id = models.AutoField(primary_key=True)
    name = models.CharField("Menu name", max_length=50, unique=True, blank=False)
    description = models.TextField("Description", max_length=300, blank=True)

    objects = Manager()

    class Meta:
        ordering = ["menu_id"]
        verbose_name = "Инстанс меню"

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.menu_id}, {self.name}"


class MenuBullet(models.Model):
    """Пункт меню"""

    menu_bullet_id = models.AutoField(primary_key=True)
    name = models.CharField(
        "Название пункта меню", max_length=50, unique=True, blank=False
    )
    url = models.URLField(max_length=50, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name="menu_bullets"
    )

    objects = Manager()

    class Meta:
        ordering = ["menu_bullet_id"]
        verbose_name = "Пункт меню"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.menu_bullet_id}, {self.name}"
