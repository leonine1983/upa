#Restringir acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic.edit import UpdateView
from Triagem.models import triagem


# verificar a classificação de risco
class triagem_classifica_Risco_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    fields = ['classifica_tipo']
    model = triagem
    template_name = 'Triagem/triagem.html' 
    success_message = 'Vinculação de classificação risco feita com sucesso!'      

   
    # Chamar o model Triagem
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """Criar as condicionais para a classificação de risco"""    
        # variaves da PA
        cor1 = 'Vermelho'
        cor2 = 'Laranja'
        cor3 = 'Amarelo'
        cor4 = 'Verde'

        def verificar_pressao_arterial():
            pa_value = self.object.pressao_arterial_PA
            #pa_max = pressao_arterial_PA_2 

            if pa_value <= 120:
                pa = 'PA: Pressão arterial sistólica menor ou igual a 90 mmHg (milímetros de mercúrio), indica uma classificação de risco vermelho (emergência).'
                pAcor = cor1
            elif 91 <= pa_value <= 100:
                pa = 'PA: Pressão arterial sistólica entre 91 e 100 mmHg, indica uma classificação de risco laranja (muito urgente).'
                pAcor = cor2
            elif 101 <= pa_value <= 110:
                pa = 'PA: Pressão arterial sistólica entre 101 e 110 mmHg, indica uma classificação de risco amarelo (urgente).'
                pAcor = cor3
            else:
                pa = 'PA: Pressão arterial sistólica maior que 110 mmHg: indica uma classificação de risco verde (pouco urgente) ou azul (não urgente), dependendo de outros sintomas e condições do paciente.'
                pAcor = cor4
            return pa, pAcor            
        pa, pAcor = verificar_pressao_arterial()


        def verifica_Frequencia_Cardiaca():
            fC_value = self.object.frequencia_cardiaca_FC

            if fC_value <= 39:
                fc = 'FC:  Frequência cardíaca abaixo de 40, indica uma classificação de risco vermelho (emergência).'
                fCor = cor1
            if fC_value >= 131:
                fc = 'FC: Frequência cardíaca acima de 130 batimentos por minuto: indica uma classificação de risco vermelho (emergência)..'
                fCor = cor1                        
            elif (40 <= fC_value <= 50) or (120 <= fC_value <= 130):
                fc = 'FC:  Frequência cardíaca entre 40 e 50 ou entre 120 e 130 batimentos por minuto: indica uma classificação de risco amarelo (urgência).'
                fCor = cor2
            elif (51 <= fC_value <= 99) :
                fc = 'FC:  Frequência cardíaca entre 50 e 100 batimentos por minuto: indica uma classificação de risco verde (pouca urgência).'
                fCor = cor3
            elif (100 <= fC_value <= 120) :
                fc = 'FC: Frequência cardíaca entre 100 e 120 batimentos por minuto: indica uma classificação de risco verde.'
                fCor = cor3
            else:
                fc = 'FC: Por favor verifique novamente a frequência cardíaca do paciente'
                fCor = cor1
            return fc, fCor
        fc, fCor = verifica_Frequencia_Cardiaca()

        def verifica_Frequencia_Respiratoria():
            fR_value = self.object.frequencia_cardiaca_FC
            if fR_value <= 8:
                fr = 'FR: Frequência respiratória menor ou igual a 8 respirações por minuto: Cor vermelha. Indica uma condição grave e necessidade de atendimento imediato.'
                fRcor = cor1                       
            elif 9 <= fR_value <= 14:
                fr = 'FR: Frequência respiratória entre 9 e 14 respirações por minuto: Cor laranja. Indica uma condição potencialmente grave e necessidade de atendimento rápido'
                fRcor = cor2  
            elif 15 <= fR_value <= 20:
                fr = 'FR: Frequência respiratória entre 15 e 20 respirações por minuto: Cor amarela. Indica uma condição moderada e necessidade de atendimento em tempo adequado.'
                fRcor = cor3            
            else:
                fr = 'FR: Frequência respiratória maior ou igual a 21 respirações por minuto: Cor verde. Indica uma condição menos grave, mas que ainda requer avaliação médica'
                fRcor = cor4
            return fr, fRcor
        fr, fRcor = verifica_Frequencia_Respiratoria() 

        def verifica_Saturação_Oxigenio():
            spO_value = self.object.saturacao_de_oxigenio_SPO2
            if spO_value <= 92:
                spo = 'SPO²: Saturação de oxigênio menor ou igual a 92%: Cor vermelho. Condição grave e necessidade de atendimento imediato, risco de insuficiência respiratória.'
                spOcor = cor1                       
            elif 93 <= spO_value <= 94:
                spo = 'SPO²: Saturação de oxigênio entre 93% e 94%: Cor laranja. Indica uma condição potencialmente grave e necessidade de atendimento rápido. Embora a saturação esteja um pouco acima do limite da cor azul, ainda é considerada uma faixa preocupante.'
                spOcor = cor2             
            else:
                spo = 'SPO²: Saturação de oxigênio acima de 94%: Avaliação da saturação de oxigênio, considerada dentro dos parâmetros normais.'
                spOcor = cor4
            return spo, spOcor
        spo, spOcor = verifica_Saturação_Oxigenio()	

        def verifica_hemiglicoteste():
            hgT_value = self.object.hemoglicoteste_HGT
            if hgT_value >= 126:
                hgt = 'HGT: Sintomas de Diabetes: Valores iguais ou superiores a 126 mg/dL (7,0 mmol/L) em jejum, confirmados em duas ocasiões distintas, podem indicar a presença de diabetes.'
                hgTcor = cor1                       
            elif 100 <= hgT_value <= 125:
                hgt = 'HGT: Sintomas de Pré-diabetes: Valores entre 100 e 125 mg/dL (5,6 a 6,9 mmol/L) em jejum podem indicar um estado de pré-diabetes. Isso significa que a glicose está elevada, mas ainda não atingiu o limiar para o diagnóstico de diabetes.'
                hgTcor = cor2  
            elif 70 <= hgT_value <= 99:
                hgt = 'HGT: Níveis normais de glicose: Valores entre 70 a 99 mg/dL (3,9 a 5,5 mmol/L).'
                hgTcor = cor4            
            else:
                hgt = 'HGT:  Valores inferiores a 70 mg/dL (3,9 mmol/L) em jejum podem indicar a ocorrência de hipoglicemia.'
                hgTcor = cor1
            return hgt, hgTcor
        hgt, hgTcor = verifica_hemiglicoteste()

        def verifica_peso():
            altura_info = self.object.altura
            peso_info = self.object.peso
            pesO_value =round((peso_info/(altura_info*altura_info)), 2)
            if pesO_value <= 18.5:
                peso = 'Baixo peso: IMC abaixo de 18,5 kg/m². Indica uma faixa de peso considerada abaixo do recomendado para a altura e pode estar associada a riscos de desnutrição e fragilidade.'
                pesOcor = cor2                       
            elif 18.6 <= pesO_value <= 24.9:
                peso = 'Peso normal: IMC entre 18,5 e 24,9 kg/m². Nessa faixa, o peso é considerado saudável em relação à altura.'
                pesOcor = cor1  
            elif 25 <= pesO_value <= 29.9:
                peso = 'Sobrepeso: IMC entre 25 e 29,9 kg/m². Indica uma faixa de peso acima do ideal para a altura e pode estar associada a riscos de doenças como diabetes tipo 2, doenças cardiovasculares e outras condições relacionadas à obesidade.'
                pesOcor = cor3
            elif 30 <= pesO_value <= 34.9:
                peso = 'Obesidade grau 1: IMC entre 30 e 34,9 kg/m²'
                pesOcor = cor1
            elif 35 <= pesO_value <= 39.9:
                peso = 'Obesidade grau 2: IMC entre 35 e 39,9 kg/m².'
                pesOcor = cor1
            else:
                peso = 'Obesidade grau 3 (obesidade mórbida): IMC igual ou superior a 40 kg/m².'
                pesOcor = cor1           
            
            return peso, pesOcor, peso_info, altura_info, pesO_value
        peso, pesOcor, peso_info, altura_info, pesO_value= verifica_peso()	

        def verifica_temp():  
            temP_value = self.object.temperatura_TEMP 
            if temP_value >= 40.1:
                temp = 'Hipertermia grave: Temperatura do paciente acima de 40°C.'
                temPcor = cor1           
            elif 39.1 <= temP_value <= 40:
                temp = 'Febre alta: Temperatura do paciente a partir de 39,1°C a 40°C.'
                temPcor = cor1  
            elif 38.1 <= temP_value <= 39:
                temp = 'Febre moderada: Temperatura do paciente a partir de 38,1°C a 39°C.'
                temPcor = cor2
            elif 37.6 <= temP_value <= 38:
                temp = 'Febre baixa: Temperatura do paciente a partir de 37,6°C a 38°C.'
                temPcor = cor3
            elif 36 <= temP_value <= 37.5:
                temp = 'Temperatura normal: Temperatura do paciente a partir de 36°C a 37,5°C.'
                temPcor = cor4
            elif 35 <= temP_value <= 35.9:
                temp = 'Hipotermia moderada: Temperatura do paciente a partir 35°C a 35,9°C.'
                temPcor = cor2
            elif temP_value <= 34.9:
                temp = 'Hipotermia grave: Temperatura do paciente abaixo de 35°C.'
                temPcor = cor1            
            else:
                temp = 'Hipertermia grave: acima de 40°C.'
                temPcor = cor1           
            
            return temp, temPcor
        temp, temPcor = verifica_temp()

        def sugestao():
            texto = 'De acordo a avaliação feita com base nos dados informados\
                    no pré-atendimento, com destaque apenas para a Pressão Arterial, Frequência Cardíaca\
                        , Frequência Respiratória, Saturação de Oxigênio, Hipoglicoteste e Temperatura, apontamos atendimento '
            if pAcor == cor1 or fCor == cor1 or fRcor == cor1 or spOcor == cor1 or hgTcor == cor1 or temPcor == cor1:
                sugest = f'{texto} (Vermelho) Emergência Imediata para esse paciente.'
                segeScor = cor1
            elif pAcor == cor2 or fCor == cor2 or fRcor == cor2 or spOcor == cor2 or hgTcor == cor2 or temPcor == cor2:
                sugest = f'{texto} (Laranja) Muita Urgência para esse paciente.'
                segeScor = cor2
            elif pAcor == cor3 or fCor == cor3 or fRcor == cor3 or spOcor == cor3 or hgTcor == cor3 or temPcor == cor3:
                sugest = f'{texto} (Amarelo) Urgência para esse paciente.'
                segeScor = cor3
            else:
                sugest = f'{texto} (Verde) Pouca Urgência para esse paciente.'
                segeScor = cor4
            return sugest, segeScor 
        sugest, segeScor = sugestao()


        # contexto      
        context['sistem_sugestao'] = sugest
        context['sistem_sugestao_cor'] = segeScor
        context['info_extra'] = 'Analisando...'
        context['tipo_select'] = 'Defina a classificação de Risco do Paciente'        
        context ['nome_paciente'] = self.object.paciente_triagem.paciente_envio_triagem.nome_social 

        # Pressão Arterial
        context['pAcor'] = pAcor
        context['pa_enviado'] = self.object.pressao_arterial_PA
        context['pressao_arterial_PA'] = pa

        # Frequencia Cardiaca
        context['fCor'] = fCor
        context['fc_enviado'] = self.object.frequencia_cardiaca_FC
        context['frequencia_cardiaca_FC'] = fc

        # Frequencia Respiratória
        context['fRcor'] = fRcor
        context['fr_enviado'] = self.object.frequencia_respiratoria_FR
        context['frequencia_respiratoria_FR'] = fr

        # Saturação de Oxigênio
        context['spOcor'] = spOcor
        context['spo_enviado'] = self.object.saturacao_de_oxigenio_SPO2
        context['saturacao_de_oxigenio_SPO2'] = spo

        # Hipoglicoteste
        context['hgTcor'] = hgTcor
        context['hgt_enviado'] = self.object.hemoglicoteste_HGT
        context['hemoglicoteste_HGT'] = hgt

        # Peso
        context['pesOcor'] = pesOcor
        context['peso_enviado'] = self.object.peso
        context['peso'] = peso
        context['altura_info'] = altura_info
        context['pesO_value'] = pesO_value

        # Temperatura
        context['temPcor'] = temPcor
        context['temp_enviado'] = self.object.temperatura_TEMP
        context['temp'] = temp

        context['data_triagem'] = self.object.data_triagem
        context['hora_triagem'] = self.object.hora_triagem 

        context['triagem_andamento'] = "ok" 
        context['classifica'] = "ok" 

        

        return context

    def get_success_url(self) -> str:
        id = self.object.paciente_triagem.id
        if id != None:        
            #return reverse('Triagem:triagem_concluida', kwargs={'pk': id})triagem_Etiqueta
            return reverse('Triagem:triagem_Etiqueta', kwargs={'pk': id})
        return super().get_success_url()   
        