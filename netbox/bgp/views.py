from django.shortcuts import render
from django.views.generic import View
from utilities.forms import ConfirmationForm
from utilities.views import (
    BulkDeleteView, BulkEditView, BulkImportView, ObjectDeleteView, ObjectEditView, ObjectListView,
)
from . import filters, forms, tables
from .models import Neighbor, NeighborState
from .tables import NeighborTable


class NeighborListView(ObjectListView):
    queryset = Neighbor.objects.all()
    filter = filters.NeighborFilter
    filter_form = forms.NeighborFilterForm
    table = NeighborTable
    template_name = 'bgp/neighbor_list.html'

