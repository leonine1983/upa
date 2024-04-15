
from .forms import VideoForm
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from  .models import config_Marquee

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.models import Group, User
from .models import Notificate_system

from django import forms
from django.contrib.auth.models import Group



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


class Detail_notifica(LoginRequiredMixin, DetailView):
    model = Notificate_system
    template_name = 'configUPA/notificate_detail.html'
    context_object_name = 'notifica_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["detail_view"] = True
        return context
    

class All_notifica(LoginRequiredMixin, View):
    template_name = 'configUPA/notificate_detail.html'

    def get(self, request, *args, **kwargs):
        notifica_all = Notificate_system.objects.filter(user=self.request.user)
        context = {
            'notifica_all': notifica_all,
            'detail_view': False
        }
        return render(request, self.template_name, context)
    



class NotificateForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False, label='Grupo', widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control ckeditor'}))
    



class Create_notifica(LoginRequiredMixin, View):
    template_name = 'configUPA/notificate_create.html'

    def get(self, request):
        form = NotificateForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NotificateForm(request.POST)
        
        if form.is_valid():
            group = form.cleaned_data['group']
            description = form.cleaned_data['description']
            
            if group:
                users_to_notify = group.user_set.all()
            else:
                users_to_notify = User.objects.all()

            for user in users_to_notify:
                Notificate_system.objects.create(user=user, description=description)

            return redirect(reverse_lazy('configUPA:notifica_create'))

        return render(request, self.template_name, {'form': form})

class SuccessNotificationView(LoginRequiredMixin, View):
    template_name = 'configUPA/success_notification.html'

    def get(self, request):
        return render(request, self.template_name)
    

def noti_visto(request, pk):
    msg = Notificate_system.objects.filter(pk=pk)
    for m in msg:
        m.visto = True
        m.save()
    return redirect(reverse_lazy('configUPA:notifica', kwargs={'pk':pk}))

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

def handler500(request, *args, **kwargs):
    context = {'error_message': 'Oops! Houve um erro interno no servidor.'}
    return render(request, 'configUPA/error-500.html', context, status=500)

