#Restringir acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView

from Atendimento.models import envio_triagem, ficha_de_atendimento
from Triagem.models import triagem
from Triagem.forms import TriagemEnfermaria_Alergias_UpdateForm
from django.db.models import Max
from django.http import Http404
from datetime import datetime

        
# verificar se o paciente possui alergia e depois envia para classificação de risco
class triagem_enfermaria_Alergia_Update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ficha_de_atendimento
    form_class = TriagemEnfermaria_Alergias_UpdateForm
    template_name = 'Triagem/triagem.html'
    success_message = "Alergia cadastrada ao paciente com sucesso!"

    def get(self, request, *args, **kwargs):
        self.hora = kwargs.get('hora')
        self.data = kwargs.get('data')
        self.paciente_envio_triagem_id = kwargs.get('paciente_envio_triagem_id')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['nome_paciente'] = self.object.nome_social        
        context ['tipo_titulo'] = 'Pré-atendimento | ALERGIAS e COMORBIDADES'
        context ['tipo_select'] = f"{self.kwargs['pk']} - {envio_triagem.objects.filter(paciente_envio_triagem_id=self.kwargs['pk']).aggregate(Max('id'))['id__max']}"
        return context
    
    def get(self, request, *args, **kwargs):
        self.hora = kwargs.get('hora')
        self.data = kwargs.get('data')
        self.paciente_envio_triagem_id = kwargs.get('paciente_envio_triagem_id')

        return super().get(request, hora=self.hora, data=self.data, paciente_envio_triagem_id=self.paciente_envio_triagem_id)

    from datetime import datetime

    def get_success_url(self, **kwargs):
        hora_str = self.kwargs.get('hora')
        data_str = self.kwargs.get('data')

        # Convertendo as strings para objetos datetime
        hora = datetime.strptime(hora_str, '%H:%M:%S')
        data = datetime.strptime(data_str, '%Y-%m-%d')

        # Agora, hora e data são objetos datetime, você pode usá-los com strftime
        hora_formatada = hora.strftime('%Y-%m-%d')  # Corrigido: use o formato correto para a hora
        data_formatada = data.strftime('%H:%M:%S')  # Corrigido: use o formato correto para a data

        # Aqui, hora_formatada e data_formatada são strings formatadas
        print(hora_formatada)
        print(data_formatada)
        
        paciente_envio_triagem_id = self.kwargs.get('paciente_envio_triagem_id')

        

        classifica_risco_id = triagem.objects.filter(
                    paciente_triagem_id=paciente_envio_triagem_id,
                    data_envio_a_classificao=data,
                    #hora_envio_a_classificao=hora
                ).first().id
        
        return reverse('Triagem:triagem_classifica_Risco_update', kwargs={'pk': classifica_risco_id})
        """
        ultimo_envio_triagem_id = envio_triagem.objects.filter(
            paciente_envio_triagem_id=paciente_envio_triagem_id ,
            data_envio_triagem=data,
            horario_triagem=hora
        )
        if ultimo_envio_triagem_id.exists():
            ultimo_envio_triagem_id = ultimo_envio_triagem_id.latest('id')
            print(f'último envio_triagem {hora}')
            print(f'último envio_triagem {data}')
            print(f'último envio_triagem {paciente_envio_triagem_id}')


           
            try:
                classifica_risco_id = triagem.objects.filter(
                    paciente_triagem_id=ultimo_envio_triagem_id.id
                    #data_envio_a_classificao=data
                    #hora_envio_a_classificao=hora
                ).first()

                if classifica_risco_id:
                    print(f'valor do classifica risco {classifica_risco_id.id}')
                    return reverse('Triagem:triagem_classifica_Risco_update', kwargs={'pk': classifica_risco_id.id})
                else:
                    # Lide com a situação em que o objeto não foi encontrado
                    raise Http404("Classificação de risco não encontrada para os parâmetros fornecidos.")

            except triagem.DoesNotExist:
                # Lide com a situação em que o objeto não foi encontrado
                raise Http404("Classificação de risco não encontrada para os parâmetros fornecidos.")

        else:
            # Lide com a situação em que o objeto não foi encontrado
            raise Http404("Envio triagem não encontrado para os parâmetros fornecidos.")

       
        
        if ultimo_envio_triagem_id:
            # Busca o ID correspondente na tabela triagem
            #classifica_risco_id = triagem.objects.filter(paciente_triagem__id=ultimo_envio_triagem_id).values_list('id', flat=True).first()
            classifica_risco_id = triagem.objects.filter(paciente_envio_triagem_id=ultimo_envio_triagem_id,data_envio_a_classificao =data, hora_envio_a_classificao = hora )
            print(f'valor do classifica riso {classifica_risco_id}')
            
         

        # Caso não encontre nenhum ID correspondente, retorna a URL padrão
        return super().get_success_url()"""
    
