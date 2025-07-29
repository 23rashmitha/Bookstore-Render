# books/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('list/', views.List, name='list'),
    path('stories/', views.Stories, name='stories'),
    
path('engineering/', views.engineering, name='engineering'),
path('medical/', views.Medical, name='medical'),
path('jee/', views.Jee, name='jee'),

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
    path('mechanical/', views.Mechanical, name='mechanical'),
    path('mechanical/book/<int:book_id>/', views.mechanical_book_detail, name='mechanical_book_detail'),

    path('civil/', views.Civil, name='civil'),
    path('civil/book/<int:book_id>/', views.civil_book_detail, name='civil_book_detail'),

    path('cse/', views.Cse, name='cse'),
    path('cse/book/<int:book_id>/', views.cse_book_detail, name='cse_book_detail'),

    path('ece/', views.Ece, name='ece'),
    path('ece/book/<int:book_id>/', views.ece_book_detail, name='ece_book_detail'),

    path('eee/', views.Eee, name='eee'),
    path('eee/book/<int:book_id>/', views.eee_book_detail, name='eee_book_detail'),

    path('chemical/', views.Chemical, name='chemical'),
    path('chemical/book/<int:book_id>/', views.chemical_book_detail, name='chemical_book_detail'),
    
    # ----------------- Medical (MBBS) -----------------
    path('anatomy/', views.Anatomy, name='anatomy'),
    path('anatomy/book/<int:book_id>/', views.anatomy_book_detail, name='anatomy_book_detail'),

    path('physiology/', views.Physiology, name='physiology'),
    path('physiology/book/<int:book_id>/', views.physiology_book_detail, name='physiology_book_detail'),

    path('biochemistry/', views.Biochemistry, name='biochemistry'),
    path('biochemistry/book/<int:book_id>/', views.biochemistry_book_detail, name='biochemistry_book_detail'),

    path('pharmacology/', views.Pharmacology, name='pharmacology'),
    path('pharmacology/book/<int:book_id>/', views.pharmacology_book_detail, name='pharmacology_book_detail'),

    path('microbiology/', views.Microbiology, name='microbiology'),
    path('microbiology/book/<int:book_id>/', views.microbiology_book_detail, name='microbiology_book_detail'),
    
    path('pathology/', views.Pathology, name='pathology'),
    path('pathology/book/<int:book_id>/', views.pathology_book_detail, name='pathology_book_detail'),
    
    
    path('jee/physics/', views.JeePhysics, name='jee_physics'),
    path('jee/physics/<int:book_id>/', views.jee_physics_book_detail, name='jee_physics_book_detail'),

    path('jee/chemistry/', views.JeeChemistry, name='jee_chemistry'),
    path('jee/chemistry/<int:book_id>/', views.jee_chemistry_book_detail, name='jee_chemistry_book_detail'),

    path('jee/mathematics/', views.JeeMath, name='jee_math'),
    path('jee/mathematics/<int:book_id>/', views.jee_math_book_detail, name='jee_math_book_detail'),

    path('jee/mock/', views.JeeMock, name='jee_mock'),
    path('jee/mock/<int:book_id>/', views.jee_mock_book_detail, name='jee_mock_book_detail'),


]
