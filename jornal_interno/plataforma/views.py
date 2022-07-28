from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Colunista, Edicao,Noticia,Comentario
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'plataforma/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            if hasattr(request.user, 'colunista'):
                return HttpResponseRedirect(reverse('plataforma:index'))
        else:
            erro = 'Email e senha inválidas!'
            return render(request, 'plataforma/login.html', {'erro': erro})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('plataforma:index'))

class CadastroColunista(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'plataforma/cadastrocolunista.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        cpf = request.POST['cpf']
        senha = request.POST['senha']
        if username and cpf and senha:
            user = User.objects.create_user(
                username=username, password=senha)
            Colunista.objects.create(user=user, cpf=cpf)
            return HttpResponseRedirect(reverse('plataforma:login'))
        else:
            erro = 'Informe corretamente os parâmetros necessários!'
            return render(request, 'plataforma/cadastrocolunista.html', {'erro': erro})

@method_decorator(login_required(login_url="/login/"), name='dispatch')
class CadastroEdicao(View):
    def get(self, request, *args, **kwargs):
        colunista = request.user.colunista
        contexto = {'colunista': colunista}
        return render(request, 'plataforma/cadastraredicao.html', contexto)

    def post(self, request, *args, **kwargs):
        texto = request.POST['texto']

        if texto:
            if hasattr(request.user, 'colunista'):
                edicao = Edicao(colunista=request.user.colunista, texto = texto)
                edicao.save()
                return HttpResponseRedirect(reverse('plataforma:index'))
            else:
                erro = 'Usuario não logado!'
                return render(request, 'plataforma/login.html', {'erro': erro})
        else:
            erro = 'Informe corretamente os parâmetros necessários!'
            return render(request, 'plataforma/cadastraredicao.html', {'erro': erro})

@method_decorator(login_required(login_url="/login/"), name='dispatch')
class CadastroNoticia(View):
    def get(self, request, edicao_id, *args, **kwargs):
        colunista = request.user.colunista
        edicao = get_object_or_404(Edicao, pk=edicao_id)
        contexto = {'colunista': colunista,'edicao': edicao}
        return render(request, 'plataforma/cadastrarnoticia.html', contexto)

    def post(self, request, edicao_id, *args, **kwargs):
        texto = request.POST['texto']
        edicao = get_object_or_404(Edicao, pk=edicao_id)

        if texto:
            if hasattr(request.user, 'colunista'):
                noticia = Noticia(colunista=request.user.colunista, texto = texto, edicao = edicao)
                noticia.save()
                return HttpResponseRedirect(reverse('plataforma:detail', args=(edicao_id,)))
            else:
                erro = 'Usuario não logado!'
                return render(request, 'plataforma/login', {'erro': erro})
        else:
            erro = 'Informe corretamente os parâmetros necessários!'
            return render(request, 'plataforma/cadastrarnoticia.html', {'erro': erro})

@method_decorator(login_required(login_url="/login/"), name='dispatch')
class CadastroComentario(View):
    def get(self, request, noticia_id, *args, **kwargs):
        colunista = request.user.colunista
        noticia = get_object_or_404(Noticia, pk=noticia_id)
        contexto = {'colunista': colunista, 'noticia': noticia}
        return render(request, 'plataforma/cadastrarcomentario.html', contexto)

    def post(self, request, noticia_id, *args, **kwargs):
        texto = request.POST['texto']
        noticia = get_object_or_404(Noticia, pk=noticia_id)
    
        if texto:
            if hasattr(request.user, 'colunista'):
                comentario = Comentario(colunista=request.user.colunista, texto = texto, noticia = noticia)
                comentario.save()
                return HttpResponseRedirect(reverse('plataforma:detailnoticia', args=(noticia_id,)))
            else:
                erro = 'Usuario não logado!'
                return render(request, 'plataforma/login', {'erro': erro})
        else:
            erro = 'Informe corretamente os parâmetros necessários!'
            return render(request, 'plataforma/cadastrarcomentario.html', {'erro': erro})
    

def index(request):
    edicao_list = Edicao.objects.order_by('-data_pub')[:5]
    context = {'edicao_list': edicao_list}
    return render(request,'plataforma/index.html', context)

def detail(request, edicao_id):
    edicao = get_object_or_404(Edicao, pk=edicao_id)
    return render(request,'plataforma/detail.html',{'edicao': edicao})

def detailnoticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request,'plataforma/detailnoticia.html',{'noticia': noticia})