from django.shortcuts import render
from core.models import FeriadoModel
from datetime import date
from .forms import FeriadoForm
def feriado(request):
    hoje = date.today()
    qs = FeriadoModel.objects.filter(mes=hoje.month)
    qs = qs.filter(dia=hoje.day)
    if len(qs) == 1:
        nome_feriado = qs[0].nome
        contexto = {'title':"Meu Feriado", 'feriado':True,
                'nome_feriado':nome_feriado}
    else: 
        contexto = {'title':"Meu Feriado", 'feriado':False}
    return render(request, 'feriado.html', contexto)

def cadastro(request):
    if request.method == 'POST':
        form_feriado = FeriadoForm(request.POST)
        if form_feriado.is_valid():
            feriado = FeriadoModel.objects.create(**form_feriado.cleaned_data)
            # Retorne uma resposta HTTP para o envio bem-sucedido do formulário
            return redirect('success_url')  # Substitua 'success_url' pelo URL desejado

    # Código para lidar com solicitações GET (opcional)
    else:
        form_feriado = FeriadoForm()

    contexto = {'form_feriado': FeriadoForm()}  # Supondo que 'contexto' seja um dicionário para o contexto do template
    return render(request, "cadastro.html", contexto)
