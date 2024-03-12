from django.urls import path, re_path

from . import views

app_name = 'Medicos'

urlpatterns = [
    path('', views.medico_protuario_view_, name='medico_prontuario'),
    #path('', views.medico_prontuario_view.as_view(), name='medico_prontuario'),
    path('atendimento/<int:pk>', views.medico_atendimento_view, name='medico_atendimento'), 
    # Chama Paciente
    path('iniciar-atendimento/<int:pk>/', views.iniciar_atendimento_view, name='iniciar_atendimento'),
    path('medico_chama_paciente/<int:pk>/', views.MedicoChamaPacienteView.as_view(), name='medico_chama_paciente'),
    path('enfermeira_chama_paciente/<int:pk>/', views.EnfermeiroChamaPacienteView.as_view(), name='enfermagem_chama_paciente'),
    path('medico_avisa_atendimentoo/<int:pk>/', views.chamar_pacientee.update_chama_paciente.Update_chama_usuarioo, name='medico_avisa_pacientee'),
    path('enfermagem_avisa_atendimentoo/<int:pk>/', views.Update_chama_usuario_triagem, name='enfermagem_avisa_pacientee'),
    path('medico_avisa_atendimentoo/<int:pk>/', views.Update_chama_usuario_pos_atendimento, name='medico_avisa_paciente_pos_atendimento'),

    #perfil completo do paciente / historico
    path('medico/lista_historico_paciente/', views.paciente_lista_historico.as_view(), name='lista_paciente_medico'),  
    path('medico/historico_paciente/<int:pk>', views.paciente_perfil_completo, name='perfil_completo_paciente'),  
    path('medico/historico_paciente_historico/<int:pk>', views.paciente_perfil_completo_segunda_parte, name='perfil_completo_segunda_parte'),  
    path('medico/historico_paciente/historico/<int:pk>', views.paciente_perfil_completo_menu_lateral, name='perfil_completo_paciente_menu_lateral'),
    
    path('atendimento/paciente/<int:pk>', views.atendimento_medico_createView.as_view(), name='dados do paciente'),
    path('atendimento/paciente/update/<int:pk>', views.atendimento_medico_Atualiza.as_view(), name='dados_do_paciente_atualiza'),
    path('atendimento/paciente/medicamento/<int:pk>', views.atendimento_medico_updateview.as_view(), name='dados_do_paciente_medicamentos'),
    path('atendimento_medico_concluido/<int:pk>', views.atendimento_medico_concluido_update.as_view(), name='final_medico_concluida'),
    path('atendimento_medico_concluido/exibe/<int:pk>', views.exibe_prescreve_medicamento_update.as_view(), name='exibe_prescreve_medicamento'),
    # PDFs ------------------------------------------------------------------
    path('atendimento_medico_concluido/exibe/geraPDF/<int:pk>', views.gerarPdf, name='geraPdf'),
    # Cria, atualiza e apaga ----------------------------------------------------------------------
    path('medico_signup/', views.medico_signup, name='medico_signup'),
    path('medico_signup/atulizando/<int:pk>', views.MedicoUpdateView.as_view(), name='medico_signup_atualiza'),
    path('medico_signup/atulizando/extras/<int:pk>', views.MedicoUpdateView_extra.as_view(), name='medico_signup_atualiza_extras'),
    path('medico_signup/delete/<int:pk>', views.MedicoDeleteView.as_view(), name='medico_delete'),
    # Salas
    path('medicos/cadastroSalas/', views.Cadastra_Sala_view.as_view(), name='cadastroSala' ),
    path('medicos/Salas/', views.Lista_Salas_ListView.as_view(), name='salas' ),    
    path('medicos/Salas/atualizacao/<int:pk>', views.Atualiza_Sala_UpdatView.as_view(), name='salasUpdate' ),
    path('medicos/Salas/delete/<int:pk>', views.Delete_Sala_Delet.as_view(), name='salasDelete' ),
    # Exames
    path('medicos/cadastroExames/', views.Cadastra_Exame_view.as_view(), name='cadastroExame' ),    
    path('medicos/cadastroExames/atualizacao/<int:pk>', views.Atualiza_Exame_UpdatView.as_view(), name='exameUpdate' ),
    path('medicos/Salas/', views.Lista_Salas_ListView.as_view(), name='salas' ),    
    path('medicos/Exames/delete/<int:pk>', views.Delete_Exame_Delet.as_view(), name='exameDelete' ),

    # Medicamentos
    path('medicos/cdastraMedicamento/', views.Cadastra_Medicamento.as_view(), name='cadastroMedicamento' ),    
    path('medicos/cadastroExames/atualizacao/<int:pk>', views.Atualiza_Exame_UpdatView.as_view(), name='exameUpdate' ),
    path('medicos/Salas/', views.Lista_Salas_ListView.as_view(), name='salas' ),    
    path('medicos/Exames/delete/<int:pk>', views.Delete_Exame_Delet.as_view(), name='exameDelete' ),
    # vincula Profissional
    path('medicos/Salas/profissional/', views.VinculaProfissiona_sala_view.as_view(), name='salasProfissionalCreate' ),
    path('medicos/Salas/profissional/update/<int:pk>', views.VinculaProfissiona_sala_update.as_view(), name='salasProfissionalUpdate' ),
    path('medicos/Salas/profissional/delete/<int:pk>', views.DeleteProfissionaSala_Delet.as_view(), name='salasProfissionalDelete' ),
  
    path('cadastrar-chamada/', views.cadastrar_chamada, name='cadastrar_chamada'),
    # importar csv para cid 10
    path('importar_csv/', views.import_csv, name='importa_csv'),
    

]


