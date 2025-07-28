from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('list/', views.List, name='list'),
    path('stories/', views.Stories, name='stories'),

    path('telugu/', views.Telugu, name='telugu'),
    path('telugu/book/<int:book_id>/', views.telugu_book_detail, name='telugu_book_detail'),

    path('hindi/', views.Hindi, name='hindi'),
    path('hindi/book/<int:book_id>/', views.hindi_book_detail, name='hindi_book_detail'),

    path('english/', views.English, name='english'),
    path('english/book/<int:book_id>/', views.english_book_detail, name='english_book_detail'),

    path('french/', views.French, name='french'),
    path('french/book/<int:book_id>/', views.french_book_detail, name='french_book_detail'),

    path('kannada/', views.Kannada, name='kannada'),
    path('kannada/book/<int:book_id>/', views.kannada_book_detail, name='kannada_book_detail'),
]
