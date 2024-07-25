from django.urls import path

from .views import main_menu, tree

urlpatterns = [
    path('', main_menu, name='main_menu'),
    path('<path:path>/', tree, name='draw_menu'),
]
