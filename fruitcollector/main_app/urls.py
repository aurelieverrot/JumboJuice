from django.urls import path
from . import views

# . is relative pathing - "from here import views"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('juices/new/', views.new_juice, name='new_juice'),
    path('juices/', views.juices_index, name='juices_index'),
    path('fruits/new/', views.new_fruit, name='new_fruit'),
    path('fruits/', views.fruits_index, name='index'),
    path('fruits/<int:fruit_id>', views.fruits_detail, name='detail'),
    # path('fruits/<int:fruit_id>/edit', views.fruits_update, name='fruits_update'),
    # path('fruits/<int:fruit_id>/delete', views.fruits_delete, name='fruits_delete'),
    # path('fruits/<int:fruit_id>/add_smoothie/', views.add_smoothie, name='add_smoothie'),
    # path('fruits/<int:fruit_id>/assoc_vitamin/<int:vitamin_id>', views.assoc_vitamin, name='assoc_vitamin'),
    path('accounts/signup', views.signup, name='signup'),
]

# The name='home' kwarg is optional but will come in handy for referencing the URL in other parts of the app, especially from within templates.

