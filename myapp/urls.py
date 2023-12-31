from django.urls import path
from  .views import AddPlayer
urlpatterns = [
    path('add_player/', AddPlayer, name='add_player'),
    # Add other URL patterns as needed
]
