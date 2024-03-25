#Para criar outros campos para o usuario
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, User)
from django.db import models
from Atendimento.models import *
from Triagem.models import triagem
from django.db.models import Q
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import Group, User, Permission
from ckeditor.fields import RichTextField
from Triagem.models import Exames_Model


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser definido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    crm = models.CharField(max_length=13, null=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_user_permissions')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='custom_user')
    grupo = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='custom_users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomUserManager()

    #caso não exista registros de grupos em Groups
    #criar os grupos group_Admin, group_Medicos, group_Enfermagem, group_Tec_Enfermagem
    @receiver(post_migrate)
    def create_grupos_model(sender, **kwargs):
        # Irá pecorrer a lista e adicionar o conteudo dessa lista no model Groups
        groups_name = ['group_UPA-Admin', 'group_Medicos', 'group_Enfermagem', 'group_Tec_Enfermagem']
        if not Group.objects.exists():
            for g_name in groups_name:
                Group.objects.create(
                    name = g_name
                ) 

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.endereco


# -----------------Controle de doenças CID 10 ---------------------------
class cid_10 (models.Model):
    codigo = models.CharField(max_length=12, null=True)
    descricao = models.TextField(max_length=300, null=True)
    codigo_Cid10 = models.CharField(max_length=50)

    class Meta:
        ordering= ['id']
    def __str__(self):
        return f'{self.codigo_Cid10} - {self.descricao}'

    @receiver(post_migrate)
    def envia_cid(sender, **kwargs):
        sequencia = "0;001-057;1;2;3;4;5;6;7;007.1;007.2;8;008.1;008.2;008.3;008.4;008.5;008.9;9;10;11;12;13;14;15;16;17;18;018.1;018.2;018.3;018.9;19;20;21;22;23;24;25;26;27;28;29;30;31;32;032.1;032.2;032.9;33;34;35;36;37;38;39;4B8r3B4p7yhRXuBWLqsQ546WR43cqQwrbXMDFnBi6vSJBeif8tPW85a7r7DM961Jvk4hdryZoByEp8GC8HzsqJpRN4FxGM9;50;51;52;53;54;55;56;57;058-096;58;59;60;61;62;63;64;65;66;67;68;69;70;71;72;73;74;75;76;77;78;79;4B8r3B4p7yhRXuBWLqsQ546WR43cqQwrbXMDFnBi6vSJBeif8tPW85a7r7DM961Jvk4hdryZoByEp8GC8HzsqJpRN4FxGM9105;106;107;108;109;110;111;112-119;112;113;114;115;116;117;118;119;120-129;120;120.1;120.2;120.3;120.4;120.9;121;122;123;124;125;126;127;128;129;130-139;130;131;132;133;134;135;136;137;138;139;140-142;140;141;142;143-164;143;144;145;146;147;148;149;150;151;152;153;154;155;156;157;158;159;160;161;162;163;164;165-179;165;166;167;168;169;170;171;172;173;174;175;176;177;178;179;180-197;180;181;182;183;184;185;186;187;188;189;190;191;192;193;194;195;196;197;198-199;198;199;200-210;200;201;202;203;204;205;206;207;208;209;210;211-233;211;212;213;214;215;216;217;218;219;220;221;222;223;224;225;226;227;228;229;230;231;232;233;234-244;234;235;236;237;238;239;240;241;242;243;244;245-253;245;246;247;248;249;250;251;252;253;254-266;254;255;256;257;258;259;260;261;262;263;264;265;266;267-270;267;268;269;270;271-289;271;272;273;274;275;276;277;278;279;280;281;282;283;284;285;286;287;288;289;1.096-1.103;1.096;1.097;1.098;1.099;1.100;1.101;1.102;1.103;290-298;290;291;292;293;294;295;296;297;298;900-999;901;-;-;-;-;"
        sequencia2 = "Nenhuma doença encontrada;Algumas doenças infecciosas e parasitárias;Cólera;Febres tifóide e paratifóide;Shiguelose;Amebíase;Diarréia e gastroenterite de origem infecciosa presumível;Outras doenças infecciosas intestinais;Tuberculose respiratória;Tuberculose pulmonar;Outras tuberculoses respiratórias;Outras tuberculoses;Tuberculose do sistema nervoso;Tuberculose do intestino, do peritônio e dos gânglios mesentéricos;Tuberculose óssea e das articulações;Tuberculose do aparelho geniturinário;Tuberculose miliar;Restante de outras tuberculoses;Peste;Brucelose;Hanseníase [lepra];Tétano neonatal;Outros tétanos;Difteria;Coqueluche;Infecção meningocócica;Septicemia;Outras doenças bacterianas;Leptospirose icterohemorrágica;Outras formas de leptospirose;Leptospirose não especificada;Restante de outras doenças bacterianas;Sífilis congênita;Sífilis precoce;Outras sífilis;Infecção gonocócica;Doenças por clamídias transmitidas por via sexual;Outras infecções com transmissão predominantemente sexual;Febres recorrentes;Tracoma;Tifo exantemático;Poliomielite aguda;Raiva;Encefalite viral;Febre amarela;Outras febre por arbovírus e febres hemorrágicas por vírus;Dengue [dengue clássico];Febre hemorrágica devida ao vírus da dengue;Restante de outras febre por arbovírus e febres hemorrágicas por vírus;Infecções pelo vírus do herpes;Varicela e herpes zoster;Sarampo;Rubéola;Hepatite aguda B;Outras hepatites virais;Doença pelo vírus da imunodeficiência humana [HIV];Caxumba [parotidite epidêmica];Outras doenças virais;Meningite viral;Restante de outras doenças virais;Micoses;Malária;Malária por Plasmodium falciparum;Malária por Plasmodium vivax;Malária por Plasmodium malariae;Outras formas de malária confirmadas por exames parasitológicos;Malária não especificada;Leishmaniose;Leishmaniose visceral;Leishmaniose cutânea;Leishmaniose cutâneo-mucosa;Leishmaniose não especificada;Tripanossomíase;Esquistossomose;Outras infestações por trematódeos;Equinococose;Dracunculíase;Oncocercose;Filariose;Ancilostomíase;Outras helmintíases;Seqüelas de tuberculose;Seqüelas de poliomielite;Seqüelas de hanseníase [lepra];Outras doenças infecciosas e parasitárias;Neoplasias [tumores];Neoplasia maligna do lábio, cavidade oral e faringe;Neoplasia maligna do esôfago;Neoplasia maligna do estômago;Neoplasia maligna do cólon;Neoplasia maligna da junção retossigmóide, reto, ânus e canal anal;Neoplasia maligna do fígado e das vias biliares intra-hepáticas;Neoplasia maligna do pâncreas;Outras neoplasias malignas de órgãos digestivos;Neoplasias malignas de laringe;Neoplasia maligna da traquéia, dos brônquios e dos pulmões;Outras neoplasias malignas de órgãos respiratórios e intratorácicos;Neoplasia maligna do osso e da cartilagem articular;Neoplasia maligna da pele;Outras neoplasias malignas da pele;Neoplasias malignas do tecido mesotelial e tecidos moles;Neoplasia maligna da mama;Neoplasia maligna do colo do útero;Neoplasia maligna de outras porções e de porções não especificadas do útero;Outras neoplasias malignas dos órgãos genitais femininos;Neoplasia maligna da próstata;Outras neoplasias malignas dos órgãos genitais masculinos;Neoplasia maligna da bexiga;Outras neoplasias malignas do trato urinário;Neoplasia maligna dos olhos e anexos;Neoplasia maligna do encéfalo;Neoplasia maligna de outras partes do sistema nervoso central;Neoplasias malignas de outras localizações, de localização mal definida, secundárias e de localização não especificada;Doença de Hodgkin;Linfoma não-Hodgkin;Leucemia;Outras neoplasias malignas de tecidos linfóide, hematopoético e relacionados;Carcinoma in situ de colo do útero;Neoplasia benigna da pele;Neoplasia benigna da mama;Leiomioma do útero;Neoplasia benigna do ovário;Neoplasia benigna dos órgãos urinários;Neoplasia benigna do encéfalo e de outras partes do sistema nervoso central;Outras neoplasias in situ e neoplasias benignas e neoplasias de comportamento incerto ou desconhecido;Doenças do sangue e dos órgãos hematopoéticos e alguns transtornos imunitários;Anemia por deficiência de ferro;Outras anemias;Afecções hemorrágicas e outras doenças do sangue e dos órgãos hematopoéticos;Alguns transtornos envolvendo o mecanismo imunitário;Doenças endócrinas, nutricionais e metabólicas;Transtornos tireoidianos relacionados à deficiência de iodo;Tireotoxicose;Outros transtornos tireoidianos;Diabetes mellitus;Desnutrição;Deficiência de vitamina A;Outras deficiências vitamínicas;Seqüelas de desnutrição e de outras deficiências nutricionais;Obesidade;Depleção de volume;Outros transtornos endócrinos, nutricionais e metabólicos;Transtornos mentais e comportamentais;Demência;Transtornos mentais e comportamentais devidos ao uso de álcool;Transtornos mentais e comportamentais devidos ao uso de outras substâncias psicoativas;Esquizofrenia, transtornos esquizotípicos e delirantes;Transtornos de humor [afetivos];Transtornos neuróticos, transtornos relacionados com o stress e transtornos somatoformes;Retardo mental;Outros transtornos mentais e comportamentais;Doenças do sistema nervoso;Doenças inflamatórias do sistema nervoso central;Meningite bacteriana, não classificada em outra parte;Meningite em doenças bacterianas classificadas em outra parte;Meningite em outras doenças infecciosas e parasitárias classificadas em outra parte;Meningite devida a outras causas e a causas não especificadas;Restante de doenças inflamatórias do sistema nervoso central;Doença de Parkinson;Doença de Alzheimer;Esclerose múltiplas;Epilepsia;Enxaqueca e outras síndromes de algias cefálicos;Acidentes vasculares cerebrais isquêmicos transitórios e síndromes correlatas;Transtornos dos nervos, das raízes e dos plexos nervosos;Paralisia cerebral e outras síndromes paralíticas;Outras doenças do sistema nervoso;Doenças do olho e anexos;Inflamação da pálpebra;Conjuntivite e outros transtornos da conjuntiva;Ceratite e outros transtornos da esclerótica e da córnea;Catarata e outros transtornos do cristalino;Descolamentos e defeitos da retina;Glaucoma;Estrabismo;Transtornos da refração e da acomodação;Cegueira e visão subnormal;Outras doenças do olho e anexos;Doenças do ouvido e da apófise mastóide;Otite média e outros transtornos do ouvido médio e da apófise mastóide;Perda de audição;Outras doenças do ouvido e da apófise mastóide;Doenças do aparelho circulatório;Febre reumática aguda;Doença reumática crônica do coração;Hipertensão essencial (primária);Outras doenças hipertensivas;Infarto agudo do miocárdio;Outras doenças isquêmicas do coração;Embolia pulmonar;Transtornos de condução e arritmias cardíacas;Insuficiência cardíaca;Outras doenças do coração;Hemorragia intracraniana;Infarto cerebral;Acidente vascular cerebral, não especificado como hemorrágico ou isquêmico;Outras doenças cerebrovasculares;Ateroesclerose;Outras doenças vasculares periféricas;Embolia e trombose arteriais;Outras doenças das artérias, arteríolas e capilares;Flebite, tromboflebite, embolia e trombose venosa;Veias varicosas das extremidades inferiores;Hemorróidas;Outras doenças do aparelho circulatório;Doenças do aparelho respiratório;Faringite aguda e amigdalite aguda;Laringite e traqueíte agudas;Outras infecções agudas das vias aéreas superiores;Influenza [gripe];Pneumonia;Bronquite aguda e bronquiolite aguda;Sinusite crônica;Outras doenças do nariz e dos seios paranasais;Doenças crônicas das amígdalas e das adenóides;Outras doenças do trato respiratório superior;Bronquite, enfisema e outras doenças pulmonares obstrutivas crônicas;Asma;Bronquiectasia;Pneumoconiose;Outras doenças do aparelho respiratório;Doenças do aparelho digestivo;Cárie dentária;Outros transtornos dos dentes e estruturas de suporte;Outras doenças da cavidade oral, glândulas salivares e dos maxilares;Úlcera gástrica e duodenal;Gastrite e duodenite;Outras doenças do esôfago, estômago e duodeno;Doenças do apêndice;Hérnia inguinal;Outras hérnias;Doença de Crohn e colite ulcerativa;Íleo paralítico e obstrução intestinal sem hérnia;Doença diverticular do intestino;Outras doenças dos intestinos e peritônio;Doença alcoólica do fígado;Outras doenças do fígado;Colelitíase e colecistite;Pancreatite aguda e outras doenças do pâncreas;Outras doenças do aparelho digestivo;Doenças da pele e do tecido subcutâneo;Infecções da pele e do tecido subcutâneo;Outras doenças da pele e do tecido subcutâneo;Doenças do sistema osteomuscular e do tecido conjuntivo;Artrite reumatóide e outras poliartropatias inflamatórias;Artrose;Deformidades adquiridas das articulações;Outros transtronos articulares;Doenças sistêmicas do tecido conjuntivo;Transtornos discais cervicais e outros transtornos discais intervertebrais;Outras dorsopatias;Transtornos do tecido mole;Transtornos da densidade e da estrutura ósseas;Osteomielite;Outras doenças do sistema osteomuscular e do tecido conjuntivo;Doenças do aparelho geniturinário;Síndrome nefríticas aguda e rapidamente progressiva;Outras doenças glomerulares;Doenças renais túbulo-intersticiais;Insuficiência renal;Urolitíase;Cistite;Outras doenças do aparelho urinário;Hiperplasia da próstata;Outros transtornos da próstata;Hidrocele e espermatocele;Preprúcio redundante, fimose e parafimose;Outras doenças dos órgãos genitais masculinos;Transtornos da mama;Salpingite e ooforite;Doença inflamatória do colo do útero;Outras doenças inflamatórias dos órgãos pélvicos femininos;Endometriose;Prolapso genital feminino;Transtornos não-inflamatórios do ovário, da trompa de Falópio e do ligamento largo;Transtornos da menstruação;Transtornos menopáusicos e outros transtornos perimenopáusicos;Infertilidade feminina;Outros transtornos do aparelho geniturinário;Gravidez, parto e puerpério;Aborto espontâneo;Aborto por razões médicas;Outras gravidezes que terminam em aborto;Edema, proteinúria e transtornos hipertensivos na gravidez, parto e puerpério;Placenta prévia, descolamento prematuro de placenta e hemorragia anteparto;Outros motivos de assistência à mãe relacionados à cavidade fetal e amniótica, e possíveis problemas de parto;Trabalho de parto obstruído;Hemorragia pós-parto;Outras complicações da gravidez e do parto;Parto único espontâneo;Complicações predominantemente relacionadas ao puerpério e outras afecções obstétricas, não classificadas em outra parte;Algumas afecções originadas no período perinatal;Feto e recém-nascido afetados por fatores maternos e por complicações da gravidez, trabalho de parto e parto;Retardo de crescimento fetal, desnutrição fetal e transtornos relacionados à gestação curta e baixo peso ao nascer;Trauma durante o nascimento;Hipóxia intrauterina e asfixia ao nascer;Outros transtornos respiratórios originados no período perinatal;Doenças infecciosas e parasitárias congênitas;Outras infecções específicas do período perinatal;Doença hemolítica do feto e do recém-nascido;Outras afecções originadas no período perinatal;Malformações congênitas, deformidades e anomalias cromossômicas;Espinha bífida;Outras malformações congênitas do sistema nervoso;Malformações congênitas do aparelho circulatório;Fenda labial e fenda palatina;Ausência, atresia e estenose do intestino delgado;Outras malformações congênitas do aparelho digestivo;Testiculo não-descido;Outras malformações do aparelho geniturinário;Deformidades congênitas do quadril;Deformidades congênitas dos pés;Outras malformações e deformidades congênitas do aparelho osteomuscular;Outras malformações congênitas;Anomalias cromossômicas, não classificadas em outra parte;Sintomas, sinais e achados anormais de exames clínicos e de laboratório, não classificados em outra parte;Dor abdominal e pélvica;Febre de origem desconhecida;Senilidade;Outros sintomas, sinais e achados anormais de exames clínicos e de laboratório, não classificados em outra parte;Lesões, envenenamentos e algumas outras conseqüências de causas externas;Fratura do crânio e dos ossos da face;Fratura do pescoço, tórax ou pelve;Fratura do fêmur;Fratura de outros ossos dos membros;Fraturas envolvendo múltiplas regiões do corpo;Luxações, entorse e distensão de regiões especificadas e de regiões múltiplas do corpo;Traumatismo do olho e da órbita ocular;Traumatismo intracraniano;Traumatismo de outros órgãos internos;Lesões por esmagamento e amputações traumáticas de regiões especificadas e de múltiplas regiões do corpo;Outros traumatismos de regiões especificadas e não especificadas e de regiões múltiplas do corpo;Efeitos de corpo estranho que entra através de orifício natural;Queimadura e corrosões;Envenenamento por drogas e substâncias biológicas;Efeitos tóxicos de substâncias de origem principalmente não-medicinal;Síndromes de maus tratos;Outros efeitos e os efeitos não especificados de causas externas;Certas complicações precoces de traumatismo e complicações cirúrgicas, e da assistência médica não classificadas em outra parte;Seqüelas de traumatismos, de envenenamento e de outras conseqüências de causas externas;Causas externas de morbidade e de mortalidade;Acidentes de transporte;Quedas;Afogamento e submersão acidentais;Exposição ao fumo, ao fogo e às chamas;Envenenamento, intoxicação por ou exposição a substâncias nocivas;Lesões autoprovocadas voluntariamente;Agressões;Todas as outras causas externas;Fatores que exercem influência sobre o estado de saúde e o contato com serviços de saúde;Pessoas em contato com os serviços de saúde para exame e investigação;Estado de infecção assintomática pelo vírus da imunodeficiência humana [HIV];Outras pessoas com riscos potenciais à saúde relacionadas com doenças transmissíveis;Anticoncepção; Rastreamento (screening) pré-natal e outras supervisões da gravidez;Nascidos vivos segundo o local de nascimento;Assistência e exame pós-natal;Pessoas em contato com serviços de saúde para cuidados e procedimentos específicos;Pessoas em contato com os serviços de saúde por outras razões;Códigos para propósitos especiais;Síndrome respiratória aguda grave (Severe acute respiratory syndrome) [SARS];CID 10ª Revisão não disponível;CID não preenchido ou inválido;Não preenchido;CID inválido;"
        sequencia3 = "0;A00-B99;A00;A01;A03;A06;A09;A02, A04-A05, A07-A08;A15-A16;A15.0-A15.3, A16.0-A16.3;A15.4-A15.9, A16.4-A16.9;A17-A19;A17;A18.3;A18.0;A18.1;A19;A18.2, A18.4-A18.8;A20;A23;A30;A33;A34-A35;A36;A37;A39;A40-A41;A21-A22, A24-A28, A31-A32, A38, A42-A49;A27.0;A27.8;A27.9;A21-A22, A24-A26, A28, A31-A32, A38, A42-A49;A50;A51;A52-A53;A54;A55-A56;A57-A64;A68;A71;A75;A80;A82;A83-A86;A95;A90-A94, A96-A99;A90;A91;A92-A94, A96-A99;B00;B01-B02;B05;B06;B16;B15, B17-B19;B20-B24;B26;A81, A87-A89, B03-B04, B07-B09, B25, B27-B34;A87;A81, A88-A89, B03-B04, B07-B09, B25, B27-B34;B35-B49;B50-B54;B50;B51;B52;B53;B54;B55;B55.0;B55.1;B55.2;B55.9;B56-B57;B65;B66;B67;B72;B73;B74;B76;B68-B71, B75, B77-B83;B90;B91;B92;A65-A67, A69-A70, A74, A77-A79, B58-B64, B85-B89, B94-B99;C00-D48;C00-C14;C15;C16;C18;C19-C21;C22;C25;C17, C23-C24, C26;C32;C33-C34;C30-C31, C37-C39;C40-C41;C43;C44;C45-C49;C50;C53;C54-C55;C51-C52, C56-C58;C61;C60, C62-C63;C67;C64-C66, C68;C69;C71;C70, C72;C73-C80, C97;C81;C82-C85;C91-C95;C88-C90, C96;D06;D22-D23;D24;D25;D27;D30;D33;D00-D05, D07-D21, D26, D28-D29, D31-D32, D34-D48;D50-D89;D50;D51-D64;D65-D77;D80-D89;E00-E90;E00-E02;E05;E03-E04, E06-E07;E10-E14;E40-E46;E50;E51-E56;E64;E66;E86;E15-E35, E58-E63, E65, E67-E85, E87-E90;F00-F99;F00-F03;F10;F11-F19;F20-F29;F30-F39;F40-F48;F70-F79;F04-F09, F50-F69, F80-F99;G00-G99;G00-G09;G00;G01;G02;G03;G04-G09;G20;G30;G35;G40-G41;G43-G44;G45;G50-G59;G80-G83;G10-G13, G21-G26, G31-G32, G36-G37, G46-G47, G60-G73, G90-G99;H00-H59;H00-H01;H10-H13;H15-H19;H25-H28;H33;H40-H42;H49-H50;H52;H54;H02-H06, H20-H22, H30-H32, H34-H36, H43-H48, H51, H53, H55-H59;H60-H95;H65-H75;H90-H91;H60-H62, H80-H83, H92-H95;I00-I99;I00-I02;I05-I09;I10;I11-I15;I21-I22;I20, I23-I25;I26;I44-I49;I50;I27-I43, I51-I52;I60-I62;I63;I64;I65-I69;I70;I73;I74;I71-I72, I77-I79;I80-I82;I83;I84;I85-I99;J00-J99;J02-J03;J04;J00-J01, J05-J06;J09-J11;J12-J18;J20-J21;J32;J30-J31, J33-J34;J35;J36-J39;J40-J44;J45-J46;J47;J60-J65;J22, J66-J99;K00-K93;K02;K00-K01, K03-K08;K09-K14;K25-K27;K29;K20-K23, K28, K30-K31;K35-K38;K40;K41-K46;K50-K51;K56;K57;K52-K55, K58-K67;K70;K71-K77;K80-K81;K85-K86;K82-K83, K87-K93;L00-L99;L00-L08;L10-L99;M00-M99;M05-M14;M15-M19;M20-M21;M00-M03, M22-M25;M30-M36;M50-M51;M40-M49, M53-M54;M60-M79;M80-M85;M86;M87-M99;N00-N99;N00-N01;N02-N08;N10-N16;N17-N19;N20-N23;N30;N25-N29, N31-N39;N40;N41-N42;N43;N47;N44-N46, N48-N51;N60-N64;N70;N72;N71, N73-N77;N80;N81;N83;N91-N92;N95;N97;N82, N84-N90, N93-N94, N96, N98-N99;O00-O99;O03;O04;O00-O02, O05-O08;O10-O16;O44-O46;O30-O43, O47-O48;O64-O66;O72;O20-O29, O60-O63, O67-O71, O73-O75, O81-O84;O80;O85-O99;P00-P96;P00-P04;P05-P07;P10-P15;P20-P21;P22-P28;P35-P37;P38-P39;P55;P08, P29, P50-P54, P56-P96;Q00-Q99;Q05;Q00-Q04, Q06-Q07;Q20-Q28;Q35-Q37;Q41;Q38-Q40, Q42-Q45;Q53;Q50-Q52, Q54-Q64;Q65;Q66;Q67-Q79;Q10-Q18, Q30-Q34, Q80-Q89;Q90-Q99;R00-R99;R10;R50;R54;R00-R09, R11-R49, R51-R53, R55-R99;S00-T98;S02;S12, S22, S32, T08;S72;S42, S52, S62, S82, S92, T10, T12;T02;S03, S13, S23, S33, S43, S53, S63, S73, S83, S93, T03;S05;S06;S26-S27, S36-S37;S07-S08, S17-S18, S28, S38, S47-S48, S57-S58, S67-S68, S77-S78, S87-S88, S97-S98, T04-T05;S00-S01, S04, S09-S11, S14-S16, S19-S21, S24-S25, S29-S31, S34-S35, S39-S41, S44-S46, S49-S51, S54-S56, S59-S61, S64-S66, S69-S71, S74-S76, S79-S81, S84-S86, S89-S91, S94-S96, S99, T00-T01, T06-T07, T09, T11, T13-T14;T15-T19;T20-T32;T36-T50;T51-T65;T74;T33-T35, T66-T73, T75-T78;T79-T88;T90-T98;V01-Y98;V01-V99;W00-W19;W65-W74;X00-X09;X40-X49;X60-X84;X85-Y09;W20-W64, W75-W99, X10-X39, X50-X59, Y10-Y89;Z00-Z99;Z00-Z13;Z21;Z20, Z22-Z29;Z30;Z34-Z36;Z38;Z39;Z40-Z54;Z31-Z33, Z37, Z55-Z99;U00-U99;U04;U99; - - -;em branco;Subcategoria da CID não existente"
        sequencia_split = sequencia.split(';')[:-1]
        lista = [num for num in sequencia_split]
        sequencia2_split = sequencia2.split(';')[:-1]
        lista2 = [num for num in sequencia2_split]
        sequencia3_split = sequencia3.split(';')[:-1]
        lista3 = [num for num in sequencia3_split]

        # Usarei a função ZIP para permitir a interação simultanea entre as tres listas
        if not cid_10.objects.exists():
            for seq, seq2, seq3 in zip(lista, lista2, lista3):
                cid_10.objects.create(
                    codigo = seq,
                    descricao = seq2,
                    codigo_Cid10 = seq3
                )    

    @staticmethod
    def consulta_personalizada(q):
        return cid_10.objects.filter(Q(codigo=q) | Q(descricao_icontains=q) | Q(codigo_Cid10 =q) )  


class Medicamento(models.Model):
    nome_medicamento = models.CharField(max_length=255)
    principio_ativo = models.CharField(max_length=255, null=True, blank=True)
    forma_farmaceutica = models.CharField(max_length=100, null=True, blank=True)
    concentracao = models.CharField(max_length=50, null=True, blank=True)
    via_administracao = models.CharField(max_length=50, null=True, blank=True)
    quantidade_disponivel = models.PositiveIntegerField()
    unidade_medida = models.CharField(max_length=20, null=True, blank=True)
    data_validade = models.DateField(null=True, blank=True)
    fabricante = models.CharField(max_length=255, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome_medicamento


class Medico_atendimento (models.Model):
    paciente_medico_atendimento = models.OneToOneField(triagem, null=False, on_delete=models.PROTECT)    
    historico_doenca_atual_HDA = RichTextField(null=True, blank=True)
    exame_fisico = RichTextField(null=True, blank=True)
    Diagnostico = RichTextField(null=True, blank=True)
    classificacao_internacional_doenca_CID = models.ForeignKey(cid_10, null=True, default='Não se aplica', on_delete=models.CASCADE)
    medicamento = models.ManyToManyField(Medicamento, blank=True)
    conduta = RichTextField(null=True, blank=True)
    data_medico = models.DateField(auto_now_add=True, null=False)
    hora_medico = models.TimeField(auto_now_add=True, null=True )
    tempo_espera_paciente = models.DurationField(blank=True, null=True)
    medico_nome = models.CharField(max_length=40, null=True)
    
    # Cotabilização de chamadas -------------------------------------
    respondeu_ao_chamado = models.BooleanField(default=True, null=True)
    chamadas_contabilizadas = models.IntegerField(default=0, null=True)
    # Fim Cotabilização de chamadas -------------------------------------
    
    class Meta:
        permissions = [('Acesso_permitido_Admin', 'Acesso permitido ao admin do sistema na UPA'),\
                       ('Acesso_permitido_medic', 'Acesso permitido aos médicos') ]
        
    def __str__(self) -> str:
        return self.paciente_medico_atendimento.paciente_triagem.paciente_envio_triagem.nome_social
    
    @receiver(post_migrate)
    def add_example_medicamento(sender, **kwargs):
        if not Medicamento.objects.exists():
            Medicamento.objects.create(
                nome_medicamento='Exemplo Medicamento',
                principio_ativo='Ativo Exemplo',
                forma_farmaceutica='Comprimido',
                concentracao='10mg',
                via_administracao='Oral',
                quantidade_disponivel=50,
                unidade_medida='Comprimidos',
                data_validade='2023-12-31',
                fabricante='Fabricante Exemplo',
                observacoes='Este é um exemplo de medicamento.'
            )


class Chamar_P_para_atendimento(models.Model):
    # Define o modelo "Chamar_P_para_atendimento" com três campos: "nome_paciente", "profissionalSaude" e "data_chamada"
    nome_paciente = models.ForeignKey(triagem, null=True, on_delete=models.CASCADE)
    profissionalSaude_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    data_chamada = models.DateTimeField(auto_now=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(default=timezone.now)
    chamado = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(Chamar_P_para_atendimento, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.request and self.request.user:
            # Define a data e hora de criação do registro
            self.data_criacao = timezone.now()
            self.profissionalSaude_id = self.request.user

            # Exclui os últimos 5 registros criados pelo usuário
            Chamar_P_para_atendimento.objects.all().delete()            

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return str(self.nome_paciente.paciente_triagem.paciente_envio_triagem.nome_social)


class CadastroSala(models.Model):
    nome_Sala = models.CharField(max_length=40, null=False, default='Ex: Sala de pediatria')
    descricao_Sala = models.TextField(max_length=200, null=False, default='Ex.: Sala de atendimento pediátrico')
    
    @receiver(post_migrate)
    def create_register(sender, **kwargs):
        salas_e_descricoes = [
                                ("Sala de Emergência", "Utilizada para atendimento médico de emergência."),
                                ("Sala de Cirurgia", "Destinada a procedimentos cirúrgicos."),
                                ("Sala de Recuperação Pós-cirúrgica", "Espaço para a recuperação de pacientes após cirurgias."),
                                ("Sala de Consulta", "Usada para consultas médicas regulares."),
                                ("Sala de Exames de Diagnóstico", "Destinada à realização de exames para diagnóstico médico."),
                                ("Sala de Tratamento Intensivo (UTI)", "Para tratamento intensivo de pacientes críticos."),
                                ("Sala de Parto", "Utilizada para procedimentos de parto."),
                                ("Sala de Maternidade", "Destinada ao cuidado de mães e recém-nascidos."),
                                ("Sala de Pediatria", "Especializada no tratamento de crianças."),
                                ("Sala de Radiologia", "Para realização de exames de imagem."),
                                ("Sala de Ultrassonografia", "Especializada em exames de ultrassom."),
                                ("Sala de Endoscopia", "Utilizada para procedimentos endoscópicos."),
                                ("Sala de Quimioterapia", "Para administração de tratamentos quimioterápicos."),
                                ("Sala de Hemodiálise", "Destinada a pacientes que necessitam de diálise renal."),
                                ("Sala de Triagem", "Utilizada para triagem e classificação de pacientes."),
                                ("Sala de Observação", "Espaço para observação de pacientes."),
                                ("Sala de Isolamento", "Para pacientes com doenças contagiosas."),
                                ("Sala de Fisioterapia", "Especializada em tratamentos de fisioterapia."),
                                ("Sala de Psicologia Clínica", "Destinada a consultas e tratamentos psicológicos."),
                                ("Sala de Nutrição Clínica", "Para consultas e orientações nutricionais."),
                                ("Sala de Reabilitação", "Espaço para programas de reabilitação médica."),
                                ("Sala de Farmácia Hospitalar", "Destinada ao armazenamento e dispensação de medicamentos."),
                                ("Sala de Esterilização", "Para esterilização de instrumentos médicos."),
                                ("Sala de Anestesia", "Utilizada para administração de anestesia antes de procedimentos."),
                                ("Sala de Autópsia", "Espaço para realização de autópsias."),
                                ("Sala de Treinamento Médico", "Utilizada para treinamento e ensino médico."),
                                ("Sala de Conferências", "Para realização de conferências e eventos médicos."),
                                ("Sala de Arquivo Médico", "Destinada ao armazenamento de registros médicos."),
                                ("Sala de Espera", "Espaço para pacientes aguardarem atendimento."),
                                ("Sala de Administração Hospitalar", "Utilizada para atividades administrativas do hospital."),
                                ("Sala de Informática Médica", "Especializada em atividades de informática médica."),
                                ("Sala de Manutenção", "Para atividades de manutenção predial e de equipamentos."),
                                ("Sala de Lavanderia Hospitalar", "Para lavagem e processamento de roupas hospitalares."),
                                ("Sala de Almoxarifado", "Utilizada para armazenamento de suprimentos e materiais."),
                                ("Sala de Coleta de Sangue", "Para coleta de amostras de sangue."),
                                ("Sala de Vacinação", "Destinada à administração de vacinas."),
                                ("Sala de Controle de Infecção Hospitalar", "Especializada no controle de infecções hospitalares."),
                            ]
        if not CadastroSala.objects.exists():
            CadastroSala.objects.bulk_create(
                [CadastroSala(nome_Sala = sala, descricao_Sala = descricao ) for sala, descricao in salas_e_descricoes]
            )              

    def __str__(self):
        return self.nome_Sala


class Salas_Atendimento(models.Model):
    nomeSala = models.ForeignKey(CadastroSala, on_delete=models.CASCADE)
    profissionalSaude = models.ForeignKey(User, limit_choices_to={'groups__name__in':['group_Medicos', 'group_Enfermagem']}, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nomeSala.nome_Sala )


class Salva_modelo_exame(models.Model):
    
    nome = models.CharField(max_length=40, null=False, default='Ex: Nome do modelo')
    exame = models.ManyToManyField(Exames_Model)
    conteudo = models.TextField(max_length=500, null=False, default='Ex: Solicito os seguintes exames ...')

    def __init__(self):
        return self.nome
    


    






   


    

