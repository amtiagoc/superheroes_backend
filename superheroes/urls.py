from django.urls import path
from . import views
  
urlpatterns = [
    path('',views.apiOverview, name='home'),
    path('crear/', views.add_superheroe, name='add-superheroe'),
    path('listar/', views.view_superheroe, name='listar-superheroes'),
    path('actualizar/<str:pk>/', views.update_superheroe, name='update-superheroe'),
    path('eliminar/<str:pk>/', views.delete_superheroe, name='delete-superheroe'),
]