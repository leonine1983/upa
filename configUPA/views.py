from django.shortcuts import render, redirect
from .forms import VideoForm
from django.views.generic import CreateView, UpdateView, DetailView
from configUPA.models import Notificate_system
from django.contrib.auth.models import User
from  .models import config_Marquee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy




# video bacgroud
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Atendimento:painel')
    else:
        form = VideoForm()
    return render(request, 'configUPA/config.html', {
        'form' : form,
        'backgroud_painel': 'oi'})


# CONFIGURA O LETREIRO ---------------------------------------------------------
class letreiroCreateView(LoginRequiredMixin, CreateView):
    model = config_Marquee
    fields = '__all__'
    template_name = 'configUPA/config.html'
    success_url = reverse_lazy("Atendimento:painel")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['letreiroCreate'] = 'oi'
        return context
    
# CONFIGURA O notificações ---------------------------------------------------------
class Create_notifica(LoginRequiredMixin, CreateView):
    model = Notificate_system
    fields = '__all__'
    template_name = 'configUPA/notificate_create.html'

"""


Para enviar uma notificação para todos os usuários de uma só vez, você precisa percorrer todos os usuários no seu banco de dados e criar um objeto Notificate_system para cada um deles. Aqui está um exemplo de como você poderia fazer isso:

python
Copy code
from django.contrib.auth.models import User
from .models import Notificate_system

def enviar_notificacao_para_todos(descricao):
    # Obtém todos os usuários
    usuarios = User.objects.all()

    # Para cada usuário, cria uma notificação
    for usuario in usuarios:
        notificacao = Notificate_system.objects.create(
            user=usuario,
            description=descricao,
            visto=False
        )
        # Salva a notificação
        notificacao.save()

"""


    
# CONFIGURA O LETREIRO ---------------------------------------------------------
def handler404(request, exception=None):
    context = {'error_message': 'Oops! A página que você está procurando não foi encontrada.'}
    return render(request, 'configUPA/error-404.html', context, status=404)

def handler500(request):
    context = {'error_message': 'Oops! Houve um erro interno no servidor.'}
    return render(request, 'configUPA/error-500.html', context, status=500)
