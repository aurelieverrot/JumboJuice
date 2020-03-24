from django.urls import path
from . import views

# . is relative pathing - "from here import views"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('juices/', views.juices_index, name='juices_index'),
    path('juices/new/', views.new_juice, name='new_juice'),
    path('juices/<int:juice_id>', views.juice_detail, name='juice_detail'),
    path('juices/<int:juice_id>/edit', views.juice_update, name='juice_update'),
    path('juice/<int:juice_id>/delete', views.juice_delete, name='juice_delete'),
    path('fruits/new/', views.new_fruit, name='new_fruit'),
    path('fruits/', views.fruits_index, name='index'),
    path('fruits/<int:fruit_id>', views.fruits_detail, name='fruits_detail'),
    # path('fruits/<int:fruit_id>/edit', views.fruits_update, name='fruits_update'),
    # path('fruits/<int:fruit_id>/delete', views.fruits_delete, name='fruits_delete'),
    path('fruits/<int:fruit_id>/add_vitamin', views.add_vitamin, name='add_vitamin'),
    path('accounts/signup', views.signup, name='signup'),
    path('profile/', views.profile_update, name='profile'),
    path('profile/<int:user_id>', views.profile_update, name='profile_update'),
    path('profile/<int:user_id>/delete', views.profile_delete, name='profile_delete')
]

# The name='home' kwarg is optional but will come in handy for referencing the URL in other parts of the app, especially from within templates.

