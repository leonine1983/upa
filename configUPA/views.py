from django.shortcuts import render, redirect
from .forms import VideoForm
from django.views.generic import CreateView, UpdateView
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
        'backgroud_painel': ''})


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
