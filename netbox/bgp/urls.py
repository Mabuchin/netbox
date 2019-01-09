from __future__ import unicode_literals

from django.conf.urls import url

from extras.views import ObjectChangeLogView
from . import views
from .models import Neighbor

app_name = 'bgp'
urlpatterns = [
    # Providers
    url(r'^bgp/$', views.NeighborListView.as_view(), name='neighbor_list'),
    #url(r'^bgp/add/$', views.NeighborCreateView.as_view(), name='neighbor_add'),
    #url(r'^bgp/import/$', views.NeighborBulkImportView.as_view(), name='neighbor_import'),
    #url(r'^bgp/edit/$', views.NeighborBulkEditView.as_view(), name='neighbor_bulk_edit'),
    #url(r'^bgp/delete/$', views.NeighborBulkDeleteView.as_view(), name='neighbor_bulk_delete'),
    #url(r'^bgp/(?P<slug>[\w-]+)/$', views.NeighborView.as_view(), name='neighbor'),
    #url(r'^bgp/(?P<slug>[\w-]+)/edit/$', views.NeighborEditView.as_view(), name='neighbor_edit'),
    #url(r'^bgp/(?P<slug>[\w-]+)/delete/$', views.NeighborDeleteView.as_view(), name='neighbor_delete'),
    #url(r'^bgp/(?P<slug>[\w-]+)/changelog/$', ObjectChangeLogView.as_view(), name='neighbor_changelog',
    #    kwargs={'model': Neighbor}),

]
