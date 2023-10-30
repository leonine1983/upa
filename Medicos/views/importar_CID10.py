import csv
from Atendimento.models import *
import chardet
from Medicos.models import cid_10
from django.shortcuts import render

# -----------------Controle de doenças CID 10 ---------------------------
def import_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        print(request.POST)  # Adicionando este print
        # Detecta o encoding do arquivo
        encoding = chardet.detect(csv_file.read())['encoding']
        csv_file.seek(0)
        decoded_file = csv_file.read().decode(encoding).splitlines()
        reader = csv.DictReader(decoded_file, delimiter=';')
        print(reader.fieldnames)
        
        inserts = []
        for row in reader:
            codigo = row['Codigo']
            if not cid_10.objects.filter(codigo=codigo).exists():
                obj = cid_10.objects.create(
                    codigo=codigo,
                    descricao=row['Descricao'],
                    codigo_Cid10=row['Codigos_da_CID_10']
                )
                inserts.append(str(obj))

        print(f"Linhas salvas: {len(inserts)}")
        return render(request, 'Medicos/import_csv.html', {'success': True})
    
    return render(request, 'Medicos/import_csv.html')
