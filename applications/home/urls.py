from django.urls import path
# vistas importadas
from . import views

urlpatterns = [

    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListviwe.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
    path(
        'add-prueba/',
        views.PruebaCreateView.as_view(),
        name='prueba_add'),
    path(
        'resume-foundation/',
        views.ResumeFoundationView.as_view(),
        name='resume_foundation'),
]
