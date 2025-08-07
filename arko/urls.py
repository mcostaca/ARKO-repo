from django.urls import path, include
from .views import EstadoListView, MunicipioListView, DistritoListView, HomeView, PostLogin

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('postlogin/', PostLogin.as_view(), name='escolha-area'),
    path('estados/', EstadoListView.as_view(), name='estados-list'),
    path('municipios/', MunicipioListView.as_view(), name='municipios-list'),
    path('distritos/', DistritoListView.as_view(), name='distritos-list'),
    path('select2/', include('django_select2.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
