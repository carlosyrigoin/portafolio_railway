from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Portafolio, Visitas
from .forms import PortafolioForm

class PortafolioView(TemplateView):
    template_name = "administracion/portafolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["portafolios"] = Portafolio.objects.all()
        return context

class AdministracionView(LoginRequiredMixin, TemplateView):
    template_name = "administracion/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["portafolios"] = Portafolio.objects.all()
        context["visitas"] = Visitas.objects.all().order_by('-id')[:5]
        return context

class PortafolioCreate(LoginRequiredMixin, FormView):
    model = Portafolio
    template_name = "administracion/create.html"
    form_class = PortafolioForm

    def form_valid(self, form):
        Portafolio.objects.create(**form.cleaned_data)
        return redirect("administracion")


@login_required
def portafolioDelete(request, id):
    portafolio = Portafolio.objects.get(id=id)
    portafolio.delete()
    return redirect("administracion")