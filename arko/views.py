from django.views.generic import ListView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


from .models.localidades import Estado, Municipio, Distrito
import django_tables2 as tables
from django_tables2.views import SingleTableView

from .tables import EstadoTable, MunicipioTable, DistritoTable
from .forms import MunicipioSelectForm, DistritoSelectForm, EstadoSelectForm


class HomeView(FormView):
    template_name = 'home.html'
    form_class = AuthenticationForm
    success_url = '/postlogin/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context



class PostLogin(LoginRequiredMixin, TemplateView):
    template_name = 'postlogin.html'


class EstadoListView(LoginRequiredMixin,SingleTableView):
    model = Estado
    table_class = EstadoTable
    template_name = 'estados_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        estados_id = self.request.GET.get('estado')
        if estados_id:
            qs = qs.filter(id=estados_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EstadoSelectForm(self.request.GET)
        return context

class MunicipioListView(LoginRequiredMixin, SingleTableView):
    model = Municipio
    table_class = MunicipioTable
    template_name = 'municipios_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        municipio_id = self.request.GET.get('municipio')
        if municipio_id:
            qs = qs.filter(id=municipio_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MunicipioSelectForm(self.request.GET)
        return context

class DistritoListView(LoginRequiredMixin, SingleTableView):
    model = Distrito
    table_class = DistritoTable
    template_name = 'distritos_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        distrito_id = self.request.GET.get('distrito')
        if distrito_id:
            qs = qs.filter(id=distrito_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DistritoSelectForm(self.request.GET)
        return context
