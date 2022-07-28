from django.urls import path
from . import views

app_name = 'plataforma'
urlpatterns = [

    path('', views.index, name='index'),
    path('edicao/<int:edicao_id>/', views.detail, name='detail'),
    path('edicao/noticia/<int:noticia_id>/', views.detailnoticia, name='detailnoticia'),

    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logoutView, name='logout'),

    path('cadastroedicao/', views.CadastroEdicao.as_view(), name='cadastroedicao'),
    path('cadastronoticia/', views.CadastroNoticia.as_view(), name='cadastronoticia'),
    path('cadastrocomentario/', views.CadastroComentario.as_view(), name='cadastrocomentario'),
    path('cadastrocolunista/', views.CadastroColunista.as_view(),name='cadastrocolunista'),
]