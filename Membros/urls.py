from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import MembrosListView, MembrosCreateView, MembrosRetrieveView, MembrosUpdateView, MembrosDeleteView

urlpatterns = [
    path('listmembros/', MembrosListView.as_view(), name='membros-list'),
    path('membrocreate/', MembrosCreateView.as_view(), name='membros-create'),
    path('detalhemembro/<int:pk>/', MembrosRetrieveView.as_view(), name='membros-retrieve'),
    path('Atualizarmembro/<int:pk>', MembrosUpdateView.as_view(), name='membros-update'),
    path('Excluirmembro/<int:pk>', MembrosDeleteView.as_view(), name='membros-delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
