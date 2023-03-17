from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('registro/', views.registro, name="registrar"),
    


    path('', views.listaTarefa, name='tarefa'),

    path('detalhes/<str:pk>/', views.detalhesTarefa, name='detalhes'),
    path('adicionar/', views.adicionarTarefa, name='adicionar-tarefa'),
    path('atualizar/<str:pk>/', views.atualizarTarefa, name='atualizar-tarefa'),
    path('apagar/<str:pk>/', views.apagarTarefa, name='apagar-tarefa')

]    