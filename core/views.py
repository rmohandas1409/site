from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages

from .models import Topo, Portifolio, Galeria_Portifolio, Parceiro, Promocoes, Galeria_Promocoes, Servico, Dicas, Footer


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['topos'] = Topo.objects.order_by('?').all()
        context['portifolio'] = Portifolio.objects.order_by('?').all()
        context['galeria_portifolio'] = Galeria_Portifolio.objects.order_by('?').all()
        context['parceiros'] = Parceiro.objects.order_by('?').all()
        context['promocoes'] = Promocoes.objects.order_by('?').all()
        context['galeria_promocoes'] = Galeria_Promocoes.objects.order_by('?').all()
        context['servico'] = Servico.objects.order_by('?').all()
        context['dicas'] = Dicas.objects.order_by('?').all()
        context['footer'] = Footer.objects.order_by('?').all()
        return context

